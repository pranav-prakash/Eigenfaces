import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os 


DATA_PATH = '/Users/BAlKhamissi/Documents/Datasets/yalefaces'
num_faces = 15
num_per_face = 11
num_images = 165
input_dim = (num_images, 243, 320)
X_train = np.zeros(input_dim, dtype='uint8')
Y_train = np.zeros(input_dim, dtype='uint8')

def imshow(img, gray = True, title=''):
    plt.title(title)
    plt.imshow(img, cmap='gray') if gray else plt.imshow(img)
    plt.show()

for face in xrange(num_faces):
    face_path = os.path.join(DATA_PATH, str(face+1).zfill(2))
    for i, file in enumerate(os.listdir(face_path)):
        file_path = os.path.join(face_path, file)
        img = plt.imread(file_path, 0)
        idx = face*num_per_face+i
        X_train[idx] = img
        Y_train[idx] = face

img_mean = np.mean(X_train, axis=0)
imshow(img_mean, title='Mean Image')

A = X_train - img_mean
U, S, V = np.linalg.svd(A)