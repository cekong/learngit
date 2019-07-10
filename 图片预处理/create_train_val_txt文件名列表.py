# -- coding: utf-8 --
# 生成trainval.txt文件
import os

def file_name(file_dir):
    # filecount = len([name for name in os.listdir(file_dir) if os.path.isfile(os.path.join(file_dir, name))])
    # print(filecount,'张图片')
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            a=os.path.splitext(file)
            if os.path.splitext(file)[1] == '.jpg':
                file_name = file
                L.append(file_name)
    return L

label_folder = '/home/deepl/share/platedata/原数据/未命名文件夹'
trainval_file = 'train_val_list.txt'

txt_name = file_name(label_folder)

with open(trainval_file, 'w') as f:
  for i in txt_name:
    f.write('{}\n'.format(i))
f.close()