import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_metric_vs_noise(root, list_of_datasets, legend_ncols=3):
    csv_path = root  + 'results_noise.csv'
    fig_path = root + 'noise.pdf'

    # Read CSV
    df = pd.read_csv(csv_path)
    df = df[df['dataset'].isin(list_of_datasets)]
    df.loc[~df['dataset'].str.startswith('ogbl'), 'metric_value'] = df['auc_value']

    # Ensure required columns exist
    required_cols = {'dataset', 'metric_value', 'noise_std', 'noise_drop'}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"CSV must contain columns: {required_cols}")

    # Get unique datasets
    datasets = sorted(df['dataset'].unique())
    
    # Create single figure and axis
    plt.figure(figsize=(8, 8))
    
    for dataset in datasets:
        subset = df[df['dataset'] == dataset].sort_values(by='noise_std')
        plt.plot(subset['noise_std'], subset['metric_value'], marker='o', label=dataset)

    #plt.title(f"Metric vs Noise Std (Noise Drop: {noise_drop_value})")
    plt.xlabel(r"Noise $\sigma$", fontsize=20)
    plt.ylabel("Metric Value", fontsize=20)
    plt.ylim(0.8, 1.0)
    plt.yticks(np.arange(0.8, 1.01, 0.05))      
    plt.xticks(fontsize=16)
    plt.xticks(np.arange(0.0, 0.201, 0.05))      
    plt.yticks(fontsize=16)

    # Move legend below the plot
    plt.legend(loc='upper center',
               bbox_to_anchor=(0.5, -0.2),
               ncol=legend_ncols,
               frameon=False, fontsize=18)

    # Adjust layout to make space below
    plt.tight_layout(rect=[0, 0.1, 1, 1])  # leave space for legend
    plt.savefig(fig_path)
    plt.show()

root = 'D:/Indranil/JRF/Submission/IEEE_multiheaded/codebase/affNet/results/'
list_of_datasets = ['Cora', 'CiteSeer', 'Texas', 'Wisconsin', 'Squirrel', 
                    'Chameleon', 'Photo', 'ogbl-ppa', 'ogbl-collab', 'ogbl-citation2']
plot_metric_vs_noise(root, list_of_datasets)
