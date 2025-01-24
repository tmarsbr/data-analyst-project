import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from typing import Optional, List, Union
from matplotlib import ticker

def plot_data(data, figsize=(18, 6), title="Visualização dos Dados"):
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=figsize)
    plt.plot(data, color='#1f77b4', linewidth=2)
    plt.title(title, pad=20, fontsize=18, fontweight='bold')
    plt.xlabel('Eixo X', fontsize=14)
    plt.ylabel('Eixo Y', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def create_histogram(data, bins=20, title='Histograma'):
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 6))
    sns.histplot(data, bins=bins, kde=True, color='#1f77b4', edgecolor='black')
    plt.title(title, fontsize=18, pad=20, fontweight='bold')
    plt.xlabel('Valores', fontsize=14)
    plt.ylabel('Frequência', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def create_scatterplot(df, x, y, hue=None, title='Scatter Plot'):
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=df, x=x, y=y, hue=hue, palette='viridis', s=100, alpha=0.7, edgecolor='black')
    plt.title(title, fontsize=18, pad=20, fontweight='bold')
    plt.xlabel(x, fontsize=14)
    plt.ylabel(y, fontsize=14)
    plt.legend(title=hue, fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def create_barplot(df, x, y, title='Bar Plot'):
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x=x, y=y, palette='viridis', edgecolor='black')
    plt.title(title, fontsize=18, pad=20, fontweight='bold')
    plt.xlabel(x, fontsize=14)
    plt.ylabel(y, fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def generate_scatter_plot(x, y):
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, alpha=0.7, color='#1f77b4', edgecolor='black')
    plt.title('Scatter Plot', fontsize=18, pad=20, fontweight='bold')
    plt.xlabel('X-axis', fontsize=14)
    plt.ylabel('Y-axis', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_streams_distribution(df):
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(16, 9))
    sns.histplot(data=df, x='streams', bins=50, log_scale=True, color='#1f77b4', edgecolor='black')
    plt.title('Distribuição de Streams: 99% dos dados abaixo de 1 Bilhão\n(Escala Logarítmica)', fontsize=22, pad=25, fontweight='bold')
    plt.xlabel('Streams', fontsize=18, labelpad=15)
    plt.ylabel('Contagem de Músicas', fontsize=18, labelpad=15)
    plt.xticks([10**4, 10**6, 10**8, 10**9], ['10 mil', '1 milhão', '100 milhões', '1 bilhão'], fontsize=14)
    max_count = df['streams'].value_counts().max()
    plt.annotate(f'Pico: {max_count//1000}K músicas\nentre 10-100 milhões', xy=(10**7, max_count), xytext=(10**8, max_count*0.8), arrowprops=dict(facecolor='#e74c3c', shrink=0.05), fontsize=14, color='#e74c3c')
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    plt.savefig('streams_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()

def plot_feature_correlation_matrix(data, features: Optional[List[str]] = None):
    if features is None:
        features = ['danceability', 'energy', 'valence', 'bpm', 'streams']
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(10, 8))
    sns.heatmap(data[features].corr(), annot=True, cmap='coolwarm', center=0, linewidths=0.5, linecolor='black')
    plt.title('Feature Correlation Matrix', fontsize=18, pad=20, fontweight='bold')
    plt.tight_layout()
    plt.show()

def plot_top_artists(df: pd.DataFrame, n: int = 10):
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(15, 8))
    top_artists = df['artist(s)_name'].value_counts().head(n)
    sns.barplot(x=top_artists.values, y=top_artists.index, palette='viridis', edgecolor='black')
    plt.title('Top Artistas por Número de Músicas', fontsize=18, pad=20, fontweight='bold')
    plt.xlabel('Número de Músicas', fontsize=14)
    plt.ylabel('Artista', fontsize=14)
    plt.tight_layout()
    plt.show()

