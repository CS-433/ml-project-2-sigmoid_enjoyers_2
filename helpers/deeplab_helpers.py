#Calculates accuracy between outputs and target values, where both are a 4-dimensional torch tensor
def calculate_accuracy(outputs, targets):
    #Reduce dimensions back from one-hot encoding to compare
    predictions = torch.argmax(outputs, dim=1)
    targets_values = torch.argmax(targets, dim=1)
    correct = (predictions == targets_values).float() #Label 1 where true 0 where not
    return (correct.sum() / correct.numel()).item() #Return accuracy

#Calculates the intersection over union between two torch tensors
def calculate_IOU(outputs, targets, num_classes):
    #Reduce dimensions back from one-hot encoding to compare
    preds = torch.argmax(outputs, dim=1)
    labels = torch.argmax(targets, dim=1)
    
    iou_list = []
    #Iterate over classes
    for cls in range(num_classes):
        pred_mask = (preds == cls)
        label_mask = (labels == cls)
        intersection = (pred_mask & label_mask).sum().item()
        union = (pred_mask | label_mask).sum().item()
        if union == 0:
            iou = 0  # Avoid division by zero
        else:
            iou = intersection / union
        iou_list.append(iou)
    return iou_list


#Reads the deeplab training logs in the format they were written in
def read_deeplab_logs(filepath):
    train_accuracies = []
    train_losses = []
    val_accuracies = []
    val_losses = []
    train_ious = []
    val_ious = []
    
    with open(filepath, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            lineparts = line.split(";")
            train_losses.append(float(lineparts[1].split(":")[1]))
            val_losses.append(float(lineparts[2].split(":")[1]))
            train_accuracies.append(float(lineparts[3].split(":")[1]))
            val_accuracies.append(float(lineparts[4].split(":")[1]))
            train_iou_list = ast.literal_eval(lineparts[5].split(":")[1])
            train_ious.append(train_iou_list)
            val_iou_list = ast.literal_eval(lineparts[6].split(":")[1])
            val_ious.append(val_iou_list)
            
    return train_accuracies, train_losses, train_ious, val_accuracies, val_losses, val_ious