# TestPackage

This is a test package for UFOManager.

You need to install the requirements for corresponding python version.

You need to install the [UFOManger Package](https://github.com/ThanosWang/TestPackage/blob/main/UFOManager/UFOManager-1.0.tar.gz)

You can use
'''bash
from UFOManger import Upload, Download
Upload(command,modelpath)

Download(command.Github_Access_Token)
'''
in your python script,

or use
'''bash
python -m UFOManager.Upload 'Command'

Python -m UFOManager.Download 'Command'
'''
in command line.

For Upload, 'Command' includes 'Validation check', 'Generate metadata', 'Upload model', 'Update new version', 'Upload metadata to GitHub'.

For Download, 'Command' includes 'Search for model', 'Download model', 'Search and Download'.

Upload is workable in Python 2 and 3, while Download only works in Python 3.
