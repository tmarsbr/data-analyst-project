# 🎵 Análise de Músicas Mais Streamadas do Spotify

## 📊 Sobre o Projeto
Uma análise exploratória aprofundada das músicas mais streamadas no Spotify em 2023, utilizando Python e técnicas avançadas de Data Science para descobrir padrões e tendências que definem o sucesso musical na era do streaming.

## 🎯 Objetivos
### Principais
- Identificar padrões de sucesso em músicas populares
- Analisar correlações entre características musicais e streams
- Mapear tendências temporais de lançamentos

### Específicos
- Quantificar o impacto de features musicais (danceability, energy, etc.)
- Avaliar a influência de colaborações entre artistas
- Medir o efeito da presença em playlists

## 📈 Metodologia
1. **Coleta de Dados**
   - Dataset do Spotify com músicas mais streamadas
   - Métricas de áudio e engajamento
   - Dados de playlists e charts

2. **Pré-processamento**
   - Limpeza de dados ausentes
   - Normalização de features
   - Tratamento de outliers

3. **Análise Exploratória**
   - Distribuições estatísticas
   - Correlações entre variáveis
   - Análise temporal

## 🔬 Principais Análises
1. **Métricas de Popularidade**
   - Distribuição de streams
   - Crescimento ao longo do tempo
   - Picos de popularidade

2. **Características Musicais**
   - Correlação com streams
   - Padrões por gênero
   - Tendências sazonais

3. **Análise de Artistas**
   - Ranking por streams
   - Impacto de colaborações
   - Consistência de performance

## 🛠️ Stack Tecnológico
### Core
- Python 3.9+
- Pandas 1.5+
- NumPy 1.20+

### Visualização
- Matplotlib 3.4+
- Seaborn 0.11+
- Plotly 5.0+

### Ambiente
- Jupyter Notebook
- VSCode
- Git

## 📁 Estrutura do Projeto
```
data-analyst-project/
├── data/
│   ├── raw/               # Dados originais do Spotify
│   └── processed/         # Dados limpos e transformados
├── notebooks/
│   ├── 01_exploratory.ipynb    # Análise exploratória inicial
│   ├── 02_features.ipynb       # Análise de características
│   └── 03_insights.ipynb       # Conclusões e visualizações
├── src/
│   ├── data_preprocessing.py    # Funções de limpeza
│   ├── data_analysis.py        # Funções analíticas
│   └── visualization.py        # Funções de visualização
├── requirements.txt            # Dependências
└── README.md                  # Documentação
```

## 🚀 Como Executar
1. **Preparação do Ambiente**
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/spotify-analysis.git
cd spotify-analysis

# Crie o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate   # Windows

# Instale as dependências
pip install -r requirements.txt
```

2. **Configuração dos Dados**
```bash
# Crie as pastas necessárias
mkdir -p data/{raw,processed}

# Coloque seu arquivo CSV do Spotify em data/raw/
```

3. **Execução da Análise**
```bash
# Processe os dados
python src/data_preprocessing.py

# Execute os notebooks
jupyter notebook notebooks/
```

## 📊 Resultados Principais
### Descobertas
- Padrões de sucesso identificados
- Características mais influentes
- Tendências temporais relevantes

### Visualizações
- Heatmaps de correlação
- Gráficos de distribuição
- Análises temporais

## 👤 Autor
**Tiago Silva**
- 🔗 [LinkedIn](https://www.linkedin.com/in/tiagocientistadados)
- 💻 [GitHub](https://github.com/tmarsbr)
- 📧 [Email](mailto:tiagomars233@gmail.com)

## 🤝 Como Contribuir
1. Fork o projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença
Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## 🙏 Agradecimentos
- Spotify pela disponibilização dos dados
- Comunidade de Data Science pelo suporte
- Contribuidores do projeto

# Data Analyst Project

## Setup Instructions

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd data-analyst-project
    ```

2. Set up the virtual environment:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment:
    ```sh
    python setup_environment.py
    ```

5. Run the Jupyter Notebook:
    ```sh
    jupyter notebook
    ```

## Project Structure

- `src/`: Source code for data preprocessing, analysis, and visualization.
- `notebooks/`: Jupyter notebooks for data analysis.
- `data/`: Directory for raw and processed data.
- `setup.py`: Script to install required packages.
- `setup_environment.py`: Script to set up the project environment.

## Usage

- Use the functions in `src/` for data preprocessing, analysis, and visualization.
- Follow the steps in the Jupyter notebooks for detailed analysis.