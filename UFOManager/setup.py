import setuptools

setuptools.setup(
    name="UFOManager",
    version="1.0",
    author="Mark Neubauer, Avik Roy, Zijun Wang",
    author_email='msn@illinois.edu, avroy@illinois.edu, zijun4@illinois.edu',
    description='This is the python package for uploading and downloading UFO models',
    py_modules=['__init__','uploadv3','Download'],
    packages=setuptools.find_packages()
)
