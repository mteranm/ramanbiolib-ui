# -*- mode: python ; coding: utf-8 -*-

import os
import glob
from PyInstaller.utils.hooks import collect_dynamic_libs, collect_data_files
import cefpython3

CEF_PATH = os.path.dirname(cefpython3.__file__)
print(os.path.dirname(cefpython3.__file__))

block_cipher = None

# Collect files dynamically
static_files = glob.glob(os.path.join('src', 'static', '*'))
img_files = glob.glob(os.path.join('src', 'img', '*'))
template_files = glob.glob(os.path.join('src', 'templates', '*'))

# Create the datas list
datas = [
    (file, 'static') for file in static_files
] + [
    (file, 'img') for file in img_files
] + [
    (file, 'templates') for file in template_files
]

print(collect_dynamic_libs('cefpython3'),)

print(collect_data_files('cefpython3'),)

a = Analysis(
    ['src/app.py'],
    pathex=['.'],
    binaries=[
        *collect_dynamic_libs('cefpython3'),
        ("C:/Windows/System32/MSVCR100.dll", "."),
        # Manually add CEF data files like .pak files
    ],  # Collect CEF shared libraries
    datas=[
        *collect_data_files('cefpython3'),
        ("src/templates/index.html", "src/templates/"),
        (f"{CEF_PATH}/cef.pak", "."),  
        (f"{CEF_PATH}/devtools_resources.pak", "."),  
        (f"{CEF_PATH}/locales", "locales"),  # If locales are missing
    ],
    hiddenimports=[],
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
    onedir=True
)
