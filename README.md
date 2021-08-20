# SCCL Presynth

This is a repository of pre-synthesized [SCCL](https://github.com/microsoft/sccl) algorithms, mainly including algorithms that would be too slow to synthesize at the start of every run.

Importing the the `sccl_presynth` module from the root of the repository will register all the algorithms for a subsequent call to `sccl.init`.

For example, the following code will select a presynthesized Alltoall algorithm for a single DGX-1:
```
import sccl
import sccl_presynth
sccl.init(1, 'dgx1', ('alltoall', '1MB'))
```
You may need to add the root of the repository to `PYTHONPATH` to let Python find the module, for example:
```
PYTHONPATH=<path-to-repo> python3 train.py
```