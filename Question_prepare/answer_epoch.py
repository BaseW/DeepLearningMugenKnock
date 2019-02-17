import cv2
import numpy as np
from glob import glob

np.random.seed(0)

num_classes = 2
img_height, img_width = 64, 64

# get train data
def data_load(path):
    xs = np.ndarray((0, img_height, img_width, 3))
    ts = np.ndarray((0))
    paths = []
    
    for dir_path in glob(path + '/*'):
        for path in glob(dir_path + '/*'):
            x = cv2.imread(path)
            x = cv2.resize(x, (img_width, img_height)).astype(np.float32)
            x /= 255.
            xs = np.r_[xs, x[None, ...]]

            t = np.zeros((1))
            if 'akahara' in path:
                t = np.array((0))
            elif 'madara' in path:
                t = np.array((1))
            ts = np.r_[ts, t]

            paths.append(path)

    xs = xs.transpose(0,3,1,2)

    return xs, ts, paths


xs, ts, paths = data_load('../Dataset/train/images/')

mb = 3
mbi = 0
train_ind = np.arange(len(xs))
np.random.seed(0)
np.random.shuffle(train_ind)

epoch_max = 3
epoch = 0

while epoch < epoch_max:
    if mbi + mb > len(xs):
        mb_ind = train_ind[mbi:]
        np.random.shuffle(train_ind)
        mb_ind = np.hstack((mb_ind, train_ind[:(mb-(len(xs)-mbi))]))
        epoch += 1
        mbi = mb - (len(xs) - mbi)
    else:
        mb_ind = train_ind[mbi: mbi+mb]
        mbi += mb

    print(mb_ind)
