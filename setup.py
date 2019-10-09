import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "gensim", "mglearn", "pdfminer", "docx",
                                  "scipy", "wordcloud", "urllib3", "numpy", "matplotlib",
                                  "nltk", "pandas", "sklearn", "pip"], 'include_files':['tcl86t.dll','tk86t.dll']}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Outline",
        version = "0.1",
        description = "Summarizes docs",
        options = {"build_exe": build_exe_options},
        executables = [Executable("outline.py", base=base)])