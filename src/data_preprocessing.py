import pandas as pd
import numpy as np
from typing import Optional

def load_data(file_path: str) -> pd.DataFrame:
    """Load data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded dataset
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find file at path: {file_path}")

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
    """Clean and prepare Spotify dataset.
    
    Args:
        df (pd.DataFrame): Raw Spotify dataset
        
    Returns:
        pd.DataFrame: Cleaned dataset with proper data types and derived columns
    """
    try:
        # Handle missing values
        df = df.dropna(subset=['streams', 'artist(s)_name', 'track_name'])
        
        # Convert streams to numeric using a more robust method
        df['streams'] = pd.to_numeric(df['streams'].astype(str).str.replace(',', ''), errors='coerce')
        
        # Clean text columns with improved handling - only process columns that exist
        text_columns = ['track_name', 'artist(s)_name']
        if 'album_type' in df.columns:
            text_columns.append('album_type')
        df[text_columns] = df[text_columns].apply(lambda x: x.str.strip() if x.dtype == 'object' else x)
        
        # Handle released_date conversion
        df = _process_release_date(df)
        
        # Sort and add time features
        df = df.sort_values('streams', ascending=False).reset_index(drop=True)
        df['ano'] = df['released_date'].dt.year
        df['mes'] = df['released_date'].dt.month
        
        print("\n✅ Pré-processamento concluído!")
        return df
        
    except Exception as e:
        print(f"Error during data cleaning: {str(e)}")
        raise

def _process_release_date(df: pd.DataFrame) -> pd.DataFrame:
    """Helper function to process release date information."""
    if 'released_date' not in df.columns:
        if all(col in df.columns for col in ['released_year', 'released_month', 'released_day']):
            df['released_date'] = pd.to_datetime(
                {
                    'year': df['released_year'],
                    'month': df['released_month'],
                    'day': df['released_day']
                },
                errors='coerce'
            )
        else:
            raise KeyError("Required date columns not found")
    else:
        df['released_date'] = pd.to_datetime(df['released_date'], errors='coerce')
    
    if df['released_date'].isna().any():
        print("Warning: NaT values detected in 'released_date'")
    
    return df

def normalize_audio_features(df: pd.DataFrame, features: Optional[list] = None) -> pd.DataFrame:
    """Normalize audio features to range [0,1]."""
    if features is None:
        features = ['danceability', 'energy', 'valence', 'bpm']
    
    for feature in features:
        if feature in df.columns and df[feature].dtype in ['int64', 'float64']:
            df[feature] = df[feature] / 100
    
    return df

# Remove the code execution at module level
# This should be done in the main script instead