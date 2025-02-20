# -*- mode: python ; coding: utf-8 -*-

from glob import glob
from PyInstaller.utils.hooks import collect_dynamic_libs, collect_data_files

DEBUG = True
block_cipher = None

a = Analysis(
    ["src/app.py"],
    pathex=['.'],
    hookspath=["."],  # To find "hook-cefpython3.py"
    binaries=[
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

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name="ramanbiolib-ui",
          debug=DEBUG,
          strip=False,
          upx=False,
          console=DEBUG,
        )

COLLECT(exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=False,
        name="ramanbiolib-ui")