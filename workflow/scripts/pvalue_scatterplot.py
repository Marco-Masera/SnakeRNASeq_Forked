#!/usr/bin/env python3
import csv
import sys
import matplotlib.pyplot as plt
import numpy as np

def process_csv(file_path):
    values = []
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            for row in reader:
                if len(row) < 3:
                    continue
                try:
                    value = float(row[2])
                    values.append(value)
                except ValueError:
                    print(f"Warning: Unable to convert '{row[2]}' to float in file {file_path}.")
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
    return values

def process_csv_with_key(file_path):
    values = dict()
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            for row in reader:
                if len(row) < 3:
                    continue
                try:
                    value = float(row[2])
                    key = row[0]
                    values[key] = value
                except ValueError:
                    print(f"Warning: Unable to convert '{row[2]}' to float in file {file_path}.")
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
    return values

def plot_data(datasets, file_labels):
    # Create 1 row, 3 columns of subplots
    fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
    colors = ['red', 'blue', 'green']
    names = [
        n.replace("DGE/", "").replace("_contrast.csv","").replace(".toptable_clean.ALL_contrast.mark_seqc.header_added.csv","")
        for n in file_labels
    ]
    
    for i, values in enumerate(datasets):
        if not values:
            axes[i].set_title(f"{names[i]}\n(No data)")
            continue
        
        # X-axis: indices of the values
        x = np.random.uniform(0,100, len(values))
        p_values = np.array(values)
        # To avoid math error for p-value 0, replace non-positive values with a tiny positive number.
        p_values = np.where(p_values <= 0, 1e-310, p_values)
        y = -np.log10(p_values)
        
        axes[i].scatter(x, y, color=colors[i], s=10)
        axes[i].set_title(names[i])
        axes[i].set_xlabel("Index")
        if i == 0:
            axes[i].set_ylabel("-log10(p-value)")
    
    plt.tight_layout()
    plt.savefig("pvalues_scatterplot.png", transparent=None, dpi='figure', format=None,
        metadata=None, bbox_inches=None, pad_inches=0.1,
        facecolor='auto', edgecolor='auto', backend=None
       )

def scatter_vs(datasets, file_labels):
    # Create 1 row, 3 columns of subplots
    fig, axes = plt.subplots(1, 2, figsize=(15, 5), sharey=True)
    colors = ['red', 'blue']
    names = [
        n.replace("DGE/", "").replace("_contrast.csv","").replace(".toptable_clean.ALL_contrast.mark_seqc.header_added.csv","")
        for n in file_labels
    ]
    
    x = np.array(datasets[0])
    p_values = np.array(datasets[1])
    # To avoid math error for p-value 0, replace non-positive values with a tiny positive number.
    p_values = np.where(p_values <= 0, 1e-310, p_values)
    y = -np.log10(p_values)
    x = -np.log10(x)
    axes[0].scatter(x, y, color=colors[0], s=10)
    axes[0].set_ylabel(f"{names[1]}-pvalues")
    axes[0].set_xlabel("DEGW-pvalues")

    x = np.array(datasets[0])
    p_values = np.array(datasets[2])
    # To avoid math error for p-value 0, replace non-positive values with a tiny positive number.
    p_values = np.where(p_values <= 0, 1e-310, p_values)
    y = -np.log10(p_values)
    x = -np.log10(x)
    axes[1].scatter(x, y, color=colors[1], s=10)
    axes[1].set_ylabel(f"{names[2]}-pvalues")
    axes[1].set_xlabel("DEGW-pvalues")
    
    plt.tight_layout()
    plt.savefig("pvalues_comparisons.png", transparent=None, dpi='figure', format=None,
        metadata=None, bbox_inches=None, pad_inches=0.1,
        facecolor='auto', edgecolor='auto', backend=None
       )

def plot_lines_data(datasets, file_labels):
    names = [
        n.replace("DGE/", "").replace("_contrast.csv","").replace(".toptable_clean.ALL_contrast.mark_seqc.header_added.csv","")
        for n in file_labels
    ]
    
    plt.figure(figsize=(10, 6))
    colors = ['red', 'blue', 'green']
    
    for i, values in enumerate(datasets):
        if not values:
            continue
        x = np.arange(len(values))
        p_values = np.array(values)
        # Replace non-positive p-values to avoid math errors in log transformation.
        p_values = np.where(p_values <= 0, 1e-310, p_values)
        y = -np.log10(p_values)
        plt.plot(x, y, color=colors[i], label=names[i])
    
    plt.xlabel("Index")
    plt.ylabel("-log10(p-value)")
    plt.title("Comparison of p-values")
    plt.legend()
    plt.tight_layout()
    plt.savefig("pvalues_lines.png", transparent=None, dpi='figure', format=None,
        metadata=None, bbox_inches=None, pad_inches=0.1,
        facecolor='auto', edgecolor='auto', backend=None
       )


def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py file1.csv file2.csv file3.csv")
        sys.exit(1)
    
    file_paths = sys.argv[1:]
    datasets = []
    file_labels = []
    
    for idx, file_path in enumerate(file_paths, start=1):
        values = process_csv(file_path)
        datasets.append(values)
        file_labels.append(f"File {idx}: {file_path}")
    
    plot_data(datasets, file_labels)
    plot_lines_data(datasets, file_labels)

    datasets = []
    for idx, file_path in enumerate(file_paths, start=1):
        values = process_csv_with_key(file_path)
        datasets.append(values)
    keys_by_dataset = [set(d.keys()) for d in datasets]
    shared_keys = keys_by_dataset[0].intersection(keys_by_dataset[1]).intersection(keys_by_dataset[2])
    datasets = [
        [
            d[k] for k in shared_keys
        ]
        for d in datasets
    ]

    scatter_vs(datasets, file_labels)

if __name__ == '__main__':
    main()
