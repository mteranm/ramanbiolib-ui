# -*- mode: python ; coding: utf-8 -*-

import os
from glob import glob
from PyInstaller.utils.hooks import collect_dynamic_libs, collect_data_files

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

a = Analysis(
    ['src/app.py'],
    pathex=['.'],
    binaries=[
    ],  # Collect CEF shared libraries
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
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
    debug=False,
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
)
