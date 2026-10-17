#!/usr/bin/env python3
"""Self-contained local reproduction tool for the Parallels 27.0.3 ARM64 PoC.

The only source input is a vendor application bundle supplied by the operator.
The tool never downloads Parallels binaries, signing keys, or guest images.
Run ``inspect`` before ``build``. ``all`` combines build, install, and checks.
"""
from __future__ import annotations

import argparse
import base64
import ctypes as C
from contextlib import ExitStack
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import plistlib
import re
import shlex
import shutil
import struct
import subprocess
import sys
import tempfile
import time
import zlib

VERSION = "1.0.0"
EXPECTED_BUILD = "27.0.3 (58680)"
APP_NAME = "Parallels Desktop.app"
NET_LIBRARY = "@executable_path/../Frameworks/PoCVMNet.dylib"
HELPER_LABEL = "local.codex.parallels-poc.vmnet"
PATHS = {
    "client": "Contents/MacOS/prl_client_app",
    "service": "Contents/MacOS/Parallels Service.app/Contents/MacOS/prl_disp_service",
    "vm": "Contents/MacOS/Parallels VM.app/Contents/MacOS/prl_vm_app",
}
VM_APP = "Contents/MacOS/Parallels VM.app"
SERVICE_APP = "Contents/MacOS/Parallels Service.app"
VM_ENTITLEMENTS = {
    "com.apple.security.cs.allow-unsigned-executable-memory": True,
    "com.apple.security.hypervisor": True,
}
SERVICE_ENTITLEMENTS = {"com.apple.security.smartcard": True}
CLIENT_ENTITLEMENTS = {
    "com.apple.security.automation.apple-events": True,
    "com.apple.security.device.audio-input": True,
    "com.apple.security.device.camera": True,
    "com.apple.security.personal-information.addressbook": True,
    "com.apple.security.virtualization": True,
}

# Generated from independently reviewed ARM64 sites in the vendor build.
# The 16-byte contexts on both sides are unique within their original files.
ANCHOR_DATA = [{'name': 'premium-matrix', 'binary': 'service', 'va': 4296283976, 'before': 'c1130054', 'after': '1f2003d5', 'anchor': 'fe121194e00315aa08781f121f090071c113005428028052e81300b9e0830091e1430091'}, {'name': 'linked-clone-menu', 'binary': 'client', 'va': 4300242980, 'before': '00060034', 'after': '1f2003d5', 'anchor': 'e003899af822ef97a102805221dbee9700060034a89640f9e80000b4080540b9a8000034'}, {'name': 'clipboard-choices', 'binary': 'client', 'va': 4297854176, 'before': 'c0190034', 'after': '1f2003d5', 'anchor': 'a00e40f91b0aff97c1058052f2f7f797c019003440be0090004446f9012b00b021681391'}, {'name': 'clipboard-normalization', 'binary': 'client', 'va': 4297730276, 'before': '60020037', 'after': '13000014', 'anchor': 'a00e40f91a83ff97c1058052f170f89760020037887a1f121f0900710102005408c500d0'}, {'name': 'new-vm-resource-clamp', 'binary': 'client', 'va': 4295919024, 'before': 'e0020037', 'after': '17000014', 'anchor': '30491994e00316aa41038052be59ff97e0020037e00313aa8d611994245d19947a691994'}, {'name': 'client-vm-boot-license', 'binary': 'client', 'va': 4296259008, 'before': 'ff8301d1f65703a9', 'after': '00008052c0035fd6', 'anchor': '00119f1afd7b41a9f44fc2a8c0035fd6ff8301d1f65703a9f44f04a9fd7b05a9fd430191080c40f9'}, {'name': 'dispatcher-vm-boot-license', 'binary': 'service', 'va': 4295327688, 'before': 'c01a0034', 'after': 'd6000014', 'anchor': 'e86340f9080540f900c10091de860894c01a0034e86340f9080540f900c10091d9860894'}, {'name': 'peer-hook', 'binary': 'vm', 'va': 4304880704, 'before': 'e00340f9', 'after': 'f036da17', 'anchor': '082941f9010140f924850094f50300aae00340f968160090082d41f9010140f91e850094'}, {'name': 'vm-config-gate', 'binary': 'vm', 'va': 4295328668, 'before': '0801180a', 'after': '1f2003d5', 'anchor': 'a80355f8080540b91f010071e8079f1a0801180a1f05007101180054e003679eea230191'}, {'name': 'vm-license-status', 'binary': 'vm', 'va': 4295330252, 'before': '15030035', 'after': '1f2003d5', 'anchor': '681240f9157144b9e0230091c4f1fe9715030035a80354f8080540b9c8000034681240f9'}]
REFERENCE = {'client': {'text_sha256': '8d03aeba8053a63075138d3d5dd9a9d377378e8f4ed581b0d3f74038ed4be1ac'}, 'service': {'text_sha256': '18a0ed653c7b06a0bd07a321acbf4158c11f26b07fcc4fde00a1aedc7bf960c0', 'team_anchor': '78797a303132333435363738392b2f0034433633363441435854002f7573722f62696e2f636f64657369'}, 'vm': {'text_sha256': '7cf68473ed374fb5ed9793e5b5f5743ab3ae22de6f9b8f51f59b5f30b654cfda'}}
PEER_CAVE = {'va': 4294975488, 'template': 'e00313aae10314aa022080520200a172b54e2694f40300aa340400b4e0031faa41040010022080520200a172ae4e2694f30300aa530300b4e00340f9e10313aa224e2694f60300aa760200b4e00316aa034e26941f5000f1e1010054e00316aafc4d2694800100b441020010820280d2f85c269400010035e00314aae10315aae2031faa894e26941f0000f1f6039f5a1ec92514160080121cc92514f3031faa160080121bc92514756e697175650000b2c37da2a3043d388da2696ea905a2acad23769e', 'reference_cdhash': 'b2c37da2a3043d388da2696ea905a2acad23769e'}
EMBEDDED_SOURCES = {'broker.h': {'sha256': 'c9f84c37c5d6abaaef94448c14a9be8ef95fc6020b86b361bbd7af6785593717', 'zlib_base64': 'eNpTLihKTM9NVMjPS07lUs7MS84pTUlVsCnLzUst0QeTehl2SBIpmcUFiSXJGfowBqp0RUGyPhCjChZXFuuXZuaDBVNS0zLzUhUC/J3jg12DwjydXRWUcvKTE3P0kvNTUiv0ChKLEnNyUnOKdQvyk/XADlBC0eXrGBEf4Ojs7RoSrGBkYIAh5xbk6OuqYGZqamzGBQDYZUid'}, 'helper.c': {'sha256': '44ed3220c367f71b9b891993f6dd7ae0c009312dfea46fb8f1fd5b35b90c79f6', 'zlib_base64': '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'}, 'shim.c': {'sha256': '307296562760e0414b53d1e77bc40f23a10b702d2c175a2b59405dfdf8a3edf2', 'zlib_base64': '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'}}


