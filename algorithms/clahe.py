import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('t.jpg',0)

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv2.imwrite('res2.jpg',cl1)
