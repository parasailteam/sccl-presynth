# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from sccl.autosynth.registry import register_ef_file
import os

_base = os.path.dirname(os.path.realpath(__file__))

register_ef_file(os.path.join(_base, 'Alltoall.n8-DGX1-steps2.rounds8.chunks3.sccl.xml'),
    'alltoall', 'dgx1', 1)

# DistSCCL generated algorithms
register_ef_file(os.path.join(_base, 'Allgather.n24-DistributedRelayedSwitch.localDGX1.copies3.bw0.5.senders.0.8.16.receivers.1.9.17-steps32.rounds68-gurobisol-improve-1627851830_i8_scRemote1.sccl.xml'),
    'allgather', 'ndv2', 3)
register_ef_file(os.path.join(_base, 'Allgather.n32-DistributedRelayedSwitch.localDGX1.copies4.bw0.5.senders.0.8.16.24.receivers.1.9.17.25-steps51.rounds94-gurobisol-improve-1627847444_i8_scRemote1.sccl.xml'),
    'allgather', 'ndv2', 4)
register_ef_file(os.path.join(_base, 'Alltoall.n16-DistributedRelayed.localDGX1.copies2.bw0.5.relays.0.1-steps9.rounds87.i8-gurobisol-improve-1626737981.sccl.xml'),
    'alltoall', 'ndv2', 2)
register_ef_file(os.path.join(_base, 'Alltoall.n24-DistributedRelayedSwitch.localDGX1.copies3-steps74-gurobisol-echecksol-1628634296_i8_scRemote1.sccl.xml'),
    'alltoall', 'ndv2', 3)