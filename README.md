# NumberDetection-HW2
## YOLOv4
Download the YOLOv4
```
git clone https://github.com/AlexeyAB/darknet
cd clone
```
Set up the Makefile
Modify the following lines
```
GPU=1
CUDNN=1
CUDNN_HALF=1
OPENCV=1
AVX=0
OPENMP=0
LIBSO=1
ZED_CAMERA=0
ZED_CAMERA_v2_8=0
```
According to your gpus, the ARCH should be set. My environment is RTX 2060, so the following lines also need to be uncommented.
```
# GeForce RTX 2080 Ti, RTX 2080, RTX 2070, Quadro RTX 8000, Quadro RTX 6000, Quadro RTX 5000, Tesla T4, XNOR Tensor Cores
ARCH= -gencode arch=compute_75,code=[sm_75,compute_75]
```
Then use make to compile the darknet
