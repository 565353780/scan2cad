pip install numpy-quaternion pywavefront pybind11

pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 \
  --extra-index-url https://download.pytorch.org/whl/cu117

pip install numpy==1.23.5 plyfile==0.8.1

cd ./Routines/Vox2Mesh
make clean
make -j

cd ../DFGen
make clean
make -j

cd ../CropCentered
make clean
make -j
