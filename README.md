# NumberDetection-HW2
## Dataset
First, extract the train and test data.  
Modify the DATA_ROOT in generate_data_list.py to current folder.
```
DATA_ROOT = '/YOUR/PATH'
```
Run the following scripts.
```
python3 read_label.py
python3 transform_to_yolov4.py
python3 generate_data_list.py
```

## YOLOv4
Download the YOLOv4
```
git clone https://github.com/AlexeyAB/darknet
cd darknet
```
download pretrained model at 
https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.conv.29  
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

## Setup Configs
create a hw2.data with following contents
```
classes = 10
train = /YOUR/PATH/train_list.txt
valid = /YOUR/PATH/val_list.txt
names = /YOUR/PATH/names.names
backup = backup
```
Then create a folder named 'backup'.
put the yolov4-tiny-digit.config and yolov4-tiny-digit_best.weights under the darknet folder  
## Training
```
./darknet detector train hw2.data yolov4-tiny-digit.cfg yolov4-tiny.conv.29 -map
```
## Testing
Modify the 32th line in YOLOv4_inferences.py
```
img_dn = dn.load_image(b'YOUR/PATH/test/%d.png' % (index+1), 0, 0)
```
Then run the inference script. The result will save into result.json
```
python3 YOLOv4_inferences.py
```