class Refused(RuntimeError):
    """A safety precondition failed; no install should be attempted."""


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def run(*args: str | Path, capture: bool = False) -> str:
    command = [str(arg) for arg in args]
    result = subprocess.run(command, check=True, text=True, stdout=subprocess.PIPE if capture else None,
                            stderr=subprocess.PIPE if capture else None)
    return (result.stdout or "") + (result.stderr or "")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Refused(message)


def sections(data: bytes) -> list[dict]:
    require(len(data) >= 32, "Truncated Mach-O")
    magic, cpu, _, kind, count, size, _, _ = struct.unpack_from("<IiiIIIII", data)
    require((magic, cpu, kind) == (0xFEEDFACF, 0x0100000C, 2),
            "Expected a thin ARM64 Mach-O executable")
    end, pos, found = 32 + size, 32, []
    require(count <= 4096 and end <= len(data), "Invalid Mach-O command table")
    for _ in range(count):
        require(pos + 8 <= end, "Truncated Mach-O command")
        cmd, command_size = struct.unpack_from("<II", data, pos)
        require(command_size >= 8 and pos + command_size <= end, "Invalid Mach-O command")
        if cmd == 0x19:
            require(command_size >= 72, "Truncated Mach-O segment")
            vmaddr, vmsize, fileoff, filesize, _, prot, nsects, _ = struct.unpack_from(
                "<QQQQiiII", data, pos + 24)
            require(72 + nsects * 80 <= command_size and fileoff + filesize <= len(data),
                    "Invalid Mach-O segment extent")
            for index in range(nsects):
                at = pos + 72 + index * 80
                name = data[at:at + 16].split(b"\0")[0].decode("ascii")
                segment = data[at + 16:at + 32].split(b"\0")[0].decode("ascii")
                addr, length, offset = struct.unpack_from("<QQI", data, at + 32)
                require(offset + length <= len(data), "Invalid Mach-O section extent")
                found.append(dict(name=name, segment=segment, addr=addr,
                                  size=length, offset=offset, prot=prot,
                                  vmaddr=vmaddr, vmsize=vmsize,
                                  fileoff=fileoff, filesize=filesize))
        pos += command_size
    require(pos == end, "Mach-O load command size mismatch")
    return found


def executable_offset(data: bytes, va: int, size: int) -> int:
    candidates = []
    for s in sections(data):
        if s["prot"] & 4 and s["vmaddr"] <= va and va + size <= s["vmaddr"] + min(s["vmsize"], s["filesize"]):
            candidates.append(s["fileoff"] + va - s["vmaddr"])
    require(len(set(candidates)) == 1, f"No unique executable mapping for {va:#x}")
    return candidates[0]


def text_hash(data: bytes) -> str:
    matches = [s for s in sections(data) if s["segment"] == "__TEXT" and s["name"] == "__text"]
    require(len(matches) == 1, "Expected one __TEXT.__text section")
    section = matches[0]
    return digest(data[section["offset"]:section["offset"] + section["size"]])


