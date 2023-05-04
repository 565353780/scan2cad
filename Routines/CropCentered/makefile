all : CropCentered.so

CropCentered.so : CropCentered.cpp
	c++ -I../Base -I${CONDA_PREFIX}/include/python3.8 -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` $^ -o $@

clean:
	rm CropCentered.so
