from cx_Freeze import setup, Executable
import sys
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

buildOptions = dict(packages=["heapq","webbrowser","tkinter", "folium", "jinja2","math","datetime","sys", "os"])

options = {
    'build_exe': {
        'include_files': [
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
            # 'C:\\Users\\natha\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\branca\\_cnames.json',
            # 'C:\\Users\\natha\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\branca\\_schemes.json'
        ],
    },
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

# 3
setup(
    name='Erica Road Shuttle',
    version="0.1",
    description="MyProgram that I created",
    options={"build_exe": buildOptions},
    executables= [Executable("main.py", base=base)])
