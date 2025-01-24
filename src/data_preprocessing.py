import pandas as pd
import numpy as np
from typing import Optional

def load_data(file_path: str) -> pd.DataFrame:
    """Load data from a CSV file."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find file at path: {file_path}")

def check_missing_values(df: pd.DataFrame) -> pd.Series:
    """Check for missing values in the DataFrame."""
    return df.isnull().sum()

def get_basic_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Get basic statistics of the DataFrame."""
    return df.describe()

def get_top_artists(df: pd.DataFrame, top_n: int = 10) -> pd.Series:
    """Get the top N artists by count."""
    return df['artist(s)_name'].value_counts().head(top_n)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove missing values and reset index."""
    df = df.dropna()  # Remove missing values
    df = df.reset_index(drop=True)  # Reset index after dropping
    return df

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Example transformation: converting a column to datetime."""
    if 'date_column' in df.columns:
        df['date_column'] = pd.to_datetime(df['date_column'])
    return df

def clean_spotify_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and prepare Spotify dataset."""
    try:
        # Handle missing values in critical columns
        df = df.dropna(subset=['artist(s)_name', 'track_name'])
        
        # Convert streams to numeric and handle missing values
        df['streams'] = pd.to_numeric(df['streams'].str.replace(',', ''), errors='coerce')
        
        # Clean text columns
        text_columns = ['track_name', 'artist(s)_name']
        if 'album_type' in df.columns:
            text_columns.append('album_type')
        df[text_columns] = df[text_columns].apply(lambda x: x.str.strip())
        
        # Handle missing values and commas in 'in_shazam_charts'
        if 'in_shazam_charts' in df.columns:
            df['in_shazam_charts'] = (
                pd.to_numeric(df['in_shazam_charts'].str.replace(',', ''), errors='coerce')
                .fillna(0)
                .astype(int)
            )
        
        df['key'] = df['key'].fillna('Unknown')
        
        # Process release date
        df = _process_release_date(df)
        
        # Sort and add time features
        df = df.sort_values('streams', ascending=False).reset_index(drop=True)
        df['ano'] = df['released_date'].dt.year
        df['mes'] = df['released_date'].dt.month
        
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
        features = ['danceability_%', 'energy_%', 'valence_%', 'bpm']
    
    for feature in features:
        if feature in df.columns and df[feature].dtype in ['int64', 'float64']:
            df[feature] = df[feature] / 100
    
    return df

# Example usage
if __name__ == "__main__":
    # Load the data
    file_path = 'spotify_songs.csv'  # Replace with your actual file path
    df = load_data(file_path)
    
    # Clean the data
    df = clean_spotify_data(df)
    
    # Normalize audio features
    df = normalize_audio_features(df)
    
    # Verify the data
    print("\nMissing values after preprocessing:")
    print(df.isnull().sum())
    print("\nFirst few rows of the dataset:")
    print(df.head())