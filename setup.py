from setuptools import setup, find_packages


#reading in requirement files.
with open('requirements.txt') as f:
    reqs = f.readlines()

# setup the project. this will install all the
# requirements in requirements.txt file.
setup(
    name='proj_name',
    version=0.1,
    description='',
    author='Massoud Hosseinali',
    install_requires=reqs,
    packages=find_packages(),
    python_requires='>3.5'
)
