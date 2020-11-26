import json
import cv2

with open('result.json') as f:
	table = json.load(f)

for i in range(10):
  img_cv = cv2.imread('../../Downloads/test/%d.png' % (i+1))
  for det in table[i]['bbox']:
    y1, x1, y2, x2 = det
    img_cv = cv2.rectangle(img_cv, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0))
  cv2.imwrite('results/%d.png' % i, img_cv)

