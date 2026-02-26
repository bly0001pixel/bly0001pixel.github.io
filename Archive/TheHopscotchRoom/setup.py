import sys
from cx_Freeze import setup, Executable

build_options = {
    'packages': ['pygame', 'random', 'os'],
    'include_files': [
        ('assets/', 'assets/')
    ]
}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='The.Hopscotch.Room.v1.0.0',
    version='1.0.0',
    description='By Jonathan Blyth',
    options={'build_exe': build_options},
    executables=[Executable('main.py', base=base, icon='AkarnaeLogo.ico')]
)