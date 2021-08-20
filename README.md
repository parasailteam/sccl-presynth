# SCCL Presynth

This is a repository of pre-synthesized [SCCL](https://github.com/microsoft/sccl) algorithms, mainly including algorithms that would be too slow to synthesize at the start of every run.

## Setup

The package can be installed from GitHub with:
```
pip install git+https://github.com/parasailteam/sccl-presynth
```
You can also just add the root of the repo to `PYTHONPATH`:
```
PYTHONPATH=/.../sccl-presynth/ python your_script.py
```

## Usage

Importing the the `sccl_presynth` module will register all the algorithms for a subsequent call to `sccl.init`.

For example, the following code will select a presynthesized Alltoall algorithm for a single DGX-1:
```
import sccl
import sccl_presynth
sccl.init(1, 'dgx1', ('alltoall', '1MB'))
```