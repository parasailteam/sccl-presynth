# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from setuptools import setup

setup(
    name='sccl-presynth',
    version='1.0.0',
    packages=['sccl_presynth'],
    package_data={'sccl_presynth': ['*.xml']},
    include_package_data=True,
    install_requires=[
        'sccl',
    ]
)
