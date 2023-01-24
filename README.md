# TestPackage

This is a test python package for [UFOManager](https://github.com/Neubauer-Group/UFOManager).

The aim is to transfer UFOManager repo into a python package suitable for both Python 2 and 3.

You need to install the [requirements_Python2.txt](https://github.com/ThanosWang/TestPackage/blob/main/requirements_Python2.txt) or [requirements_Python3.txt](https://github.com/ThanosWang/TestPackage/blob/main/requirements_Python3.txt) for corresponding Python version.

After download, use
```bash
$pip install UFOManager-1.0.tar.gz
```
to install this package.

You can use
```bash
from UFOManger import Upload, Download
Upload(command,modelpath)

Download(command.Github_Access_Token)
```
in your python script,

or use
```bash
python -m UFOManager.Upload 'Command'

Python -m UFOManager.Download 'Command'
```
in command line.

For Upload, 'Command' includes 'Validation check', 'Generate metadata', 'Upload model', 'Update new version', 'Upload metadata to GitHub'.

For Download, 'Command' includes 'Search for model', 'Download model', 'Search and Download'.

Upload is workable in Python 2 and 3, while Download only works in Python 3.

# Changes:
The Validation check part and Generate metadata part is improved.

For Validation check, Upload will do a series checks on particles defined in UFO models:
1. Check if particle is ghost. (We ignore particle if has a non-zero GhostNumber)
2. Check if particle is registered by [Particle Data Group](https://pdg.lbl.gov/). (Check if pdg_code is valid.)
3. Compare particle's spin and three_charge (three times charge) value with that registered by [Particle Data Group](https://pdg.lbl.gov/). If the two values of a particle are not the same, we assume the particle's id is pdg-like.
4. Check if particle is lepton, quark, or boson
5. Check if particle is Standard Model particle

For Generate metadata, Upload will generate new information for particles inside the model:
1. All Particles: All particles defined in the model and corresponding IDs 
2. Standard Model elementary particles: Standard Model elementary particles defined in the model and corresponding PDGIDs
3. Beyond the Standard Model elementary particles with Standard PDGIDs: Beyond the Standard Model elementary particles defined in the model and valid corresponding PGDIDs (new particles who have registered PDGIDs)
4. Particles with PDG-like IDs: Particles defined in the model, which are not registered by [Particle Data Group](https://pdg.lbl.gov/)， with their IDs, spin, and charge

And for all information about particles, ghost is not included
