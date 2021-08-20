# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from sccl.autosynth.registry import register_ef_file
import os

_base = os.path.dirname(os.path.realpath(__file__))

register_ef_file(os.path.join(_base, 'Alltoall.n8-DGX1-steps2.rounds8.chunks3.sccl.xml'),
    'alltoall', 'dgx1', 1)
