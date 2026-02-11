from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine(
    "postgresql://ruta:ruta@localhost/ruta", echo=True, plugins=["geoalchemy2"]
)


def get_session() -> Session:
    return sessionmaker(bind=engine)()