def source_check(app: Path) -> tuple[dict[str, bytes], dict]:
    require(app.is_dir() and app.name.endswith(".app"), "Source must be a Parallels .app bundle")
    info = plistlib.loads((app / "Contents/Info.plist").read_bytes())
    version = str(info.get("CFBundleShortVersionString", ""))
    build = str(info.get("CFBundleVersion", ""))
    require(version.startswith("27."), f"Unsupported major version {version} ({build})")
    blobs = {name: (app / path).read_bytes() for name, path in PATHS.items()}
    for name, data in blobs.items():
        require(text_hash(data) == REFERENCE[name]["text_sha256"],
                f"{name}: executable code changed; this version requires a new IDA review")
    for site in ANCHOR_DATA:
        data = blobs[site["binary"]]
        anchor = bytes.fromhex(site["anchor"])
        require(data.count(anchor) == 1, f"{site['name']}: anchor absent or ambiguous")
        at = data.find(anchor) + 16
        before = bytes.fromhex(site["before"])
        require(data[at:at + len(before)] == before,
                f"{site['name']}: instruction bytes changed")
        require(at == executable_offset(data, site["va"], len(before)),
                f"{site['name']}: address mapping changed; manual review required")
    vm = blobs["vm"]
    cave_at = executable_offset(vm, PEER_CAVE["va"], len(bytes.fromhex(PEER_CAVE["template"])))
    require(vm[cave_at:cave_at + len(bytes.fromhex(PEER_CAVE["template"]))] ==
            bytes(len(bytes.fromhex(PEER_CAVE["template"]))), "Peer pin code cave is occupied")
    team_anchor = bytes.fromhex(REFERENCE["service"]["team_anchor"])
    require(blobs["service"].count(team_anchor) == 1, "Dispatcher Team ID context changed")
    return blobs, {"version": version, "build": build,
                   "reference_build": EXPECTED_BUILD,
                   "update_compatibility": "Executable text sections and all patch anchors match the reviewed build",
                   "source_sha256": {n: digest(d) for n, d in blobs.items()},
                   "text_sha256": {n: text_hash(d) for n, d in blobs.items()},
                   "anchors": [s["name"] for s in ANCHOR_DATA]}


def patch_sites(data: bytes, binary: str, only: set[str]) -> tuple[bytes, list[dict]]:
    result, changes = bytearray(data), []
    for site in ANCHOR_DATA:
        if site["binary"] != binary or site["name"] not in only:
            continue
        anchor = bytes.fromhex(site["anchor"])
        at = data.find(anchor) + 16
        before, after = bytes.fromhex(site["before"]), bytes.fromhex(site["after"])
        require(len(before) == len(after), "Patch must preserve instruction length")
        require(data[at:at + len(before)] == before, f"{site['name']}: source changed")
        result[at:at + len(after)] = after
        changes.append({"name": site["name"], "offset": at,
                        "before": before.hex(), "after": after.hex()})
    return bytes(result), changes


def patch_team(data: bytes, team: str) -> tuple[bytes, dict]:
    require(re.fullmatch(r"[A-Z0-9]{10}", team) is not None, "Expected a ten-character Team ID")
    anchor = bytes.fromhex(REFERENCE["service"]["team_anchor"])
    at = data.find(anchor) + 16
    before = b"4C6364ACXT"
    require(data[at:at + 10] == before, "Dispatcher Team ID changed")
    out = bytearray(data)
    out[at:at + 10] = team.encode("ascii")
    return bytes(out), {"name": "dispatcher-team", "offset": at,
                        "before": before.hex(), "after": team.encode().hex()}


def patch_peer(data: bytes, cdhash: str) -> tuple[bytes, list[dict]]:
    require(re.fullmatch(r"[0-9a-fA-F]{40}", cdhash) is not None,
            "Expected a 20-byte dispatcher CDHash")
    result, changes = patch_sites(data, "vm", {"peer-hook", "vm-config-gate", "vm-license-status"})
    template = bytearray.fromhex(PEER_CAVE["template"])
    old_hash = bytes.fromhex(PEER_CAVE["reference_cdhash"])
    require(template.count(old_hash) == 1, "Peer pin template digest ambiguous")
    at_hash = template.find(old_hash)
    template[at_hash:at_hash + 20] = bytes.fromhex(cdhash)
    cave_at = executable_offset(data, PEER_CAVE["va"], len(template))
    out = bytearray(result)
    out[cave_at:cave_at + len(template)] = template
    changes.append({"name": "peer-code-cave", "offset": cave_at,
                    "size": len(template), "dispatcher_cdhash": cdhash})
    return bytes(out), changes


def inject_library(data: bytes) -> tuple[bytes, dict]:
    _, _, _, _, count, size, _, _ = struct.unpack_from("<8I", data)
    end = 32 + size
    positions = [s["offset"] for s in sections(data) if s["offset"]]
    require(positions, "No file-backed Mach-O sections")
    first = min(positions)
    name = NET_LIBRARY.encode() + b"\0"
    command_size = (24 + len(name) + 7) & ~7
    require(end + command_size <= first and not any(data[end:end + command_size]),
            "Insufficient zero-filled load-command padding")
    out = bytearray(data)
    out[end:end + command_size] = (struct.pack("<6I", 0xC, command_size, 24, 0, 0, 0) + name).ljust(command_size, b"\0")
    struct.pack_into("<II", out, 16, count + 1, size + command_size)
    require(out[first:] == data[first:], "Library injection changed original sections")
    return bytes(out), {"name": "vmnet-library", "offset": end, "size": command_size,
                        "original_sections_preserved": True}


