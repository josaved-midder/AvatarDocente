"""
scripts/seed_db.py
Crea las tablas y un usuario admin de ejemplo en build/app.db
"""

from pathlib import Path
import bcrypt
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, Session

BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "build" / "app.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

engine = create_engine(f"sqlite:///{DB_PATH}", echo=False, future=True)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="admin")


def main() -> None:
    # 1. Crear tablas
    Base.metadata.create_all(engine)

    # 2. Insertar usuario admin si no existe
    with Session(engine) as session:
        if not session.query(User).filter_by(username="admin").first():
            pwd = bcrypt.hashpw(b"admin123", bcrypt.gensalt()).decode()
            session.add(User(username="admin", password_hash=pwd, role="admin"))
            session.commit()
            print("✔️  Usuario admin creado (clave: admin123)")
        else:
            print("ℹ️  Usuario admin ya existía. Nada que hacer.")


if __name__ == "__main__":
    main()
