# Installing EfDS course environment with conda/mamba

The following environment file is provided to install the EfDS course environment with conda/mamba.
It has been checked to work on macOS and Linux.
An older version of `sqlalchemy` is required to work with the current version of `pandas`.
After the environment is installed, you can activate it with `conda activate EfDS2` and/or use the python kernel `EfDS2` in Jupyter.

```
(base) $ mamba env create -f EfDS2.yaml                                                                                                                                [7:45:44]
pkgs/r/osx-64            [====================] (00m:00s) No change
pkgs/r/noarch            [====================] (00m:00s) No change
pkgs/main/noarch         [====================] (00m:00s) Done
pkgs/main/osx-64         [====================] (00m:01s) Done
conda-forge/noarch       [====================] (00m:03s) Done
conda-forge/osx-64       [====================] (00m:07s) Done

Looking for: ['mysql', "sqlalchemy[version='<2.0']", 'pysqlite3', 'numpy', 'pandas', 'seaborn', 'matplotlib', 'ipykernel', 'ipython-sql']

Transaction

  Prefix: ~/miniconda3/envs/EfDS2

  Updating specs:

   - mysql
   - sqlalchemy[version='<2.0']
   - pysqlite3
   - numpy
   - pandas
   - seaborn
   - matplotlib
   - ipykernel
   - ipython-sql
```

(some more messages here)

```
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate EfDS2
#
# To deactivate an active environment, use
#
#     $ conda deactivate

```