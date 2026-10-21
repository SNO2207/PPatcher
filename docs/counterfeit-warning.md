# Counterfeit-warning detector

In Parallels Desktop 27.0.3 (58680) for ARM64, the blocking “This copy of Parallels Desktop may not be genuine” dialog uses SDK error `0xFFFFD4B9` (`-11079`). The client maps that result to the “Get Genuine Copy” button. A live debugger trace now identifies a local producer in `prl_client_app`, rather than an incoming dispatcher or licensing-service event.

## Producer and trigger

An LLDB breakpoint on the previously added dialog filter fired while the warning was generated. The caller stack was `prl_client_app` `sub_1000C0A68` → `libPrlGui.3.dylib` `CMessageProcessor::tryToShowMessage(CMessageInfo*)` → the filter. Registers at the filter held `0xFFFFD4B9`. IDA shows that `sub_1000C0A68` calls `CMessageManager::showMessageBox(4294956217, VM UUID, …)` when its timer callback receives `a1 == 1`.

The recurring function `sub_1000AE708` enumerates VMs, selects a VM whose state field is `0x30000004` (running), schedules that callback, and re-arms itself after 60 or 600 seconds. Its call site is in the GUI communicator constructor `sub_1000AD188`. That constructor reads the client executable's own Mach-O `LC_CODE_SIGNATURE` and Code Directory. If the integrity checks fail, including the test at `0x1000AD774` for the ad-hoc Code Directory flag, it schedules `sub_1000AE708` after 60 seconds. Local re-signing therefore activates the warning path.

The earlier search for an instruction containing the literal `-11079` missed this callback because the compiler materializes the value through a different instruction pattern. The live stack and decompilation establish the local producer for this warning; other license or integrity mechanisms may still exist.

## Patch and scope

The one-file builder changes the instruction at client VA `0x1000AD7B0` (file offset `0xAD7B0`) from `MOV W0, #0x20` (`00 04 80 52`) to `B 0x1000AD800` (`14 00 00 14`). This jumps over the block that allocates and registers the recurring counterfeit timer, then resumes normal communicator initialization. The builder requires a unique 16-byte context on each side of the instruction and the reviewed executable-section hash. IDA disassembly of the patched copy confirms the branch target.

The earlier downstream filter remains as a fallback. It branches from `isMessageShouldBeSkipped` at `0x1001F1DF8` to a checked code cave at `0x100002000`, returns true for `-11079`, and replays the original prologue for other messages. The button-response handler at `0x1001F3804` is unchanged. Neither patch changes an account entitlement or makes the application's signature genuine.

The dispatcher separately verifies a GUI peer's signing identifier and Team ID in `sub_100576FF8` for a TPM-syncing task; the VM has a reciprocal dispatcher peer check at `sub_10004BDBC`. Those checks have distinct call paths and are not the producer of this dialog.

## Verification on 21 October 2026

The patched client was installed and the application passed `codesign --verify --deep --strict`. The `Premium Linked Clone PoC` resumed and remained running. From inside the guest, DNS succeeded and HTTPS requests to `example.com` and Apple's success endpoint returned HTTP 200 with TLS verification success. The installed client contains the reviewed branch bytes at file offset `0xAD7B0`; the installed dispatcher and VM executables were unchanged by this update.

These checks establish that this particular timer registration is bypassed and that the tested VM can run with network access. They do not establish full activation, every premium feature, or that no other warning can appear later.
