from setuptools import setup, find_packages

with open("requirements.txt", "r") as fr:
    REQUIRES = fr.read()


setup(name="tesqt",
version='0.1',
scripts=['testqt.py'],
include_package_data=True,
python_requires='>=3.7',
install_requires=REQUIRES,
entry_points={
   'console_scripts':[
       'testqtqt=testqt:window']}
)
