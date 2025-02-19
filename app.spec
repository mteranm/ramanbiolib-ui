# -*- mode: python ; coding: utf-8 -*-

from glob import glob
from PyInstaller.utils.hooks import collect_dynamic_libs, collect_data_files

block_cipher = None

a = Analysis(
    ['src/app.py'],
    pathex=['.'],
    binaries=[
        ('/usr/lib/x86_64-linux-gnu/libnss3.so', '.'),
        ('/usr/lib/x86_64-linux-gnu/nss/libsoftokn3.so', '.'),
        ('/usr/lib/x86_64-linux-gnu/nss/libnssckbi.so', '.'),
        ('/usr/lib/x86_64-linux-gnu/libpython3.7m.so.1.0', '.')
    ],  # Collect CEF shared libraries
    datas=[
        ("src/static/*", "src/static"), 
        ("src/img/*", "src/img"), 
        ("src/templates/*", "src/templates"), 
        *collect_data_files('cefpython3')
    ],
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
