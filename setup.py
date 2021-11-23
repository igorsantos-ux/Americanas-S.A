import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["PySimpleGUI"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Wave 4.0",
    version="1.4",
    description="Gerador e pedidos com data limite",
    options={"build_exe": build_exe_options},
    executables=[Executable("wave 4_0.py", base=base)]
)
