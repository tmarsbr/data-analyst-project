import matplotlib.pyplot as plt
import seaborn as sns

def plot_streaming_distribution(df):
    """Plot the distribution of streams."""
    plt.figure(figsize=(12, 6))
    sns.histplot(data=df, x='streams', bins=50, log_scale=True, color='skyblue')
    plt.title('Distribuição de Streams (Escala Log)', fontsize=16, pad=20)
    plt.xlabel('Streams', fontsize=14)
    plt.ylabel('Frequência', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
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
    sns.boxplot(data=df, x='ano', y='streams', palette='viridis')
    plt.title('Distribuição de Streams por Ano', fontsize=16, pad=20)
    plt.xlabel('Ano', fontsize=14)
    plt.ylabel('Streams', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_danceability_vs_energy(df):
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=df, x='danceability_%', y='energy_%', hue='in_spotify_charts', size='streams', palette='viridis', sizes=(20, 200), alpha=0.7)
    plt.title('Danceability vs Energy', fontsize=16, pad=20)
    plt.xlabel('Danceability (%)', fontsize=14)
    plt.ylabel('Energy (%)', fontsize=14)
    plt.legend(title='In Spotify Charts', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_top_songs_by_streams(df):
    top_songs = df.sort_values('streams', ascending=False).head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(x='streams', y='track_name', data=top_songs)
    plt.title('Top 10 Músicas por Streams')
    plt.show()

def plot_correlation_matrix(df):
    features_numericas = ['streams', 'danceability_%', 'energy_%', 'valence_%', 'in_spotify_charts']
    correlation = df[features_numericas].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
    plt.title('Matriz de Correlação', fontsize=16, pad=20)
    plt.tight_layout()
    plt.show()

def plot_releases_per_month(df):
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='mes', palette='viridis')
    plt.title('Distribuição de Lançamentos por Mês', fontsize=16, pad=20)
    plt.xlabel('Mês', fontsize=14)
    plt.ylabel('Número de Lançamentos', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def create_visualizations(df):
    """Create all visualizations."""
    plt.style.use('seaborn')
    
    plot_streaming_distribution(df)
    plot_feature_relationships(df)
    plot_yearly_streams(df)
    plot_danceability_vs_energy(df)
    plot_top_songs_by_streams(df)
    plot_correlation_matrix(df)
    plot_releases_per_month(df)

if __name__ == "__main__":
    from data_preprocessing import load_data, clean_spotify_data, normalize_audio_features
    
    # Load and preprocess data
    df = load_data('spotify_songs.csv')
    df = clean_spotify_data(df)
    df = normalize_audio_features(df)
    
    # Create visualizations
    create_visualizations(df)
