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
    """
    Calcula e visualiza a matriz de correlação para as características especificadas.
    
    Args:
        df: DataFrame com os dados
        features: Lista de características para análise de correlação
    """
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

def identify_viral_potential(df: pd.DataFrame, 
                           energy_threshold: float = 70,
                           dance_threshold: float = 75) -> pd.DataFrame:
    """
    Identifica músicas com alto potencial viral baseado nos critérios descobertos.
    
    Args:
        df: DataFrame com dados do Spotify
        energy_threshold: Limite mínimo de energia (%)
        dance_threshold: Limite mínimo de dançabilidade (%)
    
    Returns:
        DataFrame com músicas de alto potencial viral
    """
    viral_songs = df[
        (df['energy_%'] > energy_threshold) & 
        (df['danceability_%'] > dance_threshold)
    ].sort_values('streams', ascending=False)
    
    return viral_songs[['track_name', 'artist(s)_name', 'streams', 
                       'energy_%', 'danceability_%', 'in_spotify_charts']]

def get_monthly_performance_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula estatísticas de performance por mês de lançamento.
    """
    monthly_stats = df.groupby('mes').agg({
        'streams': ['mean', 'median', 'count'],
        'in_spotify_charts': 'mean'
    }).round(2)
    
    monthly_stats.columns = ['avg_streams', 'median_streams', 
                           'release_count', 'avg_chart_position']
    return monthly_stats