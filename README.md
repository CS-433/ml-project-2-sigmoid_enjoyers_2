[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/UDdkOEMs)

# Task
In this project we train segmentation models to conduct pixel-wise classification of satellite images taken of Greenland. The goal is to be able to accurately label changing landscapes without any manual work.


# Prerequisites
The data required to run any code can be found [here](https://enacshare.epfl.ch/bY2wS5TcA4CefGks7NtXg) (1.4GB). Download Landcover_Greenland.zip. After unzipping all the data needs to be in images/ folder.

The libraries required to run the code are in requirements.txt

# Repository setup

## Data preparation
The file data_preprocessing.ipynb contains all of the preprocessing we do with the data. Before running any model training, this needs to be run. It will generate cached training and validation data in cache/. In our training notebooks there are designated cells to executing the code in data_preprocessing.ipynb. They are commented out as this notebook needs to only be run once.

## Best model
The code to producing our best model is found in best_model_training.ipynb. with a CPU it takes around 6h to train. To download the model this code produces 
[you can click here](https://epflch-my.sharepoint.com/:u:/g/personal/rasmus_veski_epfl_ch/EVNf9gKOXrRPph5S3I4-jWQBvgB6pU3lz1u-sMCdNcEPtQ?e=uyQCDC) (226MB)
This notebook also contains the code to produce the accuracy and IoU scores you see in the report.

Additionally, you can run best_model_analysis.ipynb, which contains the code to analyse how our best model predicted specific images. For choosing the testing image regulate the  indice argument in the plot_truth_and_prediction() function.


