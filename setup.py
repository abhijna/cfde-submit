import os
from setuptools import find_packages, setup

# Single source of truth for version
version_ns = {}
with open(os.path.join("cfde_submit", "version.py")) as f:
    exec(f.read(), version_ns)
version = version_ns['__version__']

with open('README.rst') as f:
    long_description = f.read()

setup(
    name="cfde-submit",
    description="A command line tool for submitting CFDE Datasets",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/nih-cfde/deriva-flow-client',
    version=version,
    packages=find_packages(),
    entry_points='''
    [console_scripts]
    cfde-submit=cfde_submit.main:cli
    ''',
    install_requires=[
        "bdbag>=1.6.0",
        "Click>=7.0",
        "datapackage>=1.10.0",
        "fair-research-login>=0.2.0",
        "GitPython>=3.0.4",
        "globus-automate-client>=0.10.5",
        "globus-sdk>=1.8.0,<2.0",
        "packaging>=20.1",
        "requests>=2.22.0"
    ],
    python_requires=">=3.6",
    license = 'Apache 2.0',
    maintainer='CFDE',
    maintainer_email='',
    classifiers = [
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
