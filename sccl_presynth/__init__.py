# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from sccl.autosynth.registry import register_ef_file
import os

_base = os.path.dirname(os.path.realpath(__file__))

register_ef_file(os.path.join(_base, 'Alltoall.n8-DGX1-steps2.rounds8.chunks3.sccl.xml'),
    'alltoall', 'dgx1', 1)

# DistSCCL generated algorithms
register_ef_file(os.path.join(_base, 'Alltoall.n16-DistributedRelayed.localDGX1.copies2.bw0.5.relays.0.1-steps9.rounds87.i8-gurobisol-improve-1626737981.sccl.xml'),
    'alltoall', 'ndv2', 2)
register_ef_file(os.path.join(_base, 'Alltoall.n24-DistributedRelayedSwitch.localDGX1.copies3-steps74-gurobisol-echecksol-1628634296_i8_scRemote1.sccl.xml'),
    'alltoall', 'ndv2', 3)
# New DistSCCL algorithms from paper
register_ef_file(os.path.join(_base, 'Allgather.n16-DistributedRelayedSwitch.localDGX1_1KB.copies2.lenrelay2-steps16-gurobisol-improve-1633890614_i1_scRemote1_IBContig_h6.sccl.xml'),
    'allgather', 'ndv2', 2, sizes=(0, '1MB'))
register_ef_file(os.path.join(_base, 'Allgather.n16-DistributedRelayedSwitch.localDGX1.copies2-steps20-gurobisol-improve-1630536923_i8_scRemote1_IBContig_h5-noring.sccl.xml'),
    'allgather', 'ndv2', 2, sizes=('1MB', None))
register_ef_file(os.path.join(_base, 'Allgather.n24-DistributedRelayedSwitch.localDGX1.copies3-steps37-gurobisol-improve-1630536831_i8_scRemote1_IBContig_h5-noring.sccl.xml'),
    'allgather', 'ndv2', 3, sizes=('1MB', None))
register_ef_file(os.path.join(_base, 'Allgather.n32-DistributedRelayedSwitch.localDGX1.copies4-steps36-gurobisol-improve-1630536862_i8_scRemote1_IBContig_h5-noring.sccl.xml'),
    'allgather', 'ndv2', 4, sizes=('1MB', None))
register_ef_file(os.path.join(_base, 'Allgather.n64-DistributedRelayedSwitch.localDGX1.copies8-steps96-gurobisol-improve-1630083984_i8_scRemote1_IBContig_h5-noring.sccl.xml'),
    'allgather', 'ndv2', 8, sizes=('4MB', None))
register_ef_file(os.path.join(_base, 'Allreduce.n16-DistributedRelayedSwitch.localDGX1.copies2-steps42.chunks16-gurobisol-1633806993-allreduce-1633807120_i1_scRemote1.sccl.xml'),
    'allreduce', 'ndv2', 2, sizes=('1KB', '512KB'))
register_ef_file(os.path.join(_base, 'Allreduce.n16-DistributedRelayedSwitch.localDGX1.copies2-steps42.chunks16-gurobisol-1633806993-allreduce-1633807120_i8_scRemote1.sccl.xml'),
    'allreduce', 'ndv2', 2, sizes=('1MB', '4MB'))
register_ef_file(os.path.join(_base, 'Allreduce.n16-DistributedRelayedSwitch.localDGX1.copies2-steps50.chunks16-gurobisol-1633828661-allreduce-1633829074_i8_scRemote1.sccl.xml'),
    'allreduce', 'ndv2', 2, sizes=('4MB', None))
register_ef_file(os.path.join(_base, 'Allreduce.n32-DistributedRelayedSwitch.localDGX1.copies4-steps124.chunks32-gurobisol-1633844712-allreduce-1633845033_i1_scRemote1_IBContig.sccl.xml'),
    'allreduce', 'ndv2', 4, sizes=('1KB', '1MB'))
register_ef_file(os.path.join(_base, 'Allreduce.n32-DistributedRelayedSwitch.localDGX1.copies4-steps124.chunks32-gurobisol-1633844712-allreduce-1633845033_i8_scRemote1_IBContig.sccl.xml'),
    'allreduce', 'ndv2', 4, sizes=('1MB', None))
register_ef_file(os.path.join(_base, 'Allgather.n32-DistributedRelayedSwitch.localHubAndSpokeDGX2RSwitch1KB1.n16.copies2-steps6-gurobisol-improve-1633118567_i1_scRemote1_IBContig_maxUnique_h10.sccl.xml'),
    'allgather', 'dgx2', 2, sizes=('1KB', '2MB'))
register_ef_file(os.path.join(_base, 'Allgather.n32-DistributedRelayedSwitch.localHubAndSpokeDGX2RSwitch32KB1.n16.copies2-steps9-gurobisol-improve-1633067748_i1_scRemote1_IBContig_maxUnique_h10.sccl.xml'),
    'allgather', 'dgx2', 2, sizes=('4MB', '16MB'))
register_ef_file(os.path.join(_base, 'Allgather.n32-DistributedRelayedSwitch.localHubAndSpokeDGX2RFix2.n16.copies2-steps31-gurobisol-improve-1631300207_i8_scRemote1_IBContig_h10c.sccl.xml'),
    'allgather', 'dgx2', 2, sizes=('32MB', '128MB'))
register_ef_file(os.path.join(_base, 'Allgather.n32-DistributedRelayedSwitch.localHubAndSpokeDGX2RFix.n16.copies2-steps46.chunks2-gurobisol-improve-1630969663_i8_scRemote1_IBContig_mup01_IntFocus.sccl.xml'),
    'allgather', 'dgx2', 2, sizes=('256MB', '1GB'))
register_ef_file(os.path.join(_base, 'Alltoall.n32-DistributedRelayed.localHubAndSpokeDGX2RFixOE.n16.copies2.ibconn16-steps1-gurobisol-improve-1633034665_i1_scRemote1_IBContig_maxUnique_h11.sccl.xml'),
    'alltoall', 'dgx2', 2, sizes=('1KB', '4MB'))
register_ef_file(os.path.join(_base, 'Alltoall.n32-DistributedRelayed.localHubAndSpokeDGX2RFix.n16.copies2.ibconn1-steps23-gurobisol-improve-1632620828_i2_scRemote1_IBContig_maxUnique_h11.sccl.xml'),
    'alltoall', 'dgx2', 2, sizes=('4MB', None))