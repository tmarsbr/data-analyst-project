import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional

def plot_data(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data)
    plt.title('Data Visualization')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid()
    plt.show()

def create_histogram(data, bins=10):
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, alpha=0.7, color='blue')
    plt.title('Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid()
    plt.show()

def generate_scatter_plot(x, y):
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, alpha=0.7, color='red')
    plt.title('Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid()
    plt.show()

def plot_streams_distribution(data, log_scale: bool = True):
    plt.figure(figsize=(12, 6))
    if log_scale:
        sns.histplot(np.log10(data['streams']), bins=50)
        plt.xlabel('Log10(Streams)')
    else:
        sns.histplot(data['streams'], bins=50)
        plt.xlabel('Streams')
    plt.title('Distribution of Song Streams')
    plt.ylabel('Count')
    plt.grid(True)
    plt.show()

def plot_feature_correlation_matrix(data, features: Optional[List[str]] = None):
    if features is None:
        features = ['danceability', 'energy', 'valence', 'bpm', 'streams']
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(data[features].corr(), annot=True, cmap='coolwarm')
    plt.title('Feature Correlation Matrix')
    plt.show()