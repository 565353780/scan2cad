# Scan2CAD

## Download

download 3 datasets

```bash
ScanNet, ShapeNet, Scan2CAD datasets
```

and edit the file

```bash
./Routines/Script/Parameters.json
```

## Install

```bash
conda create -n s2c python=3.8
conda activate s2c
./setup.sh
```

## Data generation

```bash
python Routines/Script/Annotation2Mesh.py
python Routines/Script/CADVoxelization.py
python Routines/Script/GenerateCorrespondences.py
```

## Train

```bash
./Network/pytorch/run.sh
```

## Run

```bash
python Routines/Script/Alignment9DoF.py --projectdir ./Network/pytorch/output/dummy
```

## Enjoy it~
