# python coco_yolo.py train_gt.json annotations/ 

import os
import glob
import json
import pandas as pd
import time
import sys
import shutil



class CocoYolo:
   def __init__(self, train_gt_path, anno_save_path):
      if os.path.exists(anno_save_path):
          shutil.rmtree(anno_save_path)
      else:
          os.mkdir(anno_save_path)
          
      self.train_gt_path = train_gt_path
      self.anno_save_path = anno_save_path

   def load_json_file(self):
      print(f'Loading json Data from: {self.train_gt_path}')
      with open(self.train_gt_path, 'r') as f:
         data = json.load(f)
      return data

   def get_anno_images_info(self, data):
      images_info = data['images']
      annotations_info = data['annotations']
      return images_info, annotations_info


   def get_anno_by_image_id(self, anno_info):
      df_anno = pd.DataFrame(anno_info)
      df_anno_group = df_anno.groupby('image_id')

      return df_anno_group

   def get_img_data(self, img_data):
      img_id = img_data['id']
      file_name = img_data['file_name']
      height = img_data['height']
      width = img_data['width']
      return img_id, file_name,height, width

   def get_anno_data(self, row, height, width):
      image_id = row[0]
      bbox = row[1]
      category_id = row[2]
      print(f'category ID: {category_id}')
      x_left = round((bbox[0]) / width, 4)
      y_top = round((bbox[1]) / height, 4)
      w = round((bbox[2]) / width, 4)
      h = round((bbox[3]) / height, 4)
      x = round(x_left + w / 2, 4)
      y = round(y_top + h / 2, 4)
      return x, y, w, h, category_id





   def main(self):
      data = self.load_json_file()
      images_info, anno_info = self.get_anno_images_info(data)
      df_anno_group = self.get_anno_by_image_id(anno_info)
      count = 0
      for img_data, df_anno_g in zip(images_info, df_anno_group):
         if img_data['id'] == df_anno_g[0]:
            img_id , file_name, height, width = self.get_img_data(img_data)
            with open(self.anno_save_path + file_name.split('.')[0] + '.txt', 'w') as f:
               for index, row in df_anno_g[1].iterrows():

                  x,y,w,h, category_id = self.get_anno_data(row, height, width)

                  if (x or y or h or w) <= 0:
                     print('here')
                  category_id = category_id - 1
                  data = str(category_id) + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h) + '\n'
                  f.write(data)
               f.close()
            #print(count)


gt_path = sys.argv[1]
save_path = sys.argv[2]

cocoyolo = CocoYolo(gt_path, save_path)
cocoyolo.main()



