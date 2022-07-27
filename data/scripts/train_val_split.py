import os
import shutil
import glob
import random

random.seed(42)

anno_list = glob.glob('./annotations/*.txt')
print(type(anno_list))
random.shuffle(anno_list)
print(type(anno_list))

train_number = int(len(anno_list)*0.85)
val_number = int(len(anno_list)*0.15)

train_anno_list = anno_list[0: train_number]
val_anno_list = anno_list[train_number:]


for file in train_anno_list:
    #file = train_anno_list[i]
    file_anno = file

    file_image = file.split('/')[-1].split('.')[0]

    shutil.move('./train_images/' + file_image + '.jpeg', './train_data/train/images/')
    shutil.move(file_anno, './train_data/train/labels/' )



for file in val_anno_list:
    #file = train_anno_list[i]
    file_anno = file

    file_image = file.split('/')[-1].split('.')[0]

    shutil.move('./train_images/' + file_image + '.jpeg', './train_data/test/images/')
    shutil.move(file_anno, './train_data/test/labels/' )
