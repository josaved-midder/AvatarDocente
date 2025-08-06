#!/usr/bin/env python3
"""
init_project.py  –  Crea la estructura inicial del proyecto “avatar-docente”.

Uso:
    python init_project.py
"""

from pathlib import Path
import textwrap
import json
import os

# ─── Configuración general ────────────────────────────────────────────────────
PROJECT_NAME = "avatar-docente"

# Carpetas que se crearán (con subcarpetas anidadas)
DIRS = [
    "src/gui/windows",
    "src/gui/widgets",
    "src/controllers",
    "src/services",
    "src/models",
    "src/config/rubrics",
    "src/utils",
    "src/assets/avatars",
    "src/assets/audio",
    "src/assets/icons",
    "tests",
    "docs/uml",
    "scripts",
    "build/logs",
    ".github/workflows",
]

# Archivos con contenido mínimo (ruta => contenido)
FILES = {
    "README.md": "# Proyecto Avatar Docente\n\nPlantilla generada automáticamente.\n",
    "LICENSE": "MIT\n",
    ".gitignore": textwrap.dedent(
        """
        # Entornos virtuales
        .venv/
        # PyInstaller
        build/
        dist/
        *.spec
        # IDE
        .idea/
        .vscode/
        __pycache__/
        """
    ),
    ".env.example": "OPENAI_API_KEY=\n",
    "pyproject.toml": textwrap.dedent(
        """
        [tool.poetry]
        name = "avatar-docente"
        version = "0.1.0"
        description = "Aplicación de escritorio con avatar docente interactivo"
        authors = ["Tu Nombre <tu@email.com>"]

        [tool.poetry.dependencies]
        python = "^3.11"
        PyQt5 = "*"
        python-dotenv = "*"
        sqlalchemy = "*"
        openai = "*"
        pyttsx3 = "*"
        bcrypt = "*"

        [tool.poetry.group.dev.dependencies]
        pytest = "*"
        black = "*"
        isort = "*"
        """
    ),
    "src/__init__.py": "",
    "src/main.py": textwrap.dedent(
        """
        \"\"\"Punto de entrada provisional\"\"\"
        import sys
        from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

        def main() -> None:
            app = QApplication(sys.argv)
            w = QWidget()
            w.setWindowTitle("Avatar Docente – MVP")
            layout = QVBoxLayout(w)
            layout.addWidget(QLabel("¡Hola, mundo!"))
            w.show()
            sys.exit(app.exec_())

        if __name__ == "__main__":
            main()
        """
    ),
    "src/config/settings.py": textwrap.dedent(
        """
        \"\"\"Carga variables desde .env\"\"\"
        import os
        from pathlib import Path
        from dotenv import load_dotenv

        BASE_DIR = Path(__file__).resolve().parents[2]
        load_dotenv(BASE_DIR / ".env", override=True)

        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
        DB_URL = f"sqlite:///{BASE_DIR / 'build' / 'app.db'}"
        """
    ),
    "scripts/run_dev.sh": "#!/usr/bin/env bash\npoetry run python -m src.main\n",
    ".github/workflows/ci.yml": textwrap.dedent(
        """
        name: CI

        on: [push, pull_request]

        jobs:
          build:
            runs-on: ubuntu-latest
            steps:
              - uses: actions/checkout@v3
              - uses: actions/setup-python@v5
                with:
                  python-version: '3.11'
              - run: pip install poetry
              - run: poetry install
              - run: poetry run pytest -v
        """
    ),
    "src/models/db_session.py": textwrap.dedent(
        """
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker, declarative_base
        from src.config.settings import DB_URL

        engine = create_engine(DB_URL, echo=False, future=True)
        SessionLocal = sessionmaker(bind=engine, autoflush=False, future=True)
        Base = declarative_base()
        """
    ),
    # Rubrica por defecto
    "src/config/rubrics/default_rubric.yml": textwrap.dedent(
        """
        criterios:
          comprension:
            peso: 0.4
          coherencia:
            peso: 0.3
          ortografia:
            peso: 0.3
        """
    ),
}

# ─── Creación de carpetas y archivos ──────────────────────────────────────────
def create_structure() -> None:
    base = Path(PROJECT_NAME)
    base.mkdir(exist_ok=True)

    for d in DIRS:
        (base / d).mkdir(parents=True, exist_ok=True)
        print(f"📁  Creada carpeta: {d}")

    for filepath, content in FILES.items():
        full_path = base / filepath
        full_path.parent.mkdir(parents=True, exist_ok=True)
        # No sobrescribir si existe
        if not full_path.exists():
            full_path.write_text(content, encoding="utf-8")
            print(f"📄  Creado archivo: {filepath}")

    # Hacer ejecutable el script run_dev.sh si estamos en Unix
    script_path = base / "scripts" / "run_dev.sh"
    if script_path.exists() and os.name != "nt":
        script_path.chmod(script_path.stat().st_mode | 0o111)

    print(f"\n✅  Estructura inicial creada en ./{PROJECT_NAME}")

if __name__ == "__main__":
    create_structure()
