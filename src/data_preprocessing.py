import pandas as pd
from typing import Optional

def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()  # Remove missing values
    df = df.reset_index(drop=True)  # Reset index after dropping
    return df

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # Example transformation: converting a column to datetime
    if 'date_column' in df.columns:
        df['date_column'] = pd.to_datetime(df['date_column'])
    return df

def clean_spotify_data(df: pd.DataFrame) -> pd.DataFrame:
    # Convert streams to numeric, removing commas
    df['streams'] = pd.to_numeric(df['streams'].str.replace(',', ''), errors='coerce')
    
    # Clean artist names
    df['artist(s)_name'] = df['artist(s)_name'].str.strip()
    
    # Convert release_date to datetime
    df['released_date'] = pd.to_datetime(df['released_date'])
    
    return df

def normalize_audio_features(df: pd.DataFrame) -> pd.DataFrame:
    # Normalize features between 0 and 1
    features = ['danceability', 'energy', 'valence', 'bpm']
    for feature in features:
        if feature in df.columns:
            df[feature] = df[feature] / 100
    return df