# yolov5-dash-cam-images
# Introduction
The goal of this project was to detect four types of object (Car, Truck, Stop-Sign, Traffic-Light) in dash cam images. Technically, the underline aim of this repository is to optimizer the state of the art object detection algorithms on dash cam images. This repository uses the most accuracte architecture of yolov5x for this purpose. The discription of the data can be seen at https://aiconnect.gomotive.com/aichallenge/. 
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
This will create train_images folder, which will contain all of the training images. 
For annotations train_gt.json file is given which contains the annotation of all the files in the training images in coco format.
# Training yolov5x for Dash cam Images Competition
# Testing and Validation Results
