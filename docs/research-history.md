# Parallels local entitlement patch experiment

This Python PoC modifies **copies** of the two ARM64 executables from Parallels Desktop **27.0.3 build 58680**. It is a reproducible static experiment for a vendor disclosure: it verifies the original file hashes and instruction bytes, applies named changes, records the changes, verifies the resulting files, and reconstructs byte-identical original copies.

**Verified:** all three profiles patched on-disk test copies successfully; IDA independently disassembled the 13 broader-profile sites and both new boot sites; restoration recovered the original SHA256 hashes; all 10 tests passed.

**Later runtime verification:** the five-site `feature-demo` deployment started successfully after signing and repairing installation attributes. It completed linked-clone creation while About reported that the application was not active. Directional clipboard choices were visible. See `runtime_verification.json` and the runtime notes below.

**Boot follow-up:** attempting to start the clone with `feature-demo` reached `LaunchVm → CheckLicense`, opened activation UI, and returned `PRL_ERR_LICENSE_NOT_VALID` before a VM engine started. The separate `boot-demo` profile targets that client method and a statically identified dispatcher start gate. It passed the client license step and started the VM process, but later VM-side checks still blocked the guest until the follow-on experiments described below. See `analysis/boot_investigation.json`.

**Later VM-start observations:** the installed `boot-demo` build passed client `CheckLicense`, reached `DspCmdVmStart`, and launched `prl_vm_app`. The VM first rejected the locally signed dispatcher, then the dispatcher rejected the locally signed VM. The companion `peer_pin.py` retains the dispatcher identifier check and pins its exact code hash; `local_team.py` changes the dispatcher's shared expected Team ID literal to the available local development Team ID. With both changes installed, the VM connected to the dispatcher. Two more VM-side checks blocked it in sequence. The companion `vm_config_gate.py` and `vm_license_status.py` reproduce the two follow-on instruction changes. With these installed, the dispatcher reported `VMS_RUNNING` and Windows 11 Setup appeared while the product still reported inactive. Networking did not initialize.

**Networking follow-up:** a restricted Shared/NAT packet helper restored internet access while the VM remained an ordinary-user process. Windows received `192.168.2.2`, resolved `example.com`, and fetched two HTTPS pages with HTTP 200 and TLS verification result 0. Every original Mach-O section in the client, dispatcher, and VM matched the preceding patched build. See [networking/README.md](networking/README.md) and `networking/runtime_success.json`.

**Not verified:** guest clipboard transfers, CPU/RAM limit bypasses, complete activation bypass, every premium capability, or long-duration networking stability. No unmodified runtime baseline was measured. Existing code signatures become invalid when patched, and the original Python licensing tool does not re-sign or install its outputs.

## Files

- `parallels_poc.py` — Python 3.9 or newer, standard library only.
- `test_parallels_poc.py` — format, branch encoding, original-binary, tamper rejection, and restoration tests.
- `feature_demo_manifest.json` — actual five-site test result, with source paths removed for submission.
- `local_checks_manifest.json` — actual thirteen-site test result, with source paths removed for submission.
- `boot_demo_manifest.json` — seven-site experiment adding two VM-start gates to `feature-demo`.
- `peer_pin.py` — separate exact-build copy-based patch for the VM process's dispatcher peer check.
- `local_team.py` — separate exact-build copy-based patch for the dispatcher's expected local Team ID.
- `vm_config_gate.py` and `vm_license_status.py` — two sequential, exact-build VM startup experiments with hash-checked reversal.
- `analysis/peer_pin.s` — assembly source for the 196-byte verification helper.
- `client_boot_after_ida.json` and `service_boot_after_ida.json` — IDA verification of the two boot-only changes.
- `service_after_ida.json` and `client_after_ida.json` — independent IDA disassembly of the patched copies.
- `validation.json` — hashes, patch counts, tests, and the limits of the verification performed.
- `runtime_verification.json` — subsequent startup repair, linked-clone creation, and guest-boot observations, with host-specific paths removed.
- `analysis/` — the preceding static analysis and original-code evidence.

