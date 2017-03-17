#!/usr/bin/env python
from setuptools import setup, find_packages
import versioneer

setup(
    name='dsphpipe',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='Matthew Wood',
    author_email='mdwood@slac.stanford.edu',
    description='Pipeline Scripts for LAT Dwarf Analysis',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/fermi-lat/dsphpipe",
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Development Status :: 4 - Beta',
    ],
    scripts=[],
    entry_points={'console_scripts': [
        'dsphpipe-quicklook = dsphpipe.scripts.quick_analysis:main'
    ]},
    install_requires=[
        'numpy >= 1.6.1',
        'astropy >= 1.2.1',
        'matplotlib >= 1.5.0',
        'scipy >= 0.14',
        'fermipy >= 0.12.5',
        'pyyaml',
        'healpy',
        'wcsaxes',
    ],
    extras_require=dict(
        all=[],
    ),
)
