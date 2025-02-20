# -*- mode: python ; coding: utf-8 -*-

import os
import glob
from PyInstaller.utils.hooks import collect_dynamic_libs, collect_data_files
import cefpython3

CEF_PATH = os.path.dirname(cefpython3.__file__)
print(os.path.dirname(cefpython3.__file__))

block_cipher = None

print(f"cef libs: {collect_dynamic_libs('cefpython3')}")
print(f"cef data: {collect_data_files('cefpython3')}")
print(f"cef data after: {[ (v[0], v[1].replace('cefpython', '.\')) for v in collect_data_files('cefpython3')]}")


a = Analysis(
    ['src/app.py'],
    pathex=['.'],
    binaries=[
        *collect_dynamic_libs('cefpython3'),
        ("C:/Windows/System32/MSVCR100.dll", "."),
        # Manually add CEF data files like .pak files
    ],  # Collect CEF shared libraries
    datas=[
        *[ (v[0], v[1].replace("cefpython", ".\")) for v in collect_data_files('cefpython3')],
        ("src/templates/index.html", "src/templates/"),
        ("src/templates/results.html", "src/templates/"),
        ("src/templates/search.html", "src/templates/"),
        ("src/static/scripts.js", "src/static/"),
        ("src/static/jquery.min.js.js", "src/static/"),
        ("src/static/styles.css", "src/static/"),
    ],
    hiddenimports=["cefpython3"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['widevinecdm.dll'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

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
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    onedir=True,
    onefile=False
)
