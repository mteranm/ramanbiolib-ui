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
from PyInstaller.utils.hooks import collect_data_files

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
py_lib_path =  "c:\\hostedtoolcache\\windows\\python\\3.7.9\\x64\\lib\\site-packages"  # "C:\\Users\\Merli\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages"
print(py_lib_path)

specpath = os.path.dirname(os.path.abspath(SPEC)) 
icon = os.path.join(specpath, 'icon.ico')
print(icon)

cipher_obj = None

a = Analysis(
    ["ramanbiolibui/app.py"],
    hookspath=["ramanbiolibui/hooks"],  # To find "hook-cefpython3.py"
    cipher=cipher_obj,
    win_private_assemblies=True,
    win_no_prefer_redirects=True,
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
        (py_lib_path + "/cefpython3/icudtl.dat", "cefpython3"),
        (py_lib_path + "/cefpython3/natives_blob.bin", "cefpython3"),
        *collect_data_files('cefpython3'),
        ('icon.ico', '.'),
    ],
)

if not os.environ.get("PYINSTALLER_CEFPYTHON3_HOOK_SUCCEEDED", None):
    raise SystemExit("Error: Pyinstaller hook-cefpython3.py script was "
                     "not executed or it failed")

pyz = PYZ(a.pure,
          a.zipped_data,
          cipher=cipher_obj)

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
    icon=icon
)