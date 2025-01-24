import os
import sys
from pathlib import Path

def setup_environment():
    project_root = Path(__file__).resolve().parent
    data_dir = project_root / 'data'
    raw_dir = data_dir / 'raw'
    processed_dir = data_dir / 'processed'

    raw_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)

    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    print(f"Project root: {project_root}")
    print(f"Data directories created at {data_dir}")

if __name__ == "__main__":
    setup_environment()
