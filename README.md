# Parallels Desktop local licensing PoC

This repository contains one self-contained Python entrypoint, [`parallels_onefile.py`](parallels_onefile.py), and the evidence behind a local test on Parallels Desktop **27.0.3 (58680) for Apple silicon**. It builds a separately signed application bundle with the client, dispatcher, and VM changes from the investigation, installs a restricted Shared/NAT networking helper, and can check DNS and HTTPS in an already registered Windows guest. No Parallels application, guest disk, certificate, private key, license, or account token is included.

The observed result on 17 October 2026 was specific: a linked clone started and reached the Windows desktop while the host logged `PRL_ERR_LICENSE_NOT_VALID`; the guest resolved `example.com` and fetched two HTTPS pages with HTTP 200 and TLS validation success. This does **not** establish full activation, all premium capabilities, or reliability after a future Parallels update. See [runtime evidence](docs/runtime.md).

## Requirements

- Apple silicon Mac with Parallels Desktop 27.0.3 build 58680 or a 27.x package whose three executable `__TEXT.__text` sections and all anchors still match that reviewed build.
- A separate, unmodified Parallels Desktop application bundle supplied by the operator. The currently patched installation is not valid build input.
- Xcode command-line tools, Python 3.9 or newer, and a local Apple Development signing identity. The identity must have a ten-character Team ID. The identity string is supplied on the command line and no private key is exported.
- A stopped VM and a quit Parallels UI before installing. Administrator authorization is needed to replace the application and install the root helper.
- An existing registered Windows VM with Parallels Tools for `verify-guest`; the test used `Premium Linked Clone PoC`. The script patches Parallels' **VM executable**. It does not generate a Windows installation or clone a guest disk.

## One-command flow

First inspect a clean source bundle:

```sh
python3 parallels_onefile.py inspect --source-app '/path/to/original/Parallels Desktop.app'
```

Then build, install, and verify. Use a fresh output directory outside this repository. The optional `--vm-name` starts the named registered guest and runs the network checks; omit it to leave all guests stopped.

```sh
python3 parallels_onefile.py all \
  --source-app '/path/to/original/Parallels Desktop.app' \
  --output "$HOME/Parallels-PoC-Build" \
  --identity 'YOUR_CODESIGN_IDENTITY_SHA1' \
  --vm-name 'Premium Linked Clone PoC'
```

The install phase prompts for macOS administrator authorization. It retains the previous app as `/Applications/Parallels Desktop.poc-backup-YYYYMMDD-HHMMSS.app`. If the root install step fails, it attempts to restore that app and the previous network helper. The output folder contains a patched vendor bundle and must stay local; the `.gitignore` excludes it from Git.

For a reviewable staged flow, use the same entrypoint with separate commands:

```sh
python3 parallels_onefile.py build --source-app '/path/to/original/Parallels Desktop.app' \
  --output "$HOME/Parallels-PoC-Build" --identity 'YOUR_CODESIGN_IDENTITY_SHA1'
python3 parallels_onefile.py verify-build --output "$HOME/Parallels-PoC-Build"
python3 parallels_onefile.py install --output "$HOME/Parallels-PoC-Build"
python3 parallels_onefile.py verify-installed --output "$HOME/Parallels-PoC-Build"
python3 parallels_onefile.py verify-guest --vm-name 'Premium Linked Clone PoC' --start
```

`verify-guest` runs fixed `nslookup.exe` and `curl.exe` checks under the current logged-in Windows user through Parallels' local SDK. It does not request or store a guest password. The command prints results; it does not shut down the guest. Use Parallels Actions → Shut Down when finished.

## How the script works

1. It parses each thin ARM64 Mach-O, confirms its executable `__TEXT.__text` section hash, and searches for a **unique 16-byte context before and after** every reviewed patch site. It confirms the original instruction bytes and their Mach-O address mapping before writing any output. Packaging or signature changes can change the whole-file SHA256 without invalidating those code anchors. A changed executable section, ambiguous anchor, occupied code cave, or insufficient load-command padding stops the build. The tool does not infer that changed code has equivalent licensing behavior.
2. It applies the five client, two dispatcher, and three VM instruction changes reproduced in the earlier static analysis. The dispatcher’s expected Team ID literal is changed to the local signing Team ID. The dispatcher is signed and its actual CDHash is placed into the VM peer-check helper, so this value is derived anew for every build. The VM’s original identifier check is retained.
3. It compiles an embedded C vmnet helper and VM interposition library. The helper runs as an on-demand root launchd service and allows only the current user’s locally signed VM identity. The library forwards Shared/NAT vmnet packets over XPC. The VM stays under the ordinary user account. Bridge mode, host-only mode, and port forwarding are outside this implementation.
4. It signs the dispatcher ad hoc with its original smartcard entitlement, the VM and interposition library with the local development identity, and the outer app ad hoc with the launchable client entitlement set. It verifies the complete staged bundle using `codesign --verify --deep --strict`.
5. Installation copies the verified build through `/private/tmp`, saves the old app, runs the unmodified vendor initializer to restore helper ownership and permissions, installs the root network helper, and checks the installed signature and file hashes. The source bundle is never patched in place.

The embedded helper, shim, and broker header are compressed text inside the Python file. At build time the script verifies each embedded source SHA256 before compiling. The script uses only the Python standard library plus macOS command-line tools.

## Update behavior and limits

The anchors provide **limited update tolerance**, not automatic compatibility with arbitrary future binaries. A repackaged or re-signed 27.x app with unchanged reviewed code sections can pass. When executable code changes, the script refuses to patch. A fresh IDA review and new tests are required to support that build. This is deliberate: a blind pattern match at a licensing branch cannot establish the meaning of new control flow, and the VM peer helper contains relative ARM64 calls tied to this code layout.

The runtime evidence covers linked-clone creation and boot, the Windows desktop, and Shared/NAT internet access on one host. Clipboard transfer, all resource-limit paths, full activation state, bridged networking, multiple concurrent VMs, and host reboot behavior were not tested. The linked clone depends on its parent VM and snapshot; do not remove either while using it.

Detailed analysis: [licensing](docs/licensing-analysis.md), [edition checks](docs/edition-checks.md), [network helper](docs/networking/README.md), [runtime verification](docs/runtime.md), and [historical investigation](docs/research-history.md).

This is a private research package prepared for vendor disclosure. It contains source and observations, not vendor binaries or guest images.
