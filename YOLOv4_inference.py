import darknet as dn

import cv2
import numpy as np
from tqdm import tqdm
from ctypes import POINTER, c_float
import json

print('setup darknet')
dn.set_gpu(0)
classes = [str(i) for i in range(10)]

print('load net')
net = dn.load_net(b"cfg/yolov4-tiny-digit.cfg", b"weights/yolov4-tiny-digit_best.weights", 0)

# cv2 image to darknet_image
def array_to_image(arr):
  arr = arr.transpose(2,0,1)
  c, h, w = arr.shape
  arr = (arr.astype(np.float32)/255.0).flatten()
  c_float_p = POINTER(c_float)
  data = arr.ctypes.data_as(c_float_p)
  im = dn.IMAGE(w, h, c, data)
  return im


# convert image format
print('start_to_convert_images')
dark_image_list = []
'''
for img_data in test_list:
  # img_name, img_cv = img_data
  img_dn = array_to_image(img_data)
  dark_image_list.append(img_dn)
'''
for index in range(13068):
  img_dn = dn.load_image(b'../../Downloads/test/%d.png' % (index+1), 0, 0)
  dark_image_list.append(img_dn)
# detect
r_list = []  # results
for img_dn in tqdm(dark_image_list):
  r = dn.detect_image(net, classes, img_dn, thresh=0.2)
  r_list.append(r)
# print(r_list[:100])

final_output = []
for i in range(13068):
  pred = r_list[i]
  bboxes = []
  scores = []
  labels = []
  # img_cv = cv2.imread('../../Downloads/test/%d.png' % (i+1))
  for det in pred:
    # print(det)
    x, y, w, h = det[2]
    x1 = int(x-w/2)
    x2 = int(x+w/2)
    y1 = int(y-h/2)
    y2 = int(y+h/2)
    bbox = (y1, x1, y2, x2)
    bboxes.append(bbox)
    scores.append(float(det[1]))
    labels.append(int(det[0]))
  final_output.append({'bbox': bboxes, 'score': scores, 'label': labels})

with open('result.json', 'w') as output_file:
  json.dump(final_output, output_file)

'''
    img_cv = cv2.rectangle(img_cv, (x1, y1), (x2, y2), (255, 0, 0))
  print()
  cv2.imwrite('results/%d.png' % i, img_cv)
'''
