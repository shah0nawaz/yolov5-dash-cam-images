# yolov5-dash-cam-images
# Introduction
The goal of this project was to detect four types of object (Car, Truck, Stop-Sign, Traffic-Light) in dash cam images. Technically, the underline aim of this repository is to optimizer the state of the art object detection algorithms on dash cam images. This repository uses the most accuracte architecture of yolov5x for this purpose. The discription of the data can be seen at https://aiconnect.gomotive.com/aichallenge/. 
# Clone the Repository & install the libaries
```
git clone https://github.com/shah0nawaz/yolov5-dash-cam-images.git
cd yolov5-dash-cam-images
pip install -r requirements.txt
wget https://github.com/ultralytics/yolov5/releases/download/v2.0/yolov5x.pt
```

# Training Data
The training data consists of 40,000 labled training images and 7,000 unlabled testing images. The data can be downloaded from the https://drive.google.com/drive/folders/1R0IdV3EfhY2GHf6vEQU_0BZwuSveqZ3q. The data floder contains the following directories and files.
data
```
  -- train
    -- train_gt.json
    -- train_images.z01
    -- train_images.z02
    -- train_images.z03
    -- train_images.z04
    -- train_images.z05
    -- train_images.z06
    -- train_images.zip
    -- unzip commands.txt
  -- public_test
    -- public_testset_images.zip
```
# Preparing Data
Firstly, download all the files and folders the run the commands in the  in the unzip commands.txt files to extract the images.

```
zip -F train_images.zip --out single_file.zip
unzip single_file.zip

```

This will create train_images folder, which contains all of the training images. 
For annotations train_gt.json file is given which contains the annotation of all the files in the training images in coco format.In order to convert annotations from coco to yolo format, here is the format procedure:
first creat a folder named 'annotations' in the directory where the train_gt.json exists. Now go to the ./data/scripts folder and run the following command.
```
python coco_yolo.py path_to/train_gt.json path_to/annotations
```
Now create a directory for training data
```
  yolov5/train_data
    -- train
      -- images
      -- labels
    -- val
      -- images
      -- labels
```

Run the following command from the ./data/script/train_val_split.py
```
python train_val_split.py path_extracted_images/ path_yolo_formate_annotations/ path_to/train_data/train path_to/train_data/val 0.8 0.2
```


# Training yolov5x for Dash cam Images
The dash-cam-images.yaml should look line below
```

train: ./train_data/images/train  
val: ./train_data/images/validation  


# Classes
nc: 4  # number of classes
names: ["Car", "Truck", "Stop-Sign", "Traffic-Light"]  # class names

```
Run the following command to start training
```
python train.py python train.py --data dash-cam-images.yaml --cfg yolov5x-dashcam.yaml --weights '' --batch-size devices 0,1

```
# Testing and Validation Results
