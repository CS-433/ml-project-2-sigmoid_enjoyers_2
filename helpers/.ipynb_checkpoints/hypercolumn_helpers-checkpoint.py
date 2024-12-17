
def load_data(file_path):
    """Load data from a txt file and return as a list of floats."""
    with open(file_path, 'r') as file:
        data = [float(line.strip()) for line in file]
    return data

def plot_combined_folder_data(folder_name, folder_path):
    """Generate a figure for a specific folder with all plots included."""
    plt.figure(figsize=(10, 6))
    plt.title(f"Performance Metrics - {folder_name}", fontsize=16)
    
    # Colors and labels for each metric
    metric_labels = {
        'train_accuracies.txt': 'Train Accuracy',
        'train_losses.txt': 'Train Loss',
        'val_accuracies.txt': 'Validation Accuracy',
        'val_losses.txt': 'Validation Loss'
    }
    
    for metric in metrics:
        metric_file = os.path.join(folder_path, metric)
        if os.path.exists(metric_file):
            data = load_data(metric_file)
            plt.plot(range(len(data)), data, label=metric_labels[metric])
    
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy / Loss')
    plt.xticks(range(0, len(data), max(1, len(data)//10)))  # Adjust ticks based on data length
    plt.legend(loc='best')
    plt.grid(alpha=0.5)
    plt.tight_layout()
    
    # Save the plot to a file
    save_path = os.path.join('plots/Hypercolumn', f"hypercolumn_all_{folder_name}.png")
    plt.savefig(save_path)
    print(f"Saved plot to {save_path}")
    
    plt.show()