def write_binary(path: Path, data: bytes) -> None:
    mode = path.stat().st_mode & 0o777
    path.write_bytes(data)
    path.chmod(mode)


def embedded(name: str) -> bytes:
    entry = EMBEDDED_SOURCES[name]
    source = zlib.decompress(base64.b64decode(entry["zlib_base64"]))
    require(digest(source) == entry["sha256"], f"Embedded {name} checksum mismatch")
    return source


def sign(path: Path, identity: str, entitlements: Path | None = None,
         identifier: str | None = None) -> None:
    command = ["/usr/bin/codesign", "--force", "--sign", identity, "--timestamp=none", "--options", "0"]
    if identifier:
        command += ["--identifier", identifier]
    else:
        command += ["--preserve-metadata=identifier"]
    if entitlements:
        command += ["--entitlements", str(entitlements)]
    run(*command, path)


def signing_metadata(path: Path) -> dict[str, str]:
    output = run("/usr/bin/codesign", "-dv", "--verbose=4", path, capture=True)
    fields = {}
    for line in output.splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value
    return fields


def compile_network(output: Path, identity: str, team: str, uid: int) -> tuple[Path, Path]:
    sources = output / "build-sources"
    sources.mkdir()
    for name in ("broker.h", "helper.c", "shim.c"):
        data = embedded(name)
        if name == "helper.c":
            require(data.count(b"NT7B2P5VPY") == 1, "Unexpected helper Team ID template")
            data = data.replace(b"NT7B2P5VPY", team.encode())
        (sources / name).write_bytes(data)
    helper = output / HELPER_LABEL
    shim = output / "PoCVMNet.dylib"
    common = ["/usr/bin/clang", "-fblocks", "-O2", "-Wno-deprecated-declarations", "-I", str(sources)]
    run(*common, f"-DPOC_UID={uid}", sources / "helper.c", "-framework", "CoreFoundation",
        "-framework", "Security", "-framework", "vmnet", "-o", helper)
    run(*common, "-dynamiclib", sources / "shim.c", "-framework", "CoreFoundation",
        "-framework", "vmnet", "-o", shim)
    sign(helper, "-", identifier=HELPER_LABEL)
    sign(shim, identity, identifier="local.codex.vmnet.shim")
    return helper, shim


def plist_at(path: Path, payload: dict) -> None:
    path.write_bytes(plistlib.dumps(payload, sort_keys=True))


