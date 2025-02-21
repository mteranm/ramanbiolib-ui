# -*- mode: python ; coding: utf-8 -*-

import site
from PyInstaller.utils.hooks import collect_dynamic_libs, collect_data_files

lib_path = site.getsitepackages()[0]  # First entry is usually the main 'lib' folder
print(lib_path)

specpath = os.path.dirname(os.path.abspath(SPEC)) 
icon = os.path.join(specpath, 'icon.png')
print(icon)

DEBUG = True
block_cipher = None

a = Analysis(
    ["src/app.py"],
    pathex=['.'],
    hookspath=["src/hooks"],  # To find "hook-cefpython3.py"
    binaries=[
        ('/usr/lib/x86_64-linux-gnu/libnss3.so', '.'),
        ('/usr/lib/x86_64-linux-gnu/nss/libsoftokn3.so', '.'),
        ('/usr/lib/x86_64-linux-gnu/nss/libnssckbi.so', '.'),
        *collect_dynamic_libs('cefpython3')
    ],
    datas=[
        ("src/templates/index.html", "src/templates/"),
        ("src/templates/results.html", "src/templates/"),
        ("src/templates/search.html", "src/templates/"),
        ("src/static/scripts.js", "src/static/"),
        ("src/static/jquery.min.js.js", "src/static/"),
        ("src/static/styles.css", "src/static/"),
        ("src/img/logo.png", "src/img/"),
        ("src/img/icfo.png", "src/img/"),
        ("src/img/uoc.png", "src/img/"),
        (lib_path + "/ramanbiolib/db/raman_spectra_db.csv", "ramanbiolib/db"),
        (lib_path + "/ramanbiolib/db/raman_peaks_db.csv", "ramanbiolib/db"),
        *collect_data_files('cefpython3')
    ],
    hiddenimports=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure,
          a.zipped_data,
          cipher=block_cipher)

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