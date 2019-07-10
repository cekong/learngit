import numpy as np
import cv2
import os
import random
from tqdm import tqdm
train_txt_path = './train_val_list.txt' #图片文件名列表

CNum = 1000  # 挑选多少图片进行计算

img_h, img_w = 128, 128
means, stdevs = [], []
imgs = np.empty([img_h,img_w,3,CNum])
with open(train_txt_path, 'r') as f:
    lines = f.readlines()
    random.shuffle(lines)  # shuffle , 随机挑选图片

    for i in tqdm(range(CNum)): #tqdm 进度提示信息
        img_path = os.path.join('/media/deepl/文档/platedata/未命名文件夹', lines[i].rstrip().split()[0])

        img = cv2.imread(img_path)
        img = cv2.resize(img, (img_h, img_w))
        imgs[:,:,:,i] = img

imgs = imgs.astype(np.float32) / 255.

for i in tqdm(range(3)):
    pixels = imgs[:, :, i, :].ravel()  # 拉成一行
    means.append(np.mean(pixels))
    stdevs.append(np.std(pixels))

# cv2 读取的图像格式为BGR，PIL/Skimage读取到的都是RGB不用转
means.reverse()  # BGR --> RGB
stdevs.reverse()

print("normMean = {}".format(means))
print("normStd = {}".format(stdevs))
print('transforms.Normalize(normMean = {}, normStd = {})'.format(means, stdevs))
