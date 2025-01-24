import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from typing import Optional, List, Union

def plot_data(data, figsize=(18, 6), title="Data Visualization"):
    plt.figure(figsize=figsize)
    plt.plot(data)
    plt.title(title, pad=20, fontsize=14)
    plt.xlabel('X-axis', fontsize=12)
    plt.ylabel('Y-axis', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
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

def plot_streams_distribution(df):
    plt.figure(figsize=(12, 6))
    sns.histplot(data=df, x='streams', bins=50, log_scale=True)
    plt.title('Distribuição de Streams (Escala Log)')
    plt.show()

def plot_feature_correlation_matrix(data, features: Optional[List[str]] = None):
    if features is None:
        features = ['danceability', 'energy', 'valence', 'bpm', 'streams']
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(data[features].corr(), annot=True, cmap='coolwarm')
    plt.title('Feature Correlation Matrix')
    plt.show()

def plot_top_artists(df: pd.DataFrame, n: int = 10):
    plt.figure(figsize=(15, 8))
    top_artists = df['artist(s)_name'].value_counts().head(n)
    sns.barplot(x=top_artists.values, y=top_artists.index, palette='viridis')
    plt.title('Top Artistas por Número de Músicas', pad=20, fontsize=14)
    plt.xlabel('Número de Músicas', fontsize=12)
    plt.ylabel('Artista', fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_streams_by_year(df: pd.DataFrame):
    plt.figure(figsize=(15, 8))
    yearly_streams = df.groupby(df['released_date'].dt.year)['streams'].mean()
    sns.lineplot(x=yearly_streams.index, y=yearly_streams.values, marker='o')
    plt.title('Média de Streams por Ano', pad=20, fontsize=14)
    plt.xlabel('Ano', fontsize=12)
    plt.ylabel('Média de Streams', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()