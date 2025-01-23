def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def clean_data(df):
    df = df.dropna()  # Remove missing values
    df = df.reset_index(drop=True)  # Reset index after dropping
    return df

def transform_data(df):
    # Example transformation: converting a column to datetime
    if 'date_column' in df.columns:
        df['date_column'] = pd.to_datetime(df['date_column'])
    return df