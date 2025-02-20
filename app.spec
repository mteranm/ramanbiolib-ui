# -*- mode: python -*-
# -*- coding: utf-8 -*-

"""
This is a PyInstaller spec file.
"""

import os
import site
from PyInstaller.building.api import PYZ, EXE, COLLECT
from PyInstaller.building.build_main import Analysis
from PyInstaller.utils.hooks import is_module_satisfies
from PyInstaller.archive.pyz_crypto import PyiBlockCipher

# Constants
DEBUG = os.environ.get("CEFPYTHON_PYINSTALLER_DEBUG", False)
PYCRYPTO_MIN_VERSION = "2.6.1"

# Set this secret cipher to some secret value. It will be used
# to encrypt archive package containing your app's bytecode
# compiled Python modules, to make it harder to extract these
# files and decompile them. If using secret cipher then you
# must install pycrypto package by typing: "pip install pycrypto".
# Note that this will only encrypt archive package containing
# imported modules, it won't encrypt the main script file
# (wxpython.py). The names of all imported Python modules can be
# still accessed, only their contents are encrypted.

# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

py_lib_path = "c:\\hostedtoolcache\\windows\\python\\3.7.9\\x64\\lib\\site-packages"  # First entry is usually the main 'lib' folder
print(py_lib_path)

cipher_obj = None

a = Analysis(
    ["src/app.py"],
    hookspath=["."],  # To find "hook-cefpython3.py"
    cipher=cipher_obj,
    win_private_assemblies=True,
    win_no_prefer_redirects=True,
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
        (py_lib_path + "/ramanbiolib/db/raman_spectra_db.csv", "ramanbiolib/db"),
        (py_lib_path + "/ramanbiolib/db/raman_peaks_db.csv", "ramanbiolib/db"),
        (py_lib_path + "/cefpython3/icudtl.dat", "cefpython3"),
        (py_lib_path + "/cefpython3/natives_blob.bin", "cefpython3"),
        ('icon.ico', '.')
    ],
)

if not os.environ.get("PYINSTALLER_CEFPYTHON3_HOOK_SUCCEEDED", None):
    raise SystemExit("Error: Pyinstaller hook-cefpython3.py script was "
                     "not executed or it failed")

pyz = PYZ(a.pure,
          a.zipped_data,
          cipher=cipher_obj)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name="ramanbiolib-ui",
          debug=True,
          strip=False,
          upx=False,
          console=True,
        )

COLLECT(exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=False,
        name="ramanbiolib-ui")