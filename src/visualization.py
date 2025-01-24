import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from typing import Optional, List, Union
from matplotlib import ticker  # Add this import

def plot_data(data, figsize=(18, 6), title="Data Visualization"):
    plt.style.use('seaborn')  # Aplicando um tema mais moderno
    plt.figure(figsize=figsize)
    plt.plot(data)
    plt.title(title, pad=20, fontsize=16)
    plt.xlabel('X-axis', fontsize=14)
    plt.ylabel('Y-axis', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def create_histogram(data, bins=20, title='Histograma'):
    plt.style.use('seaborn')
    plt.figure(figsize=(12, 6))
    sns.histplot(data, bins=bins, kde=True, color='skyblue')
    plt.title(title, fontsize=16, pad=20)
    plt.xlabel('Valores', fontsize=14)
    plt.ylabel('Frequência', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def create_scatterplot(df, x, y, hue=None, title='Scatter Plot'):
    plt.style.use('seaborn')
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=df, x=x, y=y, hue=hue, palette='viridis', s=100, alpha=0.7)
    plt.title(title, fontsize=16, pad=20)
    plt.xlabel(x, fontsize=14)
    plt.ylabel(y, fontsize=14)
    plt.legend(title=hue, fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def create_barplot(df, x, y, title='Bar Plot'):
    plt.style.use('seaborn')
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x=x, y=y, palette='viridis')
    plt.title(title, fontsize=16, pad=20)
    plt.xlabel(x, fontsize=14)
    plt.ylabel(y, fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def generate_scatter_plot(x, y):
    plt.style.use('seaborn')
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, alpha=0.7, color='red')
    plt.title('Scatter Plot', fontsize=16, pad=20)
    plt.xlabel('X-axis', fontsize=14)
    plt.ylabel('Y-axis', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_streams_distribution(df):
    plt.style.use('seaborn-v0_8-whitegrid')  # Fundo branco para PPT
    plt.figure(figsize=(16, 9))  # Formato 16:9 para slides
    
    sns.histplot(data=df, x='streams', bins=50, log_scale=True, 
                 color='#2980b9', edgecolor='white', linewidth=1.5)
    
    # Título explicativo
    plt.title('Distribuição de Streams: 99% dos dados abaixo de 1 Bilhão\n(Escala Logarítmica)', 
              fontsize=22, pad=25, fontweight='bold', color='#2c3e50')
    
    # Eixos simplificados
    plt.xlabel('Streams', fontsize=18, labelpad=15, color='#34495e')
    plt.ylabel('Contagem de Músicas', fontsize=18, labelpad=15, color='#34495e')
    
    # Formatação profissional
    plt.xticks([10**4, 10**6, 10**8, 10**9], 
               ['10 mil', '1 milhão', '100 milhões', '1 bilhão'], 
               fontsize=14)
    
    # Destaque no pico
    max_count = df['streams'].value_counts().max()
    plt.annotate(f'Pico: {max_count//1000}K músicas\nentre 10-100 milhões',
                 xy=(10**7, max_count), 
                 xytext=(10**8, max_count*0.8),
                 arrowprops=dict(facecolor='#e74c3c', shrink=0.05),
                 fontsize=14, color='#e74c3c')
    
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    plt.savefig('streams_distribution.png', dpi=300, bbox_inches='tight')  # Para exportar
    plt.show()

def plot_feature_correlation_matrix(data, features: Optional[List[str]] = None):
    if features is None:
        features = ['danceability', 'energy', 'valence', 'bpm', 'streams']
    
    plt.style.use('seaborn')
    plt.figure(figsize=(10, 8))
    sns.heatmap(data[features].corr(), annot=True, cmap='coolwarm', center=0)
    plt.title('Feature Correlation Matrix', fontsize=16, pad=20)
    plt.tight_layout()
    plt.show()

def plot_top_artists(df: pd.DataFrame, n: int = 10):
    plt.style.use('seaborn')
    plt.figure(figsize=(15, 8))
    top_artists = df['artist(s)_name'].value_counts().head(n)
    sns.barplot(x=top_artists.values, y=top_artists.index, palette='viridis')
    plt.title('Top Artistas por Número de Músicas', fontsize=16, pad=20)
    plt.xlabel('Número de Músicas', fontsize=14)
    plt.ylabel('Artista', fontsize=14)
    plt.tight_layout()
    plt.show()

def plot_streams_by_year(df: pd.DataFrame):
    plt.style.use('seaborn-v0_8-white')
    plt.figure(figsize=(18, 9))
    
    # Dados agregados
    yearly_data = df.groupby(df['released_date'].dt.year)['streams'].agg(['sum', 'mean'])
    years = yearly_data.index.astype(int)
    
    # Gráfico de área para visualização suave
    plt.fill_between(years, yearly_data['sum']/1e9, alpha=0.3, color='#3498db')
    sns.lineplot(x=years, y=yearly_data['sum']/1e9, color='#2980b9', linewidth=4, 
                 label='Streams Totais (Bilhões)')
    
    # Destaque no último ano
    last_year = years[-1]
    plt.scatter(last_year, yearly_data['sum'].iloc[-1]/1e9, s=300, 
                color='#e74c3c', zorder=5, edgecolor='black')
    plt.annotate(f'+{((yearly_data["sum"].iloc[-1]/yearly_data["sum"].iloc[-2])-1)*100:.0f}% vs anterior', 
                 (last_year, yearly_data['sum'].iloc[-1]/1e9),
                 textcoords="offset points", 
                 xytext=(0,15), 
                 ha='center', 
                 fontsize=14,
                 color='#e74c3c')
    
    # Formatação profissional
    plt.title('Crescimento Explosivo de Streams: 2019-2023', 
              fontsize=24, pad=30, fontweight='bold', color='#2c3e50')
    plt.xlabel('', fontsize=18)
    plt.ylabel('Bilhões de Streams', fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    
    plt.grid(True, axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig('streams_growth.png', dpi=300)
    plt.show()

def plot_correlation_matrix(df, columns=None):
    """Plota a matriz de correlação para colunas selecionadas."""
    if columns is None:
        columns = df.select_dtypes(include=['float64', 'int64']).columns
    corr_matrix = df[columns].corr()
    plt.style.use('seaborn')
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix', fontsize=16, pad=20)
    plt.tight_layout()
    plt.show()

def plot_top_items(df, value_col, label_col, n=10, title=None):
    """Plota os top N itens com base em uma coluna de valor."""
    plt.style.use('seaborn')
    plt.figure(figsize=(12, 6))
    top_items = df.nlargest(n, value_col)
    sns.barplot(x=value_col, y=label_col, data=top_items, palette='viridis')
    plt.title(title or f'Top {n} {label_col} by {value_col}', fontsize=16, pad=20)
    plt.xlabel(value_col, fontsize=14)
    plt.ylabel(label_col, fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_danceability_vs_energy(df):
    plt.style.use('dark_background')  # Tema escuro para contraste
    plt.figure(figsize=(18, 10))
    
    # Cores neon para apresentações
    scatter = sns.scatterplot(
        data=df,
        x='danceability_%',
        y='energy_%',
        size='streams',
        hue='in_spotify_charts',
        sizes=(50, 800),
        palette='viridis',
        alpha=0.9,
        edgecolor='white',
        linewidth=0.5
    )
    
    # Título narrativo
    plt.title('Músicas Mais Populares: Alta Energia + Alta Dançabilidade', 
              fontsize=24, pad=30, fontweight='bold', color='#ecf0f1')
    
    # Eixos com destaque
    plt.xlabel('Dançabilidade (%)', fontsize=18, color='#bdc3c7')
    plt.ylabel('Energia (%)', fontsize=18, color='#bdc3c7')
    
    # Quadrante destacado
    plt.axhspan(60, 90, xmin=0.6, xmax=1, alpha=0.2, color='#2ecc71')
    plt.text(72, 75, 'Músicas Virais', fontsize=16, color='#2ecc71', 
             ha='center', va='center')
    
    # Legendas flutuantes
    plt.legend(
        title='Posição nos Charts\n(e Tamanho = Streams)',
        title_fontsize=14,
        fontsize=12,
        frameon=True,
        framealpha=0.9,
        loc='lower left'
    )
    
    plt.tight_layout()
    plt.savefig('dance_energy.png', dpi=300, transparent=True)  # Fundo transparente
    plt.show()

def plot_releases_by_month(df):
    plt.figure(figsize=(14, 7))
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df['month_name'] = df['mes'].map(lambda x: month_order[x-1])
    df_month = df.groupby('month_name').size().reset_index(name='count')
    df_month['month_name'] = pd.Categorical(df_month['month_name'], categories=month_order, ordered=True)
    df_month = df_month.sort_values('month_name')
    
    bar = sns.barplot(x='month_name', y='count', data=df_month, palette='plasma', edgecolor='black')
    bar.set_title('Number of Releases by Month', fontsize=20)
    bar.set_xlabel('Month', fontsize=15)
    bar.set_ylabel('Number of Releases', fontsize=15)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('releases_by_month.png', dpi=300, bbox_inches='tight')
    plt.show()

def plot_streams_evolution(df):
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(18, 9))
    
    # Dados processados
    years = df['released_year'].unique()
    total_streams = df.groupby('released_year')['streams'].sum() / 1e9  # Em bilhões
    avg_streams = df.groupby('released_year')['streams'].mean() / 1e6   # Em milhões

    # Gráfico principal
    ax = sns.barplot(x=years, y=total_streams, color='#3498db', alpha=0.9)
    plt.title('Crescimento de Streams: 2017-2023\n(Total vs Média por Música)', 
              fontsize=22, pad=25, fontweight='bold', color='#2c3e50')

    # Linha de média
    ax2 = ax.twinx()
    sns.lineplot(x=years, y=avg_streams, color='#e74c3c', marker='o', 
                 markersize=10, linewidth=3, ax=ax2)

    # Customização
    ax.set_ylabel('Streams Totais (Bilhões)', fontsize=16, color='#3498db')
    ax2.set_ylabel('Média por Música (Milhões)', fontsize=16, color='#e74c3c')
    ax.tick_params(axis='y', colors='#3498db')
    ax2.tick_params(axis='y', colors='#e74c3c')

    # Destaques e anotações
    max_year = total_streams.idxmax()
    plt.annotate(f'+{((total_streams[max_year]/total_streams[max_year-1])-1)*100:.0f}% vs {max_year-1}',
                 xy=(max_year, total_streams[max_year]),
                 xytext=(max_year-0.5, total_streams[max_year]*0.8),
                 arrowprops=dict(arrowstyle='->', color='#2c3e50', lw=2),
                 fontsize=14)

    # Grade e formatação
    plt.xticks(fontsize=14)
    plt.grid(axis='x', visible=False)
    plt.tight_layout()
    plt.savefig('streams_evolution.png', dpi=300, bbox_inches='tight')
    plt.show()

def plot_log_streams_distribution(df):
    plt.style.use('seaborn-v0_8-dark')
    plt.figure(figsize=(16, 8))
    
    # Histograma com KDE
    hist = sns.histplot(df['streams'], bins=50, log_scale=True, 
                        color='#27ae60', edgecolor='#2c3e50', 
                        kde=True, kde_kws={'color': '#c0392b', 'lw': 3})
    
    # Customização
    plt.title('Distribuição de Popularidade: 95% das Músicas têm menos de 100M Streams', 
              fontsize=20, pad=25, color='white', fontweight='bold')
    
    # Eixos explicativos
    plt.xlabel('Streams (Escala Logarítmica)', fontsize=16, color='white')
    plt.ylabel('Número de Músicas', fontsize=16, color='white')
    
    # Marcadores estratégicos
    plt.xticks([10**4, 10**5, 10**6, 10**7, 10**8, 10**9],
               ['10 mil', '100 mil', '1 milhão', '10 milhões', '100 milhões', '1 bilhão'], 
               rotation=45, fontsize=12)
    
    # Destaques gráficos
    plt.axvspan(10**4, 10**6, alpha=0.1, color='#f1c40f')
    plt.text(3*10**5, plt.ylim()[1]*0.8, 'Músicas de\nBaixa Visibilidade', 
             ha='center', color='#f1c40f', fontsize=14)
    
    plt.axvline(x=10**8, color='#e74c3c', linestyle='--', alpha=0.7)
    plt.text(1.2*10**8, plt.ylim()[1]*0.6, 'Top 5% de\nViralidade', 
             color='#e74c3c', fontsize=14)

    # Grade e cor de fundo
    plt.grid(True, which='both', linestyle=':', color='white', alpha=0.3)
    plt.gca().set_facecolor('#34495e')
    plt.tight_layout()
    plt.savefig('log_distribution.png', dpi=300, transparent=True)
    plt.show()