import cx_Freeze


executables = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup (
    name = 'PesquisaCosmos',
    options = {'build_exe': {'packages': ['pygame', 'PySimpleGUI', 'emoji'],
                             'include_files': ['icon.ico', 'song.mp3']}},
    executables = executables
)
