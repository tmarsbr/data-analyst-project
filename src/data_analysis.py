import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple

def get_top_artists(data: pd.DataFrame, n: int = 10) -> pd.Series:
    return data['artist(s)_name'].value_counts().head(n)

def calculate_audio_features_stats(data: pd.DataFrame) -> Dict[str, float]:
    features = ['danceability', 'energy', 'valence', 'bpm']
    stats = {}
    for feature in features:
        if feature in data.columns:
            stats[feature] = {
                'mean': data[feature].mean(),
                'median': data[feature].median(),
                'std': data[feature].std()
            }
    return stats

def analyze_streams_by_year(data: pd.DataFrame) -> pd.Series:
    return data.groupby(data['released_date'].dt.year)['streams'].mean()

def calculate_correlation(df, features):
    correlation = df[features].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
    plt.title('Matriz de Correlação')
    plt.tight_layout()
    plt.show()

def get_basic_stats(df, columns=None):
    """Obtém estatísticas básicas para colunas especificadas."""
    if columns is None:
        columns = df.select_dtypes(include=['float64', 'int64']).columns
    return df[columns].describe()

def analyze_temporal_patterns(df, date_column, value_column):
    """Analisa padrões ao longo do tempo."""
    return df.groupby(date_column)[value_column].agg(['mean', 'count', 'sum'])

def calculate_collaboration_metrics(df):
    """Calcula métricas sobre colaborações de artistas."""
    df['collab_count'] = df['artist(s)_name'].str.count(',') + 1
    return df.groupby('released_year')['collab_count'].mean()