# -*- mode: python -*-
# -*- coding: utf-8 -*-

import os
import site

# Constants
DEBUG = os.environ.get("CEFPYTHON_PYINSTALLER_DEBUG", False)

# Set this secret cipher (optional for encryption)
cipher_obj = None

# Get the Python lib path dynamically for macOS
py_lib_path = site.getsitepackages()[0]  # Uses macOS Python site-packages
print(py_lib_path)

a = Analysis(
    ["ramanbiolibui/app.py"],
    hookspath=["ramanbiolibui/hooks"],  # To find "hook-cefpython3.py"
    cipher=cipher_obj,
    datas=[
        ("ramanbiolibui/templates/index.html", "ramanbiolibui/templates/"),
        ("ramanbiolibui/templates/results.html", "ramanbiolibui/templates/"),
        ("ramanbiolibui/templates/search.html", "ramanbiolibui/templates/"),
        ("ramanbiolibui/static/scripts.js", "ramanbiolibui/static/"),
        ("ramanbiolibui/static/jquery.min.js.js", "ramanbiolibui/static/"),
        ("ramanbiolibui/static/styles.css", "ramanbiolibui/static/"),
        ("ramanbiolibui/img/logo.png", "ramanbiolibui/img/"),
        ("ramanbiolibui/img/icfo.png", "ramanbiolibui/img/"),
        ("ramanbiolibui/img/uoc.png", "ramanbiolibui/img/"),
        (py_lib_path + "/ramanbiolib/db/raman_spectra_db.csv", "ramanbiolib/db"),
        (py_lib_path + "/ramanbiolib/db/raman_peaks_db.csv", "ramanbiolib/db"),
        (py_lib_path + "/ramanbiolib/db/metadata_db.csv", "ramanbiolib/db"),
        #(py_lib_path + "/cefpython3/icudtl.dat", "cefpython3"),
        #(py_lib_path + "/cefpython3/natives_blob.bin", "cefpython3"),
    ],
)

if not os.environ.get("PYINSTALLER_CEFPYTHON3_HOOK_SUCCEEDED", None):
    raise SystemExit("Error: Pyinstaller hook-cefpython3.py script was not executed or it failed")

pyz = PYZ(a.pure, a.zipped_data, cipher=cipher_obj)

# Use BUNDLE for macOS to create a .app file

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ramanbiolib-ui',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

app = BUNDLE(exe,
    name='ramanbiolib-ui.app',
    icon=None,
    bundle_identifier=None)