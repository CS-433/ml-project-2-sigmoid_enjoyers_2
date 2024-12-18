# Task
In this project we train segmentation models to conduct pixel-wise classification of satellite images taken of Greenland. The goal is to be able to accurately label changing landscapes without any manual work.


# Prerequisites
The data required to run any code can be found [here](https://enacshare.epfl.ch/bY2wS5TcA4CefGks7NtXg) (1.4GB). Download Landcover_Greenland.zip. After unzipping all the data needs to be in images/ and labels/ folders.

The libraries required to run the code are in requirements.txt

# Repository setup
With Python version 3.9.21 (probably works for other versions too, but we have tested with 3.9.21), run ```pip install -r requirements.txt```.
After this all files in the repository should be runnable.

## Data preparation
The file data_preprocessing.ipynb contains all of the preprocessing we do with the data. Before running any model training, this needs to be run. It will generate cached training and validation data in cache/. In our training notebooks there are designated cells to executing the code in data_preprocessing.ipynb. They are commented out as this notebook needs to only be run once.

## Distribution of labels
In the file labels_distribution.ipynb, we analyze the distribution of different classes in the training and test datasets.

## Best model
The code to producing our best model is found in best_model_training.ipynb. This model was taken from a publicly available implementation from [this GitHub repository](https://github.com/K-Mike/Automatic-salt-deposits-segmentation). Specifically we took models.py and blocks.py files, and before we used them we modified the model (```UNetResNextHyperSE```) to fit our data.
With a CPU, it takes around 6h to train. To download the model this code produces 
[you can click here](https://epflch-my.sharepoint.com/:u:/g/personal/rasmus_veski_epfl_ch/EVNf9gKOXrRPph5S3I4-jWQBvgB6pU3lz1u-sMCdNcEPtQ?e=uyQCDC) (226MB).
Put the best_model.pth file in the models-folder. This notebook also contains the code to produce the accuracy and IoU scores you see in the report. If you only want the evaluation part then just run the imports, put the downloaded model into the models-folder and execute the code in the evaluation section

Additionally, you can run best_model_analysis.ipynb, which contains the code to analyse how our best model predicted specific images. To choose the testing image, change the indice argument in the plot_truth_and_prediction() function.

## Other models
The training and evaluation of all our other models is in modelling_clean.ipynb. This is a huge notebook, which is not feasible to be "run all" (would take a day on CPU). It is structured like the results table in the report.

To train a desired model first read the data you want to train it with. The "Reading data section" has 3 cells:
*Unaugmented data (2016)
*Augmented data (2016)
*All years data

Run the cell which data you want (you can run all if you have tons of memory)

Then proceed to Modelling choose the section of which model you want to run: U-Net, DeepLab or Hypercolumn. Run all cells in those sections until section Baseline. From here choose either Baseline, Augmented Data or All Data. To train and evaluate that model run all cells inside the chosen section.

To preserve you from waiting on the training process, the logs of our previous trainings are written into files in training_logs/. These are read in for the plotting of the training. However, due to the models themselves being large, we have not saved the worse models. To display new plots for a new training run, copy over the output of the training cell to the corresponding text file in training_logs, then run the code that reads the text files and generates the plots.

Finally, there is a file Training_for_iou.ipynb, which contains the training and evaluation process for our U-Net model using a custom loss function described in the report section III. MODELS AND METHODS - U-Net.