def build(source: Path, output: Path, identity: str, uid: int,
          test_unsigned_source: bool = False) -> dict:
    require(sys.platform == "darwin" and os.uname().machine == "arm64", "Requires ARM64 macOS")
    require(not output.exists(), "Output already exists")
    source = source.expanduser().resolve(strict=True)
    require(output.resolve() not in source.parents and source not in output.resolve().parents,
            "Output and source directories must be separate")
    blobs, inspection = source_check(source)
    if not test_unsigned_source:
        run("/usr/bin/codesign", "--verify", "--deep", "--strict", source)
    require(uid >= 500 and uid < 65535, "Expected a local non-root macOS account UID")
    output.mkdir(parents=True)
    app = output / APP_NAME
    try:
        run("/usr/bin/ditto", source, app)
        vm_ent = output / "vm-entitlements.plist"
        client_ent = output / "client-entitlements.plist"
        service_ent = output / "service-entitlements.plist"
        plist_at(vm_ent, VM_ENTITLEMENTS)
        plist_at(client_ent, CLIENT_ENTITLEMENTS)
        plist_at(service_ent, SERVICE_ENTITLEMENTS)

        # A signed shim is a safe way to read the local certificate's Team ID.
        marker = output / "team-probe"
        marker_source = output / "team-probe.c"
        marker_source.write_text("int main(void) { return 0; }\n")
        run("/usr/bin/clang", marker_source, "-o", marker)
        marker_source.unlink()
        sign(marker, identity, identifier="local.codex.parallels-poc.team-probe")
        team = signing_metadata(marker).get("TeamIdentifier", "")
        marker.unlink()
        require(re.fullmatch(r"[A-Z0-9]{10}", team) is not None,
                "Signing identity has no usable Team ID")
        helper, shim = compile_network(output, identity, team, uid)

        changes = {}
        client, changes["client"] = patch_sites(blobs["client"], "client", {
            "linked-clone-menu", "clipboard-choices", "clipboard-normalization",
            "new-vm-resource-clamp", "client-vm-boot-license"})
        service, changes["service"] = patch_sites(blobs["service"], "service", {
            "premium-matrix", "dispatcher-vm-boot-license"})
        service, team_change = patch_team(service, team)
        changes["service"].append(team_change)
        write_binary(app / PATHS["client"], client)
        write_binary(app / PATHS["service"], service)

        # The VM peer pin must match the final signed dispatcher CDHash.
        sign(app / SERVICE_APP, "-", service_ent)
        service_sign = signing_metadata(app / SERVICE_APP)
        cdhash = service_sign.get("CDHash", "")
        require(re.fullmatch(r"[0-9a-fA-F]{40}", cdhash) is not None,
                "Dispatcher signing did not yield a CDHash")
        vm, changes["vm"] = patch_peer(blobs["vm"], cdhash)
        vm, library_change = inject_library(vm)
        changes["vm"].append(library_change)
        write_binary(app / PATHS["vm"], vm)
        framework = app / VM_APP / "Contents/Frameworks"
        framework.mkdir(exist_ok=True)
        shutil.copy2(shim, framework / shim.name)
        sign(app / VM_APP, identity, vm_ent)
        sign(app, "-", client_ent)
        run("/usr/bin/codesign", "--verify", "--deep", "--strict", app)

        launchd = {
            "Label": HELPER_LABEL,
            "MachServices": {HELPER_LABEL: True},
            "ProcessType": "Interactive",
            "ProgramArguments": [f"/Library/PrivilegedHelperTools/{HELPER_LABEL}"],
            "StandardErrorPath": f"/var/log/{HELPER_LABEL}.log",
            "StandardOutPath": f"/var/log/{HELPER_LABEL}.log",
        }
        plist_at(output / f"{HELPER_LABEL}.plist", launchd)
        manifest = {"schema": 1, "tool_version": VERSION, "created_utc": datetime.now(timezone.utc).isoformat(),
                    "source": inspection, "team_id": team, "dispatcher_cdhash": cdhash,
                    "helper_uid": uid, "changes": changes,
                    "outputs": {n: digest((app / p).read_bytes()) for n, p in PATHS.items()},
                    "helper_sha256": digest(helper.read_bytes()),
                    "shim_sha256": digest((framework / shim.name).read_bytes()),
                    "launchd_plist_sha256": digest((output / f"{HELPER_LABEL}.plist").read_bytes()),
                    "app_signature": "codesign --verify --deep --strict passed",
                    "runtime_status": "Not established by build; use verify-installed and verify-guest."}
        (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
        return manifest
    except BaseException:
        shutil.rmtree(output, ignore_errors=True)
        raise


def verify_build(output: Path) -> dict:
    output = output.expanduser().resolve(strict=True)
    manifest = json.loads((output / "manifest.json").read_text())
    require(manifest.get("schema") == 1, "Unknown manifest schema")
    app = output / APP_NAME
    run("/usr/bin/codesign", "--verify", "--deep", "--strict", app)
    for name, relative in PATHS.items():
        require(digest((app / relative).read_bytes()) == manifest["outputs"][name],
                f"{name}: staged hash differs from manifest")
    helper = output / HELPER_LABEL
    require(digest(helper.read_bytes()) == manifest["helper_sha256"], "Helper hash differs")
    shim = app / VM_APP / "Contents/Frameworks/PoCVMNet.dylib"
    require(digest(shim.read_bytes()) == manifest["shim_sha256"], "Shim hash differs")
    plist = output / f"{HELPER_LABEL}.plist"
    require(digest(plist.read_bytes()) == manifest["launchd_plist_sha256"], "Launchd plist differs")
    return manifest


def install(output: Path, target: Path) -> None:
    manifest = verify_build(output)
    output = output.expanduser().resolve(strict=True)
    require(target == Path("/Applications/Parallels Desktop.app"),
            "Installer is limited to /Applications/Parallels Desktop.app")
    require(not subprocess.run(["/usr/bin/pgrep", "-x", "prl_vm_app"], capture_output=True).returncode == 0,
            "Shut down the VM before installation")
    require(not subprocess.run(["/usr/bin/pgrep", "-x", "prl_client_app"], capture_output=True).returncode == 0,
            "Quit Parallels before installation")
    temp = Path(tempfile.mkdtemp(prefix="codex-parallels-install-", dir="/private/tmp"))
    stage = temp / APP_NAME
    run("/usr/bin/ditto", output / APP_NAME, stage)
    helper = temp / HELPER_LABEL
    plist = temp / f"{HELPER_LABEL}.plist"
    old_helper = temp / "old-helper"
    old_plist = temp / "old-plist"
    shutil.copy2(output / HELPER_LABEL, helper)
    shutil.copy2(output / plist.name, plist)
    backup = Path(f"/Applications/Parallels Desktop.poc-backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}.app")
    checks = [f"test \"$(/usr/bin/shasum -a 256 {shlex.quote(str(stage / p))} | /usr/bin/awk '{{print $1}}')\" = {shlex.quote(manifest['outputs'][n])}"
              for n, p in PATHS.items()]
    checks.append(f"test \"$(/usr/bin/shasum -a 256 {shlex.quote(str(helper))} | /usr/bin/awk '{{print $1}}')\" = {shlex.quote(manifest['helper_sha256'])}")
    checks.append(f"test \"$(/usr/bin/shasum -a 256 {shlex.quote(str(plist))} | /usr/bin/awk '{{print $1}}')\" = {shlex.quote(manifest['launchd_plist_sha256'])}")
    shell = "\n".join([
        "#!/bin/sh", "set -eu", "test \"$(/usr/bin/id -u)\" = 0",
        "! /usr/bin/pgrep -x prl_vm_app >/dev/null", "! /usr/bin/pgrep -x prl_client_app >/dev/null",
        *checks,
        f"/usr/bin/codesign --verify --deep --strict {shlex.quote(str(stage))}",
        f"test ! -e {shlex.quote(str(backup))}",
        "installed=0",
        f"if test -f /Library/PrivilegedHelperTools/{HELPER_LABEL}; then /bin/cp -p /Library/PrivilegedHelperTools/{HELPER_LABEL} {shlex.quote(str(old_helper))}; fi",
        f"if test -f /Library/LaunchDaemons/{HELPER_LABEL}.plist; then /bin/cp -p /Library/LaunchDaemons/{HELPER_LABEL}.plist {shlex.quote(str(old_plist))}; fi",
        "restore_on_failure() {",
        "  if test \"$installed\" = 0; then",
        f"    /bin/launchctl bootout system/{HELPER_LABEL} >/dev/null 2>&1 || true",
        f"    if test -f {shlex.quote(str(old_helper))}; then /bin/cp -p {shlex.quote(str(old_helper))} /Library/PrivilegedHelperTools/{HELPER_LABEL}; else /bin/rm -f /Library/PrivilegedHelperTools/{HELPER_LABEL}; fi",
        f"    if test -f {shlex.quote(str(old_plist))}; then /bin/cp -p {shlex.quote(str(old_plist))} /Library/LaunchDaemons/{HELPER_LABEL}.plist; /bin/launchctl bootstrap system /Library/LaunchDaemons/{HELPER_LABEL}.plist || true; else /bin/rm -f /Library/LaunchDaemons/{HELPER_LABEL}.plist; fi",
        f"    if test -d {shlex.quote(str(backup))}; then",
        f"      /bin/rm -rf {shlex.quote(str(target))}",
        f"      /bin/mv {shlex.quote(str(backup))} {shlex.quote(str(target))}",
        f"      {shlex.quote(str(target / 'Contents/MacOS/inittool2'))} init -b {shlex.quote(str(target))} || true",
        "    fi",
        "  fi",
        "}",
        "trap restore_on_failure EXIT",
        f"if test -e {shlex.quote(str(target))}; then /bin/mv {shlex.quote(str(target))} {shlex.quote(str(backup))}; fi",
        f"/usr/bin/ditto {shlex.quote(str(stage))} {shlex.quote(str(target))}",
        f"{shlex.quote(str(target / 'Contents/MacOS/inittool2'))} init -b {shlex.quote(str(target))}",
        f"/usr/bin/install -d -o root -g wheel -m 755 /Library/PrivilegedHelperTools",
        f"/usr/bin/install -o root -g wheel -m 755 {shlex.quote(str(helper))} /Library/PrivilegedHelperTools/{HELPER_LABEL}",
        f"/usr/bin/install -o root -g wheel -m 644 {shlex.quote(str(plist))} /Library/LaunchDaemons/{HELPER_LABEL}.plist",
        f"/bin/launchctl bootout system/{HELPER_LABEL} >/dev/null 2>&1 || true",
        f"/bin/launchctl bootstrap system /Library/LaunchDaemons/{HELPER_LABEL}.plist",
        f"/usr/bin/codesign --verify --deep --strict {shlex.quote(str(target))}",
        "installed=1",
        f"/usr/bin/printf 'Installed. Backup: {backup}\\n'",
    ]) + "\n"
    root_script = temp / "install.sh"
    root_script.write_text(shell)
    root_script.chmod(0o700)
    try:
        if os.geteuid() == 0:
            run("/bin/sh", root_script)
        else:
            command = f"/bin/sh {shlex.quote(str(root_script))}"
            applescript = temp / "install.applescript"
            applescript.write_text("do shell script " + json.dumps(command) +
                                  ' with administrator privileges with prompt "Install the locally built Parallels research app and network helper."\n')
            run("/usr/bin/osascript", applescript)
    finally:
        shutil.rmtree(temp, ignore_errors=True)
    print(f"Installed at {target}; retained backup at {backup}")


def verify_installed(output: Path, target: Path) -> dict:
    manifest = verify_build(output)
    require(target.exists(), "Installed app absent")
    run("/usr/bin/codesign", "--verify", "--deep", "--strict", target)
    checks = {}
    for name, relative in PATHS.items():
        actual = digest((target / relative).read_bytes())
        checks[name] = actual == manifest["outputs"][name]
    helper = Path("/Library/PrivilegedHelperTools") / HELPER_LABEL
    checks["helper"] = helper.exists() and digest(helper.read_bytes()) == manifest["helper_sha256"]
    installed_plist = Path("/Library/LaunchDaemons") / f"{HELPER_LABEL}.plist"
    checks["launchd_plist"] = installed_plist.exists() and digest(installed_plist.read_bytes()) == manifest["launchd_plist_sha256"]
    checks["shim"] = digest((target / VM_APP / "Contents/Frameworks/PoCVMNet.dylib").read_bytes()) == manifest["shim_sha256"]
    checks["dispatcher_cdhash"] = signing_metadata(target / SERVICE_APP).get("CDHash") == manifest["dispatcher_cdhash"]
    checks["vm_team"] = signing_metadata(target / VM_APP).get("TeamIdentifier") == manifest["team_id"]
    checks["helper_root_owned"] = helper.stat().st_uid == 0
    require(all(checks.values()), f"Installed files differ: {checks}")
    return {"installed": True, "checks": checks, "runtime_network_verified": False}


def verify_guest(vm_name: str, start: bool = False) -> dict:
    """Use the installed SDK to run fixed DNS/HTTPS checks as the guest user."""
    H, U, R, S, I = C.c_void_p, C.c_uint32, C.c_int, C.c_char_p, C.c_int
    sdk = Path("/Applications/Parallels Desktop.app/Contents/Frameworks/") / (
        "ParallelsVirtualizationSDK.framework/Versions/11/libprl_sdk.11.dylib")
    require(sdk.is_file(), "Installed SDK 11 library not found")
    api = C.CDLL(str(sdk))
    pointer = C.POINTER(H)
    signatures = {
        "PrlApi_InitEx": (R, [U, I, U, U]), "PrlApi_Deinit": (R, []),
        "PrlHandle_Free": (R, [H]), "PrlSrv_Create": (R, [pointer]),
        "PrlLoginParams_Create": (R, [pointer]),
        "PrlLoginParams_SetFlags": (R, [H, U]),
        "PrlSrv_LoginLocalWithParams": (H, [H, H]),
        "PrlSrv_Logoff": (H, [H]), "PrlSrv_GetVmConfig": (H, [H, S, U]),
        "PrlVm_Start": (H, [H]),
        "PrlVm_TerminalConnect": (H, [H, U]),
        "PrlVm_TerminalDisconnect": (R, [H]),
        "PrlVm_LoginInGuest": (H, [H, S, S, U]),
        "PrlVmGuest_Logout": (H, [H, U]),
        "PrlApi_CreateStringsList": (R, [pointer]),
        "PrlStrList_AddItem": (R, [H, S]),
        "PrlVmGuest_RunProgram": (H, [H, S, H, H, U, I, I, I]),
        "PrlJob_Wait": (R, [H, U]),
        "PrlJob_GetRetCode": (R, [H, C.POINTER(R)]),
        "PrlJob_GetResult": (R, [H, pointer]),
        "PrlResult_GetParam": (R, [H, pointer]),
        "PrlJob_GetEvent": (R, [H, pointer]),
        "PrlEvent_GetParamByName": (R, [H, U, pointer]),
        "PrlEvtPrm_ToUint32": (R, [H, C.POINTER(U)]),
    }
    for name, (restype, args) in signatures.items():
        function = getattr(api, name)
        function.restype, function.argtypes = restype, args

    def check(code: int, op: str) -> None:
        require(code == 0, f"{op}: SDK error 0x{code & 0xffffffff:08x}")

    with ExitStack() as resources:
        check(api.PrlApi_InitEx(0xb0000, 0, 0, 0), "Initialize SDK")
        resources.callback(api.PrlApi_Deinit)

        def output(function, *args):
            handle = H()
            check(function(*args, C.byref(handle)), function.__name__)
            require(bool(handle.value), "SDK returned an invalid handle")
            resources.callback(api.PrlHandle_Free, handle.value)
            return handle.value

        def wait(job_handle, timeout=45000):
            require(bool(job_handle), "SDK returned an invalid job")
            check(api.PrlJob_Wait(job_handle, timeout), "Wait for SDK job")
            code = R()
            check(api.PrlJob_GetRetCode(job_handle, C.byref(code)), "Read SDK job status")
            check(code.value, "SDK job")

        def job(function, *args, timeout=45000):
            handle = function(*args)
            resources.callback(api.PrlHandle_Free, handle)
            wait(handle, timeout)
            return handle

        def result(function, *args):
            handle = job(function, *args)
            return output(api.PrlResult_GetParam, output(api.PrlJob_GetResult, handle))

        def cleanup(function, *args):
            handle = function(*args)
            if handle:
                try:
                    wait(handle, 5000)
                finally:
                    api.PrlHandle_Free(handle)

        server = output(api.PrlSrv_Create)
        login = output(api.PrlLoginParams_Create)
        check(api.PrlLoginParams_SetFlags(login, 4), "Set local login flags")
        job(api.PrlSrv_LoginLocalWithParams, server, login)
        resources.callback(cleanup, api.PrlSrv_Logoff, server)
        vm = result(api.PrlSrv_GetVmConfig, server, vm_name.encode(), 0x1800)
        if start:
            job(api.PrlVm_Start, vm, timeout=180000)
        job(api.PrlVm_TerminalConnect, vm, 0)
        resources.callback(api.PrlVm_TerminalDisconnect, vm)
        guest = None
        for attempt in range(24 if start else 1):
            try:
                guest = result(api.PrlVm_LoginInGuest, vm,
                               b"4a5533a7-31c6-4d7a-a400-1f330dc57a9d", None, 0)
                break
            except Refused:
                if attempt == 23 or not start:
                    raise
                time.sleep(5)
        resources.callback(cleanup, api.PrlVmGuest_Logout, guest, 0)
        commands = [
            ("dns", r"C:\Windows\System32\nslookup.exe", ["example.com"]),
            ("https_example", r"C:\Windows\System32\curl.exe",
             ["-4", "-f", "-sS", "--max-time", "20", "--write-out",
              r"\nHTTP_CODE=%{http_code};TLS_VERIFY=%{ssl_verify_result}\n", "https://example.com/"]),
            ("https_apple", r"C:\Windows\System32\curl.exe",
             ["-4", "-f", "-sS", "--max-time", "20", "--write-out",
              r"\nHTTP_CODE=%{http_code};TLS_VERIFY=%{ssl_verify_result}\n",
              "https://www.apple.com/library/test/success.html"]),
        ]
        results = []
        for label, command, arguments in commands:
            args = output(api.PrlApi_CreateStringsList)
            env = output(api.PrlApi_CreateStringsList)
            for value in arguments:
                check(api.PrlStrList_AddItem(args, value.encode()), "Add guest argument")
            print(f"CHECK_BEGIN: {label}", flush=True)
            completed = job(api.PrlVmGuest_RunProgram, guest, command.encode(), args, env,
                            0x2b800, 0, 1, 2)
            event = output(api.PrlJob_GetEvent, completed)
            parameter = output(api.PrlEvent_GetParamByName, event, 0x13e)
            exit_code = U()
            check(api.PrlEvtPrm_ToUint32(parameter, C.byref(exit_code)), "Read guest exit code")
            print(f"CHECK_END: {label}; EXIT={exit_code.value}", flush=True)
            results.append({"check": label, "guest_exit": exit_code.value})
        require(all(item["guest_exit"] == 0 for item in results), "Guest network check failed")
        return {"vm": vm_name, "checks": results, "network_verified": True}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    inspect = commands.add_parser("inspect", help="Read-only source and anchor validation")
    inspect.add_argument("--source-app", type=Path, required=True)
    prepare = commands.add_parser("build", help="Build and sign a separate test bundle")
    prepare.add_argument("--source-app", type=Path, required=True)
    prepare.add_argument("--output", type=Path, required=True)
    prepare.add_argument("--identity", required=True, help="Local Apple Development signing identity hash")
    prepare.add_argument("--uid", type=int, default=os.getuid())
    prepare.add_argument("--test-unsigned-source", action="store_true", help=argparse.SUPPRESS)
    all_in_one = commands.add_parser("all", help="Build, install, and verify in one run")
    all_in_one.add_argument("--source-app", type=Path, required=True)
    all_in_one.add_argument("--output", type=Path, required=True)
    all_in_one.add_argument("--identity", required=True)
    all_in_one.add_argument("--uid", type=int, default=os.getuid())
    all_in_one.add_argument("--vm-name", help="Existing registered Windows VM to start and check")
    for name in ("verify-build", "install", "verify-installed"):
        p = commands.add_parser(name)
        p.add_argument("--output", type=Path, required=True)
    guest = commands.add_parser("verify-guest", help="Run guest DNS and HTTPS checks through the SDK")
    guest.add_argument("--vm-name", required=True)
    guest.add_argument("--start", action="store_true", help="Start the stopped VM before checking it")
    args = parser.parse_args(argv)
    try:
        if args.command == "inspect":
            _, result = source_check(args.source_app)
        elif args.command == "build":
            result = build(args.source_app, args.output, args.identity, args.uid,
                           args.test_unsigned_source)
        elif args.command == "all":
            build(args.source_app, args.output, args.identity, args.uid)
            install(args.output, Path("/Applications/Parallels Desktop.app"))
            result = verify_installed(args.output, Path("/Applications/Parallels Desktop.app"))
            if args.vm_name:
                result["guest"] = verify_guest(args.vm_name, start=True)
        elif args.command == "verify-build":
            result = verify_build(args.output)
        elif args.command == "install":
            install(args.output, Path("/Applications/Parallels Desktop.app"))
            result = verify_installed(args.output, Path("/Applications/Parallels Desktop.app"))
        elif args.command == "verify-guest":
            result = verify_guest(args.vm_name, args.start)
        else:
            result = verify_installed(args.output, Path("/Applications/Parallels Desktop.app"))
        print(json.dumps(result, indent=2))
        return 0
    except (Refused, OSError, subprocess.CalledProcessError, ValueError, KeyError) as error:
        parser.exit(2, f"Refused: {error}\n")


if __name__ == "__main__":
    raise SystemExit(main())
