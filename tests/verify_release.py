#!/usr/bin/env python3
"""Public-release invariant gate for Grave-Machine v1.1.0."""

from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = "0e1cfd0097cf261f169c0e52a88d39f1541f04f07d179b1f009ff2cc311eb385"
errors = []

def fail(message):
    errors.append(message)
    print(f"FAIL: {message}")

def ok(message):
    print(f"ok: {message}")

required = [
    "index.html", "README.md", "CITATION.cff", "RIGHTS.md", "NOTICE.md",
    "CHANGELOG.md", "RELEASE_NOTES.md", "SHA256SUMS", "CLAUDE.md",
    "tests/verify_release.py", ".github/workflows/verify.yml",
]
for rel in required:
    if (ROOT / rel).is_file():
        ok(f"required file {rel}")
    else:
        fail(f"missing required file {rel}")

artifact = ROOT / "index.html"
if artifact.is_file():
    actual = hashlib.sha256(artifact.read_bytes()).hexdigest()
    if actual == EXPECTED:
        ok("runtime checksum")
    else:
        fail(f"runtime checksum {actual} != {EXPECTED}")

    text = artifact.read_text(encoding="utf-8")
    for fragment in [
        "Grave-Machine / گور-ماشین",
        '"defaultLanguage": "en"',
        '"author": "Mozare"',
        "کاری از مضارع",
        "یک ریمیکس ایرانی از",
        "https://collection.eliterature.org/3/works/taroko-gorge/taroko-gorge.html",
        'font-family:"Estedad"',
    ]:
        if fragment in text:
            ok(f"runtime fragment {fragment[:42]}")
        else:
            fail(f"missing runtime fragment: {fragment}")

for rel, expected in [
    ("README.md", "https://theblackbirdfield.com/works/grave-machine/run/"),
    ("CITATION.cff", 'version: "1.1.0"'),
    ("CITATION.cff", 'repository-code: "https://github.com/mozareeduge/grave-machine"'),
    ("SHA256SUMS", EXPECTED + "  index.html"),
]:
    path = ROOT / rel
    if path.is_file() and expected in path.read_text(encoding="utf-8"):
        ok(f"{rel}: {expected[:48]}")
    else:
        fail(f"{rel} missing expected text: {expected}")

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    lower = path.name.lower()
    if path.suffix.lower() in {".xlsx", ".zip"} or path.name.endswith(".taroke.json") or "diagnostic" in lower:
        fail(f"forbidden private file: {path.relative_to(ROOT)}")

if errors:
    print(f"\nRESULT: FAIL ({len(errors)})")
    sys.exit(1)

print("\nRESULT: PASS")
