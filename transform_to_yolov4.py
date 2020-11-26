import csv
import cv2
from tqdm import tqdm

# ['height', 'img_name', 'label', 'left', 'top', 'width', 'bottom', 'right']
with open('data.csv') as f:
    rows = csv.reader(f)
    next(rows)
    for label in tqdm(rows):
        img_name = label[1]
        img = cv2.imread('train/' + img_name)
        h, w, _ = img.shape
        cv2.rectangle(img, (int(float(label[3])), int(float(label[4]))), (int(float(label[7])), int(float(label[6]))), (255, 0, 0))
        '''
        cv2.imshow('a', img)
        print(int(float(label[2])))
        k = cv2.waitKey(0)
        if k == ord('q'):
            break
        '''
        center_x = (float(label[3]) + float(label[7])) / 2 / w
        center_y = (float(label[4]) + float(label[6])) / 2 / h
        width = float(label[5]) / w
        height = float(label[0]) / h
        name_part = img_name.split('.')[0]
        with open('train/' + name_part + '.txt', 'a') as f_out:
            f_out.write('%d %f %f %f %f\n' % (int(float(label[2]))%10, center_x, center_y, width, height))


