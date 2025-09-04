#!/usr/bin/env python

from os import path
import re

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))
version_file = path.join(here, "reachy2_sdk_api", "__init__.py")

with open(version_file, "r") as f:
    version_match = re.search(r'__version__ = "(.*?)"', f.read())
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Version not found")

# with open(path.join(here, '..', 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()

setup(
    name="reachy2_sdk_api",
    version=version,
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "grpcio>=1.59.0, <=1.73.1",
        "grpcio-tools>=1.59.0, <=1.73.1",
        "protobuf>=4.25.0, <=6.32.0",
    ],
    author="Pollen Robotics",
    author_email="contact@pollen-robotics.com",
    url="https://github.com/pollen-robotics/reachy2-sdk-api",
    description="gRPC Protobuf API definition for Reachy 2 SDK",
    # long_description=long_description,
    long_description_content_type="text/markdown",
)
