# VS Code Extensions Offline — Python (Windows x64)

For VS Code **1.145.2** (2026-11-06). Downloaded from the official Visual Studio Marketplace on 2026-11-12 and verified: each file's `package.json` `engines.vscode` was checked against 1.145.2, zip integrity tested, SHA256 recorded in `SHA256SUMS.txt`.

## Files

| File | Extension | Version | engines.vscode | Size |
|---|---|---|---|---|
| ms-python.python-2026.11.2026110601-win32-x64.vsix | ms-python.python | 2026.11.2026110601 | ^1.95.0 | 9,486,825 |
| ms-python.vscode-pylance-2026.4.101.vsix | ms-python.vscode-pylance | 2026.4.101 | ^1.107.0 | 33,537,462 |
| ms-python.debugpy-2026.7.13141016-win32-x64.vsix | ms-python.debugpy | 2026.7.13141016 | ^1.92.0 | 7,515,981 |
| ms-python.vscode-python-envs-1.43.2026111101-win32-x64.vsix | ms-python.vscode-python-envs | 1.43.2026111101 | ^1.110.0-20260204 | 4,484,206 |

Platform: **win32-x64** (Pylance is universal). The Python extension is an extension pack of the other three — all four are needed for offline install.

## Get the .vsix files

`.vsix` are binary and exceed GitHub's per-file / push limits, so in this repo they are stored base64-encoded and split into 2 MB chunks under `parts/`. To rebuild the originals (verified against `SHA256SUMS.txt`):

```bat
python join_vsix.py
```

This writes the 4 `.vsix` files into `vsix\`. Tested: all 4 rebuild byte-identical (SHA256 OK).

## Install (offline)

After rebuilding, run:

```bat
code --install-extension vsix\ms-python.vscode-pylance-2026.4.101.vsix
code --install-extension vsix\ms-python.python-2026.11.2026110601-win32-x64.vsix
code --install-extension vsix\ms-python.debugpy-2026.7.13141016-win32-x64.vsix
code --install-extension vsix\ms-python.vscode-python-envs-1.43.2026111101-win32-x64.vsix
```

Or in VS Code: Extensions panel → `...` → Install from VSIX, pick each file in `vsix\`.
