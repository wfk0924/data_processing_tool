'''
    opencv绘图
'''

import numpy as np
import cv2
import matplotlib.pyplot as mp
a = np.array([[[10,10], [100,10], [100,100], [10,100]]], dtype = np.int32)
b = np.array([[[100,100], [200,230], [150,200], [100,220]]], dtype = np.int32)
print(a.shape)
im = np.zeros([240, 320], dtype = np.uint8)
cv2.polylines(im, a, 1, 255)
cv2.fillPoly(im, b, 255)
part_list = np.argwhere(im == 255)
part_list = tuple(map(tuple, part_list))
print(part_list)
mp.imshow(im)
mp.show()
