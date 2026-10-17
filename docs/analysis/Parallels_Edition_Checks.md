# Parallels Desktop licensing and edition enforcement points

The main edition switch is in the service’s feature matrix builder, **`0x1001415D8`**. Its branch at **`0x100141748`** skips 23 feature IDs unless `(edition & ~1) == 2`, meaning edition 2 or 3. This is a more direct premium feature control than the generic license-validity getter.

Several independent checks also matter: VM startup validity, x86 emulation edition eligibility, CPU and RAM validation, CPU change validation, automatic resource sizing, and client configuration normalization. A change confined to one of these does not cover the others.

These are confirmed static enforcement points in **Parallels Desktop 27.0.3 build 58680 ARM64**, not a tested complete patch set. The [evidence appendix](Parallels_Edition_Checks_Evidence.md) includes original instructions, pseudocode, and call paths. The installed application and workspace executable copies were not modified.

## Binary identity

| Binary | SHA256 | Address convention |
| --- | --- | --- |
| `prl_disp_service` | `d9f2fff825b4e97400bfffb110b96b242d246d93aa3f4da05308f3e4319d6c26` | IDA image base `0x100000000` |
| `prl_client_app` | `8aafd57766594be4120607f69e795966cd5615f02d0cd79563e05b57ef49527f` | IDA image base `0x100000000` |
| `libprl_sdk.11.dylib` | `3fc83b8938ede4fc5ed385c2dcdea949da7f5302f4491ed868df4be39c84ae2a` | ARM64 slice, IDA image base zero; hash covers the universal file |

Addresses are virtual addresses, not file offsets. Decompiled `sub_...` routines are stripped functions; the descriptions below are analytical labels.

## Service checks

| Control | Exact location | Original condition and effect | Outcome a local bypass would have to achieve |
| --- | --- | --- | --- |
| Common license-status getter | Function `0x100279B3C`; disabled-state branch `0x100279B40`; validator tail call `0x100279B50` | Tests bit 0 at object offset `0x38`; otherwise evaluates parsed entitlement through `0x10031A878`. Zero means valid. | Return a valid status to callers. This supplies neither premium feature membership nor larger resource limits. |
| VM startup validity | `0x100057FC4` call; `0x100057FC8`: `CBZ W0, loc_100058320` | Zero license status enters the continuation; nonzero enters the license error path. | Reach the valid continuation. This is one caller of the shared getter. |
| Snapshot switching validity | `0x10005ED14` call; `0x10005ED18`: `CBZ W0, loc_10005EE9C` | Same status check, independently used by snapshot switching. | Reach the valid continuation. A startup-only change leaves this path intact. |
| Premium feature matrix | `0x100141740`–`0x100141748`; rejecting instruction `B.NE loc_1001419C0` | Computes `edition & 0xFFFFFFFE`, compares with 2, and skips the premium insertion block when unequal. | Include the required feature IDs in the published supported set. |
| x86 emulation edition | `0x1000582A4`–`0x1000582AC`; rejecting instruction `B.NE loc_1000584AC` | For an emulated x86 VM, accepts only `(edition & ~1) == 2`. Failure logs the Professional/Business restriction. | Pass this edition decision as well as ordinary validity checks. |
| CPU/RAM validation activation | `0x1000A23D8` edition call; `0x1000A23E0`: `B.NE loc_1000A2AE0` | On this build’s normal path, edition 1 enters the resource-limit checks; other editions skip this routine’s restriction block. | Avoid producing the licensing resource errors, while preserving unrelated configuration validation. |
| CPU count comparison | `0x1000A2460`: `CMP W0, W20`; `0x1000A2464`: `B.LS loc_1000A26C0` | Actual vCPU count is compared with `cpu_limit`, default 8. Exceeding it produces error `-26501`. | Keep the requested CPU count within the effective accepted limit or prevent this licensing rejection. |
| RAM comparison | `0x1000A273C`: `CMP W0, W20`; `0x1000A2740`: `B.LS loc_1000A2AE0` | RAM is compared with `ram_limit`, default `0x2000` MiB. Exceeding it produces `-26502`, or combines with the CPU error as `-26505`. | Pass the RAM licensing comparison. |
| Independent CPU change check | Function `0x100238AFC`; comparison `0x100238BC4`; `0x100238BC8`: `B.LE loc_100238C08` | If CPU count changes, compares the new count with `cpu_limit`, default 8. Exceeding it returns `-26501`. There is no edition test in this function. | Accept the new CPU count here too. This survives an override of the earlier edition-1 validator. |
| Automatic CPU clamp | Function `0x1002E8FEC`; `0x1002E909C` comparison, `0x1002E90A0` branch | Automatically calculated CPU count is capped at entitlement `cpu_limit`. | Retain the intended count rather than silently reducing it. |
| Automatic RAM clamp | Function `0x1002E9168`; `0x1002E9230` comparison, `0x1002E9234` branch | Automatically calculated RAM is capped at entitlement `ram_limit`, alongside a separate host maximum. | Retain the intended RAM allocation within host constraints. |

