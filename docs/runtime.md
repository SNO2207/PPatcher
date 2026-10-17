# Runtime verification

On 17 October 2026, a locally signed Parallels Desktop 27.0.3 build with the documented licensing changes started `Premium Linked Clone PoC` while the host client and dispatcher logged `PRL_ERR_LICENSE_NOT_VALID`. The Windows 11 guest reached its desktop. The VM process ran as uid 501; the packet helper ran as root.

With Shared Networking selected, the VM interface creation callback returned status 1000. Windows received `192.168.2.2/24` through gateway `192.168.2.1`. The logged-in guest user resolved `example.com` and fetched `https://example.com/` and Apple's connectivity endpoint. Both requests returned HTTP 200 with TLS verification result 0 and guest exit code 0. The helper admitted the signed VM and rejected an unrelated ad hoc signed diagnostic client.

The installed app passed recursive strict code-signature verification and the vendor initializer check. The original `__TEXT.__text` hashes in the client, dispatcher, and VM matched the pre-networking patched build. The networking addition changed a VM load command and signatures and added a dylib. This supports the conclusion that the licensing patches were preserved when networking was added.

The VM was cleanly shut down afterwards. This test did not establish complete product activation, every premium capability, bridged networking, port forwarding, simultaneous VM stability, or operation after a host reboot. The source app used for the new one-file builder was assembled from the exact original executable copies for an **offline build test**; the new installer and SDK start path have not been run end to end. The earlier manually assembled build supplies the runtime observations above.

Machine-readable historical evidence is in [runtime-success.json](networking/runtime_success.json) and [patch-preservation.json](networking/patch-preservation.json). The [research history](research-history.md) provides the sequence of prior checks and failures.