The package contains no Parallels executables, license files, account tokens, or signing material.

## Profiles

| Profile | Scope | Sites |
| --- | --- | --- |
| `feature-demo` | Service premium feature matrix plus client linked-clone menu, clipboard choices and normalization, and new-VM resource normalization. Leaves the common license-validity getter and edition reader unchanged. | 5 |
| `local-checks` | All the above, plus experimental status/edition return overrides, the x86 edition rejection, CPU/RAM validation, the direct CPU-change restriction, and automatic sizing clamps. | 13 |
| `boot-demo` | The five feature sites plus client `CTaskLaunchVm::checkLicense` and the dispatcher's VM-start license acceptance branch. Leaves the shared validity getter and edition reader unchanged. | 7 |

The narrower profile is the default. It separates the local premium-feature hypothesis from base-license validity. The broader profile is an experiment, not a validated complete unlock. It does not override every client edition flag, reported resource limit, integrity decision, operation permission, or backend entitlement.

## Inspect the original build

Run commands from the directory containing this README. These commands read the installed executables; only `apply` writes new files, under its explicitly chosen output directory.

```sh
python3 parallels_poc.py inspect \
  --service '/Applications/Parallels Desktop.app/Contents/MacOS/Parallels Service.app/Contents/MacOS/prl_disp_service' \
  --client '/Applications/Parallels Desktop.app/Contents/MacOS/prl_client_app' \
  --profile feature-demo
```

Inspect prints the planned locations, original and replacement bytes, file offsets derived from Mach-O load commands, and expected hashes. A different build, architecture, or already modified input is rejected. There is no fuzzy matching and no force option.

## Create patched copies

Choose a new output directory; an existing directory is refused.

```sh
python3 parallels_poc.py apply \
  --service '/Applications/Parallels Desktop.app/Contents/MacOS/Parallels Service.app/Contents/MacOS/prl_disp_service' \
  --client '/Applications/Parallels Desktop.app/Contents/MacOS/prl_client_app' \
  --profile feature-demo \
  --output-dir './feature-demo'
```

This creates `feature-demo/prl_disp_service`, `feature-demo/prl_client_app`, and `feature-demo/manifest.json`. Original inputs stay unchanged. Both inputs are fully validated before any output files are written. The tool has no in-place patch mode and does not invoke Parallels, restart its service, touch account data, or make network requests.

For the broader candidate experiment, use `--profile local-checks` with a different output directory. The resulting executables are standalone test copies, not an installed or runnable application bundle.

For the separate VM-start experiment, use `--profile boot-demo` with a fresh output directory. This profile does not include the shared status/edition overrides from `local-checks`.

The peer check in the VM executable is a separate binary and is not part of `boot-demo`. To reproduce its local signing-identity adjustment from an original, unmodified `prl_vm_app`, run `python3 peer_pin.py apply --input /path/to/original/prl_vm_app --output ./prl_vm_app.peer-pin`. The companion tool rejects any other source hash, checks the exact hook and empty executable-space bytes, and verifies that reversing only its two changes recovers the original SHA256. The helper uses macOS `kSecCodeInfoUnique` to compare a 20-byte code hash plus `kSecCodeInfoIdentifier`; the hash is specific to the signed dispatcher used in this runtime test and must be recalculated if that dispatcher is re-signed or modified. Run `python3 local_team.py apply --input /path/to/unsigned/boot-demo/prl_disp_service --output ./prl_disp_service.local-team` for the reciprocal dispatcher-side check. This replaces a Team ID literal shared by three peer-verifier routines, so its scope is wider than the VM handshake; signing-identifier comparisons remain. After the peer adjustment, `python3 vm_config_gate.py apply --input ./prl_vm_app.peer-pin --output ./prl_vm_app.config-gate` reproduces the first separate VM startup experiment; it removes the license-parser boolean from the conjunction that accepts the configuration packet. `python3 vm_license_status.py apply --input ./prl_vm_app.config-gate --output ./prl_vm_app.license-status` reproduces the follow-on experiment that skips a second license-status branch. Each companion tool requires the exact previous-stage hash and supports `verify` to reconstruct it in memory.

