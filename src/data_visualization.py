import matplotlib.pyplot as plt
import seaborn as sns

def plot_streaming_distribution(df):
    """Plot the distribution of streams."""
    plt.figure(figsize=(12, 6))
    sns.histplot(data=df, x='streams', bins=50, log_scale=True)
    plt.title('Distribuição de Streams (Escala Log)')
    plt.show()

def plot_feature_relationships(df):
    """Plot relationships between audio features."""
    # Create a correlation plot between audio features
    plt.figure(figsize=(12, 6))
    
    # Using the correct column names from the DataFrame
    audio_features = ['danceability_%', 'energy_%', 'valence_%', 
                     'acousticness_%', 'instrumentalness_%', 
                     'liveness_%', 'speechiness_%']
    
    correlation_matrix = df[audio_features].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlação entre Features de Áudio')
    plt.xticks(rotation=45)
    plt.yticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Scatter plot with the correct column names
    plt.figure(figsize=(12, 6))
    sns.scatterplot(
        data=df,
        x='danceability_%',
        y='energy_%',
        size='streams',
        sizes=(20, 200),
        alpha=0.6
    )
    plt.title('Danceability vs Energy')
    plt.show()

def plot_yearly_streams(df):
    """Plot distribution of streams by year."""
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='ano', y='streams')
    plt.title('Distribuição de Streams por Ano')
    plt.xticks(rotation=45)
    plt.show()

def create_visualizations(df):
    """Create all visualizations."""
    plt.style.use('seaborn')
    
    plot_streaming_distribution(df)
    plot_feature_relationships(df)
    plot_yearly_streams(df)

if __name__ == "__main__":
    from data_preprocessing import load_data, clean_spotify_data, normalize_audio_features
    
    # Load and preprocess data
    df = load_data('spotify_songs.csv')
    df = clean_spotify_data(df)
    df = normalize_audio_features(df)
    
    # Create visualizations
    create_visualizations(df)