The resource error strings previously identified at `0x1000B7EF8` are **consumers of validation errors**, rather than the original CPU/RAM comparison sites. Changing only their messages or error reporting would miss the producers above. That distinction is established by tracing `0x1000B7EF8 → 0x1000A1BEC → 0x1000A238C`.

The independent CPU change validator is called by `0x10022BBBBC`.

## The edition reader and feature matrix

The shared edition reader is **`0x100013368`**. It reads JSON field `edition`, defaults to 1, and maps values 4 and above back to 1. Both the feature matrix builder and x86 emulation check consume its result. Their accepted premium values are 2 and 3.

The premium block in `0x1001415D8` inserts these feature IDs:

```text
17, 19, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31,
32, 33, 34, 37, 38, 39, 40, 41, 43, 45, 46
```

Feature 20 has additional host/version conditions. Other feature IDs are inserted outside the premium branch. The feature matrix therefore mixes edition policy with host and configuration capabilities; it is not simply one boolean for the entire product.

`0x10003CB7C` rebuilds the set and publishes a feature-matrix-changed event with parameter 150. At initialization, `0x10002B090` also obtains the supported set. This explains why a durable change would need to affect the producer or every relevant consumer, rather than only a transient client cache.

## Client and SDK feature checks

The client wrapper **`0x1000BECA4`** calls `PrlSrv_IsFeatureSupported`, then applies client-side rules. The SDK path is:

```text
SDK 0x31C40  PrlSrv_IsFeatureSupported
  → 0x47434  locks the server handle and writes the output boolean
  → 0x18F488 checks membership in the supported-feature set
```

The SDK function returns an API status separately from the output boolean. Returning API success alone does not assert feature availability; the output boolean must also indicate support.

Confirmed consumers include:

| Feature | Client enforcement point | Observed behavior |
| --- | --- | --- |
| Linked-clone menu, ID 21 | `0x100508020` call; `0x100508024`: `CBZ W0, loc_1005080E4` | Omits the `New Linked Clone...` action when unsupported. Other checks in this block still apply. |
| Additional VM profiles, ID 24 | Function `0x1000E868C` | Uses feature availability before obtaining additional profile choices. |
| Resource configuration, ID 26 | `0x1000E85AC` call; `0x1000E85B0`: `TBNZ W0, #0, loc_1000E860C` | When unsupported, this configuration helper caps RAM at 8192 MiB and CPU count at 4. This is separate from the service’s default CPU limit of 8. |
| Directional clipboard choices, ID 46 | `0x1002C0CDC` call; `0x1002C0CE0`: `CBZ W0, loc_1002C1018` | Omits the directional clipboard choices when unsupported. |
| Clipboard value normalization, ID 46 | `0x1002A28E0` call; `0x1002A28E4`: `TBNZ W0, #0, loc_1002A2930` | If unsupported, converts directional clipboard modes 2 or 3 to mode 1. Merely exposing the combo-box entries leaves this normalization intact. |

The linked-clone menu check is a confirmed UI control. This trace does not establish that changing that menu alone would make the service accept every clone operation.

## Edition flags and published limits

Client license objects store a flag word at offset `0x38`:

- `0x100420670` tests whether all requested flag bits are present, with special handling for a zero mask.
- `0x1004206CC` tests whether any requested bits are present.
- `0x1004206BC` tests whether none are present.

In the reviewed consumers, mask `0x10000` identifies Pro and `0x80` identifies Business; combined mask `0x10080` accepts either. These helpers also serve trial, subscription, and registration logic with other masks. Making every helper return the same boolean would change unrelated—and sometimes opposite—decisions.

Service exporter **`0x1000BF974`** also publishes entitlement limits to clients: CPU limit as event parameter **135**, RAM limit as parameter **136**. Its JSON reads are at `0x1000BFC30` and `0x1000BFCA4`. Consequently, changing service comparisons without changing the exposed effective limits can leave client controls showing the original caps.

## Signature verification is a separate choice

If the approach changes the signed entitlement itself, signature acceptance becomes relevant:

```asm
0x100279B84  BL   sub_1004626AC
0x100279B88  TBZ  W0, #0, loc_100279C9C
```

The second instruction enters the signature-failure path when verification returns false. The acceptance routine still parses JSON and applies caller-selected policy after signature verification.

Signature verification is **not inherently a required patch for every possible local bypass**: overriding a downstream decision could leave the stored signed payload untouched. Conversely, changing signature acceptance alone does not grant premium edition membership or larger limits. These are alternative intervention layers, not a list that must all be changed indiscriminately.

## What is established

The exact shared premium branch, startup edition branch, CPU/RAM comparison sites, direct CPU change check, automatic clamps, and selected client gates are confirmed in IDA. The [original-code appendix](Parallels_Edition_Checks_Evidence.md) records them for inspection.

No modified executable was run, and no complete unlock was validated. Guest compatibility, VM state, host resource ceilings, service-side operation permissions, and server-issued account entitlements remain separate conditions. The identified locations therefore support targeted investigation; they are not evidence that a particular instruction replacement unlocks every premium capability.