## Verify and reconstruct originals

```sh
python3 parallels_poc.py verify --manifest './feature-demo/manifest.json'

python3 parallels_poc.py restore \
  --manifest './feature-demo/manifest.json' \
  --output-dir './restored'
```

Verification checks the patched instructions, the manifest against the tool’s compiled patch definitions, and the full original hashes after reversing the changes in memory. Extra byte changes and manifest tampering are rejected. Restore writes fresh original copies into another new directory; it does not replace files in the application bundle.

## Run the tests

Basic tests run without vendor binaries:

```sh
python3 -m unittest discover -s . -p 'test_*.py' -v
```

For the five additional original-binary tests, place unmodified `prl_disp_service` and `prl_client_app` in a directory and pass that directory through `POC_TEST_SOURCE_DIR`:

```sh
POC_TEST_SOURCE_DIR='/path/to/original-copies' \
  python3 -m unittest discover -s . -p 'test_*.py' -v
```

The original-binary tests were run against the exact files identified in the included manifests. They confirm round trips, unchanged source inputs, rejection of extra modifications, and refusal to overwrite existing output directories.

## Runtime verification and startup repair

The runtime test on 17 October 2026 used the five-site `feature-demo` profile. After ad-hoc signing, recursive strict verification of the complete installed app passed. Signing changes executable hashes, so preserve unsigned patched copies for the patch tool's hash-based verification and restoration. The immutable patch manifests describe the copy-generation stage; subsequent runtime observations are recorded separately.

Copying the complete bundle through staging lost installation ownership and privileged-helper permissions. The unmodified vendor initializer's `check` command reported that `Parallels Service` had mode `0755`, while `exceptions.list` requires root ownership, group `accessibility`, and mode `6755`. It also requires `prl_update_helper` to be owned by `root:wheel` with mode `4755`.

IDA showed that the initialization path checks the bundle against Parallels' Team ID before launching the initializer. The ad-hoc bundle failed that vendor requirement even though its signature was valid on disk. Running the unmodified vendor `inittool2 init -b` for the installed bundle with administrator authentication restored the installation attributes and bootstrap files. Its subsequent installation check passed. The five patches and executable bytes were unchanged; no additional binary patches were needed. Parallels then reached Control Center with its dispatcher running.

While About reported "This copy of Parallels Desktop is currently not active," the Linked Clone command created a separate test VM. The dispatcher returned `PRL_ERR_SUCCESS` for `DspCmdDirVmClone`; the new configuration contained linked-VM and linked-snapshot references, and its disk parent GUID matched that snapshot. About still reported inactive after the operation. The test clone and the source snapshot created by Parallels were retained as local evidence and are not included in this package.

The configuration editor exposed Windows-to-Mac-only and Mac-to-Windows-only clipboard choices. Guest transfers were not tested. A later guest-start attempt was blocked by license validation before the VM engine started. A temporary configuration-editor delay coincided with macOS requesting Documents-folder access for the new signing identity; the editor became accessible after the system request resolved.

Further runtime attempts installed the `boot-demo` changes and then both peer-identity adjustments. The installed bundle passed recursive strict code-signature verification and the vendor installation check. The VM process connected to the dispatcher, proving that the reciprocal identity checks passed in this test. It then logged `Failed to get VM configuration` and returned `PRL_ERR_VM_POWER_ON_FAILED`. IDA identified the VM-side startup function at `0x100057E14`: it requires three nonempty packet fields, a nonempty decoded object, and two nonempty license-information strings passed to `sub_1000FFF90`.

A later test removed the license-parser result from that conjunction at `0x10005839C`. The VM then parsed the linked clone's configuration, logged its Windows 11 CPU and memory settings, and progressed through `SetVmConfig`. Startup still failed: the same function checks a separate license-validation status at object offset `0x470` and branches at `0x1000589CC` when it is nonzero, logging `Failed to set VM configuration`. IDA traces the status write to `sub_1000FFF90` calling `sub_1001A205C` on the decoded license JSON. This establishes that the earlier conjunction was one gate but not the final VM startup gate.

