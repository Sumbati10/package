from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example Python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='',
    author='Lindah Sumbati',
    author_email='sumbatilinda@gmail.com'
)
