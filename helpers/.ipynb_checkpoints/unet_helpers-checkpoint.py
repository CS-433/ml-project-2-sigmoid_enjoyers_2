#Read the given filepath for the presaved logs of the training of a unet
def read_unet_logs(filepath):
    train_accuracies = []
    train_losses = []
    val_accuracies = []
    val_losses = []
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            if line[0] != "E": #Ignore epoch line
                lineparts = line.split("-")
                train_accuracies.append(float(lineparts[1].split()[1]))
                train_losses.append(float(lineparts[2].split()[1]))
                val_accuracies.append(float(lineparts[3].split()[1]))
                val_losses.append(float(lineparts[4].split()[1]))
    return train_accuracies, train_losses, val_accuracies, val_losses

def read_unet_with_iou(filepath):
    train_accuracies = []
    train_losses = []
    train_ious = []
    val_accuracies = []
    val_losses = []
    val_ious = []
    with open(filepath, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for i in range(3,len(lines),4):
            line = lines[i]
            if line[0] != "E": #Ignore epoch line
                lineparts = line.split("-")
                train_accuracies.append(float(lineparts[1].split()[1]))
                train_losses.append(float(lineparts[2].split()[1]))
                train_ious.append(float(lineparts[3].split()[1]))
                val_accuracies.append(float(lineparts[4].split()[1]))
                val_losses.append(float(lineparts[5].split()[1]))
                val_ious.append(float(lineparts[6].split()[1]))
    return train_accuracies, train_losses, train_ious, val_accuracies, val_losses, val_ious