After replacing only that second branch with a NOP, the installed VM entered its running state. The dispatcher returned `PRL_ERR_SUCCESS` for `DspCmdVmStart` and reported `VMS_RUNNING`. The guest display reached Windows 11 Setup and showed installation progress. At the same time, dispatcher startup logged `Can't load license info` and `PRL_ERR_LICENSE_NOT_VALID`, and the About dialog still said the copy was not active. This is direct runtime evidence that the linked-clone VM could boot without product activation in this local test. It does not establish a completed Windows installation, usable desktop, or all premium capabilities. The agent did not accept a Windows license agreement. The unmodified vendor installation check and recursive strict code-signature verification passed for the installed bundle.

The VM displayed `PRL_NET_PRLNET_OPEN_FAILED`: it continued running without a network connection. Its log shows two `vmnet_start_interface` attempts, each returning status `1001`, followed by `Failed to setup bind-mode virtual netif #0`. Apple's vmnet SDK defines `1001` as `VMNET_FAILURE` (general failure), not the more specific `VMNET_NOT_AUTHORIZED` (`1010`). The failure is at host virtual-interface creation, before guest network use; see `analysis/runtime_network_failure_log_excerpt.txt`.

The locally signed VM carried `com.apple.security.hypervisor` and `com.apple.security.cs.allow-unsigned-executable-memory`, but lacked the original vendor signature's restricted `com.apple.vm.networking` entitlement. Apple documents that entitlement for vmnet API access. Earlier probes showed macOS killed locally signed VM builds containing `com.apple.vm.device-access` or `com.apple.vm.networking`, including a development-certificate build containing both. Missing networking entitlement is therefore a plausible cause, but the generic `1001` status and lack of a direct authorization-denial log do not establish it as the sole cause. The missing `VmInfo.pvi` warning was concurrent in earlier attempts and has not been shown to cause a startup failure. Apple reference: https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.vm.networking

A standalone `vmnet_probe.c` follow-up called the same public `vmnet_start_interface` API with Shared mode and no restricted entitlement. It returned `1001` under the ordinary user (`uid=501, euid=501`), then returned `1000` (`VMNET_SUCCESS`) when run once with administrator authorization (`uid=0, euid=0`). The administrator probe immediately stopped its temporary interface successfully (`1000`). It installed no helper and made no persistent host configuration change. This strongly supports a privilege or entitlement cause rather than a generally broken host vmnet service. It does not establish that every Parallels-specific network parameter is otherwise correct. Running the patched guest as administrator was not tested.

The subsequent networking helper test reached the Windows desktop and verified DNS plus HTTPS from the logged-in Windows user. At that launch, the host dispatcher and client still logged `PRL_ERR_LICENSE_NOT_VALID`. The helper owns the privileged vmnet interface and proxies packets over XPC; the VM runs with uid 501. This resolves the initial network limitation for Shared/NAT in this local test. It does not establish bridging, port forwarding, complete activation, every premium capability, or a controlled comparison against an unmodified build.

## Suggested vendor report wording

> Static analysis of build 58680 identifies local edition and feature-matrix decisions governing premium capabilities. This PoC reproducibly alters those decisions in copies of the ARM64 executables. The output instructions were independently checked in IDA, and reversal restores the original file hashes. A five-site runtime deployment completed linked-clone creation while About reported that the application was not active. Additional VM-start changes passed the client license gate, reciprocal peer checks, and two VM-side license checks. The dispatcher returned success and the linked clone reached `VMS_RUNNING`. A later Shared/NAT packet helper restored internet access: Windows reached its desktop and verified DNS and HTTPS with valid TLS while the host still logged an invalid license. All original patched executable sections were preserved. Full activation, every premium capability, long-duration stability, and an unmodified runtime baseline remain unverified.

A stronger causal claim requires a controlled before-and-after reproduction with the same build, host, VM, and account/license state, demonstrating that the feature is unavailable before modification. Local binary modification may fall outside the vendor's accepted vulnerability scope; no severity or reward eligibility is asserted here.
