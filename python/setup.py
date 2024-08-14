#!/usr/bin/env python

from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# with open(path.join(here, '..', 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()

setup(
    name="reachy2-sdk-api",
    version="1.0.8",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "grpcio>=1.59.0, <=1.62.2",
        "grpcio-tools>=1.59.0, <=1.62.2",
        "protobuf>=4.25.0, <=4.25.3",
    ],
    author="Pollen Robotics",
    author_email="contact@pollen-robotics.com",
    url="https://github.com/pollen-robotics/reachy2-sdk-api",
    description="gRPC Protobuf API definition for Reachy 2 SDK",
    # long_description=long_description,
    long_description_content_type="text/markdown",
)
