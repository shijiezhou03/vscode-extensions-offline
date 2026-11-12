#!/usr/bin/env python3
"""Rebuild the original .vsix files from parts/*.b64.* chunks.

Usage: python join_vsix.py
Writes the 4 .vsix files into ./vsix/ and verifies SHA256 against SHA256SUMS.txt.
"""
import base64, glob, hashlib, os, sys

root = os.path.dirname(os.path.abspath(__file__))
outdir = os.path.join(root, "vsix")
os.makedirs(outdir, exist_ok=True)

expected = {}
with open(os.path.join(root, "SHA256SUMS.txt")) as f:
    for line in f:
        line = line.strip()
        if line:
            sha, fn = line.split(None, 1)
            expected[fn.strip()] = sha

names = sorted({os.path.basename(p).rsplit(".b64.", 1)[0] for p in glob.glob(os.path.join(root, "parts", "*.b64.*"))})
if not names:
    sys.exit("No parts found - run this script from the repo root after downloading the whole repo.")

ok = True
for fn in names:
    chunks = sorted(glob.glob(os.path.join(root, "parts", fn + ".b64.*")))
    b64 = "".join(open(c).read() for c in chunks)
    data = base64.b64decode(b64)
    sha = hashlib.sha256(data).hexdigest()
    status = "OK" if expected.get(fn) == sha else "SHA256 MISMATCH"
    if status != "OK":
        ok = False
    open(os.path.join(outdir, fn), "wb").write(data)
    print(f"{fn}  {len(data)} bytes  {status}")

print("\nDone. Install with, e.g.:")
print("  code --install-extension vsix\\ms-python.python-2026.11.2026110601-win32-x64.vsix")
sys.exit(0 if ok else 1)