def plot_streams_by_year(df: pd.DataFrame):
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(18, 9))
    yearly_data = df.groupby(df['released_date'].dt.year)['streams'].agg(['sum', 'mean'])
    years = yearly_data.index.astype(int)
    plt.fill_between(years, yearly_data['sum']/1e9, alpha=0.3, color='#1f77b4')
    sns.lineplot(x=years, y=yearly_data['sum']/1e9, color='#1f77b4', linewidth=4, label='Streams Totais (Bilhões)')
    last_year = years[-1]
    plt.scatter(last_year, yearly_data['sum'].iloc[-1]/1e9, s=300, color='#e74c3c', zorder=5, edgecolor='black')
    plt.annotate(f'+{((yearly_data["sum"].iloc[-1]/yearly_data["sum"].iloc[-2])-1)*100:.0f}% vs anterior', (last_year, yearly_data['sum'].iloc[-1]/1e9), textcoords="offset points", xytext=(0,15), ha='center', fontsize=14, color='#e74c3c')
    plt.title('Crescimento Explosivo de Streams: 2019-2023', fontsize=24, pad=30, fontweight='bold')
    plt.xlabel('', fontsize=18)
    plt.ylabel('Bilhões de Streams', fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.grid(True, axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig('streams_growth.png', dpi=300)
    plt.show()

def plot_correlation_matrix(df, columns=None):
    if columns is None:
        columns = df.select_dtypes(include=['float64', 'int64']).columns
    corr_matrix = df[columns].corr()
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, linewidths=0.5, linecolor='black')
    plt.title('Correlation Matrix', fontsize=18, pad=20, fontweight='bold')
    plt.tight_layout()
    plt.show()

def plot_top_items(df, value_col, label_col, n=10, title=None):
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 6))
    top_items = df.nlargest(n, value_col)
    sns.barplot(x=value_col, y=label_col, data=top_items, palette='viridis', edgecolor='black')
    plt.title(title or f'Top {n} {label_col} by {value_col}', fontsize=18, pad=20, fontweight='bold')
    plt.xlabel(value_col, fontsize=14)
    plt.ylabel(label_col, fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_danceability_vs_energy(df):
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(18, 10))
    scatter = sns.scatterplot(data=df, x='danceability_%', y='energy_%', size='streams', hue='in_spotify_charts', sizes=(50, 800), palette='viridis', alpha=0.9, edgecolor='black', linewidth=0.5)
    plt.title('Músicas Mais Populares: Alta Energia + Alta Dançabilidade', fontsize=24, pad=30, fontweight='bold')
    plt.xlabel('Dançabilidade (%)', fontsize=18)
    plt.ylabel('Energia (%)', fontsize=18)
    plt.axhspan(60, 90, xmin=0.6, xmax=1, alpha=0.2, color='#00FFFF')
    plt.text(72, 75, 'Músicas Virais', fontsize=16, color='#00FFFF', ha='center', va='center', fontweight='bold')
    plt.grid(False)
    ax = plt.gca()
    ax.xaxis.grid(False)
    ax.yaxis.grid(False)
    plt.legend(title='Posição nos Charts\n(e Tamanho = Streams)', title_fontsize=14, fontsize=12, frameon=True, framealpha=0.9, loc='lower left')
    plt.tight_layout()
    plt.savefig('dance_energy.png', dpi=300, transparent=True)
    plt.show()

def plot_releases_by_month(df):
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(14, 7))
    month_order = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    df['month_name'] = df['mes'].map(lambda x: month_order[x-1])
    df_month = df.groupby('month_name').size().reset_index(name='count')
    total = df_month['count'].sum()
    df_month['percentage'] = (df_month['count'] / total) * 100
    df_month['month_name'] = pd.Categorical(df_month['month_name'], categories=month_order, ordered=True)
    df_month = df_month.sort_values('month_name')
    bar = sns.barplot(x='month_name', y='count', data=df_month, hue='month_name', palette='plasma', edgecolor='black', legend=False)
    plt.title('Distribuição Mensal de Lançamentos Musicais', fontsize=18, pad=20, fontweight='bold')
    plt.xlabel('Mês', fontsize=14)
    plt.ylabel('', fontsize=14)
    plt.ylim(0, df_month['count'].max() * 1.15)
    for p, percentage in zip(bar.patches, df_month['percentage']):
        height = p.get_height()
        bar.annotate(f'{percentage:.1f}%', (p.get_x() + p.get_width() / 2., height), ha='center', va='bottom', xytext=(0, 15), textcoords='offset points', fontsize=10, color='black', fontweight='bold')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('releases_by_month.png', dpi=300, bbox_inches='tight')
    plt.show()

