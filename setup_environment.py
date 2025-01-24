import os
from pathlib import Path

# Definir o diretório raiz do projeto
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Definir diretórios de dados
DATA_DIR = PROJECT_ROOT / 'data'
RAW_DIR = DATA_DIR / 'raw'
PROCESSED_DIR = DATA_DIR / 'processed'

# Criar diretórios se não existirem
RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

def create_directories():
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)
    os.makedirs('notebooks', exist_ok=True)
    os.makedirs('src', exist_ok=True)

if __name__ == "__main__":
    create_directories()
    print("Diretórios criados com sucesso!")

# Instalar pacotes necessários
os.system('pip install -r requirements.txt')

print("Ambiente configurado com sucesso!")
