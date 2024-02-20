"""
The build/compilations setup
>> pip install -r requirements.txt
>> python setup.py install
"""
import pip
import logging
import pkg_resources

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def _parse_requirements(file_path):
    pip_ver = pkg_resources.get_distribution('pip').version
    pip_version = list(map(int, pip_ver.split('.')[:2]))
    if pip_version >= [6, 0]:
        raw = pip.req.parse_requirements(file_path,
                                         session=pip.download.PipSession())
    else:
        raw = pip.req.parse_requirements(file_path)
    return [str(i.req) for i in raw]


# parse_requirements() returns generator of pip.req.InstallRequirement objects
try:
    install_reqs = _parse_requirements("requirements.txt")
except Exception:
    logging.warning('Fail load requirements file, so using default ones.')
    install_reqs = []

long_description = open('README.rst').read()

setup(
    name='vgif',
    version='1.0.2',
    url='https://github.com/ozheng1993/video2gif',
    author='ozheng1993',
    author_email='ouzheng1993@gmail.com',
    license='MIT',
    description='https://github.com/ozheng1993/video2gif',
    packages=["vgif"],
    install_requires=install_reqs,
    include_package_data=True,
    python_requires='>=3.7',
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Visualization",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords="image video gif",
    entry_points={π
        'console_scripts': [
            'vgif-gui=vgif.main:main',
            'vgif=vgif.video2gif:main',
        ],
    },
)
