import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Read in the 7 channels of data for all the images in fileList
def extract_channels(fileList):
    images = []
    for filename in fileList:
        with rasterio.open(filename) as src:
            data = np.dstack([src.read(7), src.read(6), src.read(5), src.read(4), src.read(3), src.read(2), src.read(1)])
            images.append(data)
    return np.array(images)

#Extract the labels of all files in filelist (1 channel)
def extract_labels(fileList):
    labels = []
    for filename in fileList:
        with rasterio.open(filename) as src:
            data = src.read(1)
            labels.append(data)
    return np.array(labels)
    
#Expand label data dimenstions
def one_hot_labels(value, length):
    return np.eye(length, dtype=int)[value]

#Undos the one-hot encoding, taking the argmax of the (7) channels for the answer
def array_to_int(preds):
    return np.argmax(preds, axis = -1)


#Plot all given lists, with given parameters. Save plot to filename
def plot_training(plottables, names, from_epoch, plot_title, xlabel, ylabel, filename, have_grid = True):

    epoch_indices = range(len(plottables[0]))

    #Plot all lines
    for i in range(len(plottables)):
        plt.plot(epoch_indices[from_epoch:], plottables[i][from_epoch:], label=names[i])
    
    plt.xticks(range(from_epoch, len(plottables[0]), 2))
    if have_grid:
        plt.grid(alpha=0.3)
        
    #Lables
    plt.title(plot_title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.savefig(filename)
    plt.plot()

#Plot the two given lists side by side, rest adapted from upper function
def plot_iou(lists1, lists2, names, title, from_epoch, filename, have_grid = True, test_ious = None):

    epoch_indices = range(len(lists1[0]))

    fig, axs = plt.subplots(1, 2, figsize=(12, 6),sharey=True) #Create subplots
    #Plot all lines
    for i in range(len(lists1)):
        #Plot the lines for the labels, while extracting the columns
        color = axs[0].plot(epoch_indices[from_epoch:], lists1[i][from_epoch:], label=names[i])[0].get_color()
        axs[1].plot(epoch_indices[from_epoch:], lists2[i][from_epoch:], label=names[i])

        #Plot the test point at the end of the plot
        if test_ious is not None:
            axs[1].scatter(len(epoch_indices) - 1, test_ious[i], color=color, marker='o', label=f"Test {names[i]}")
        
        
    axs[0].set_title("Training IOUs")
    axs[1].set_title("Validation IOUs")
    axs[0].set_xticks(range(from_epoch, len(lists1[0]), 2))
    axs[1].set_xticks(range(from_epoch, len(lists1[0]), 2))
    if have_grid:
        axs[0].grid(alpha=0.3)
        axs[1].grid(alpha=0.3)

    axs[0].set_xlabel("Epochs")
    axs[1].set_xlabel("Epochs")
    axs[0].set_ylabel("IOU")
    axs[1].set_xlabel("IOU")
        
    axs[1].legend(loc="upper left", bbox_to_anchor=(1.05, 1))
    plt.suptitle(title)
    plt.savefig(filename)
    plt.show()