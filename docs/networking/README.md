# Shared/NAT networking helper experiment

The installed Parallels Desktop 27.0.3 (58680) test VM has internet access with its existing licensing changes preserved. Windows received `192.168.2.2/24` through gateway `192.168.2.1`. From the logged-in Windows session, `nslookup example.com` succeeded and `curl.exe` fetched `https://example.com/` and Apple's connectivity page with HTTP 200, TLS verification result 0, and exit code 0. `guest-network-check.txt` contains the captured output; local DNS suffix and IPv6 identifiers are omitted.

The host client and dispatcher logged `PRL_ERR_LICENSE_NOT_VALID` at this launch. `patch-preservation.json` compares every original Mach-O section in the three executables against the preceding patched installation: all match, including each `__TEXT.__text` hash. The networking addition changes a Mach-O library-load command and signatures, and adds a dylib. It does not alter those existing sections. The installed application passed recursive strict code-signature verification.

## Architecture

`helper.c` runs as root under the on-demand launchd service `local.codex.parallels-poc.vmnet`. It opens an Apple vmnet interface in Shared/NAT mode. `shim.c`, loaded by the VM executable, proxies interface startup, shutdown, packet events, reads, and writes over XPC. The VM remains uid 501; the helper owns the privileged interface. No restricted entitlement is added to the VM.

The helper checks the connecting process's effective UID and code-signature requirement. This local build permits uid 501 with development Team ID `NT7B2P5VPY` and signing identifier `com.parallels.vm` or `local.codex.vmnet.client`. These identifiers are public code-signing metadata, not credentials. The requirement is deliberately specific to this local experiment. The helper accepts at most four active connections and bounds packet count and frame size. It provides no command execution, arbitrary file access, bridge configuration, or port-forwarding operation. An unrelated ad-hoc signed client was rejected in the negative test.

The installed paths are:

- `/Library/PrivilegedHelperTools/local.codex.parallels-poc.vmnet`
- `/Library/LaunchDaemons/local.codex.parallels-poc.vmnet.plist`
- `/var/log/local.codex.parallels-poc.vmnet.log`
- `/Applications/Parallels Desktop.app/Contents/MacOS/Parallels VM.app/Contents/Frameworks/PoCVMNet.dylib`

## Validation

The standalone diagnostic first reproduced legacy vmnet failure 1001 as uid 501 and success 1000 as root. A newer network-object API failed on this host even as root, so it was not used. The successful packet-proxy diagnostic sent a DHCP Discover and received an offer as uid 501. The same test passed when the dylib was loaded using a Mach-O load command rather than a process environment variable. The installed VM then started its interface with status 1000 and reached the Windows desktop. Guest network commands ran through the local SDK as the logged-in Windows user. No user credentials were supplied or stored.

`runtime_success.json`, `runtime-log-excerpt.txt`, `installed-checks.json`, and the captured guest output record the result. The SDK verification client uses the installed SDK 11 ABI; its session selector identifies the current-user mode and is not an authentication secret. SDK ABI reference consulted: [OpenClaw's Parallels guest execution client](https://github.com/openclaw/openclaw/blob/main/scripts/e2e/parallels/parallels-exec.py).

## Scope and limitations

This is a local diagnostic implementation, not a production networking backend. It is restricted to Shared/NAT and overrides the VM's legacy interface description with that mode; keep the test VM configured for Shared Networking. Bridged and host-only operation and port forwarding are not implemented. Throughput, long-duration stability, concurrent VMs, and host-reboot behavior were not tested. Small session and interface handles are retained until process exit to protect asynchronous callback lifetimes. Networking success does not establish every premium capability or a complete activation bypass.

The sources require macOS, Xcode command-line tools, and a local signing identity for the VM and diagnostic client. `add_network_library.py` writes a separate ARM64 Mach-O copy, refuses insufficient header padding, and verifies that original section bytes remain intact. Installation and signing were performed separately; no vendor binaries or private signing material are included here.

For the local rollback, shut down the VM and quit Parallels, then use the workspace's `work/networking/prepare_rollback.py`. It prepares a temporary, administrator-run restore script using the saved preceding patched app. That restores the pre-networking test build and removes only this experiment's launchd service and helper. It does not restore a vendor-original application or modify the VM's disk.

Apple API reference: [vmnet](https://developer.apple.com/documentation/vmnet). The historical missing-entitlement diagnosis is in `../analysis/vm_signing_diagnosis.json`.