def plot_streams_evolution(df):
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(18, 9))
    years = df['released_year'].unique()
    total_streams = df.groupby('released_year')['streams'].sum() / 1e9
    avg_streams = df.groupby('released_year')['streams'].mean() / 1e6
    ax = sns.barplot(x=years, y=total_streams, color='#1f77b4', alpha=0.9, edgecolor='black')
    plt.title('Crescimento de Streams: 2017-2023\n(Total vs Média por Música)', fontsize=22, pad=25, fontweight='bold')
    ax2 = ax.twinx()
    sns.lineplot(x=years, y=avg_streams, color='#e74c3c', marker='o', markersize=10, linewidth=3, ax=ax2)
    ax.set_ylabel('Streams Totais (Bilhões)', fontsize=16, color='#1f77b4')
    ax2.set_ylabel('Média por Música (Milhões)', fontsize=16, color='#e74c3c')
    ax.tick_params(axis='y', colors='#1f77b4')
    ax2.tick_params(axis='y', colors='#e74c3c')
    max_year = total_streams.idxmax()
    plt.annotate(f'+{((total_streams[max_year]/total_streams[max_year-1])-1)*100:.0f}% vs {max_year-1}', xy=(max_year, total_streams[max_year]), xytext=(max_year-0.5, total_streams[max_year]*0.8), arrowprops=dict(arrowstyle='->', color='#2c3e50', lw=2), fontsize=14)
    plt.xticks(fontsize=14)
    plt.grid(axis='x', visible=False)
    plt.tight_layout()
    plt.savefig('streams_evolution.png', dpi=300, bbox_inches='tight')
    plt.show()

def plot_log_streams_distribution(df):
    plt.style.use('seaborn-v0_8-dark')
    plt.figure(figsize=(16, 8))
    hist = sns.histplot(df['streams'], bins=50, log_scale=True, color='#1f77b4', edgecolor='black', kde=True, kde_kws={'color': '#e74c3c', 'lw': 3})
    plt.title('Distribuição de Popularidade: 95% das Músicas têm menos de 100M Streams', fontsize=20, pad=25, fontweight='bold', color='white')
    plt.xlabel('Streams (Escala Logarítmica)', fontsize=16, color='white')
    plt.ylabel('Número de Músicas', fontsize=16, color='white')
    plt.xticks([10**4, 10**5, 10**6, 10**7, 10**8, 10**9], ['10 mil', '100 mil', '1 milhão', '10 milhões', '100 milhões', '1 bilhão'], rotation=45, fontsize=12)
    plt.axvspan(10**4, 10**6, alpha=0.1, color='#f1c40f')
    plt.text(3*10**5, plt.ylim()[1]*0.8, 'Músicas de\nBaixa Visibilidade', ha='center', color='#f1c40f', fontsize=14)
    plt.axvline(x=10**8, color='#e74c3c', linestyle='--', alpha=0.7)
    plt.text(1.2*10**8, plt.ylim()[1]*0.6, 'Top 5% de\nViralidade', color='#e74c3c', fontsize=14)
    plt.grid(True, which='both', linestyle=':', color='white', alpha=0.3)
    plt.gca().set_facecolor('#34495e')
    plt.tight_layout()
    plt.savefig('log_distribution.png', dpi=300, transparent=True)
    plt.show()