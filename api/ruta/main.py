import uvicorn
from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.orm import Session

from ruta.db import get_session
from ruta.models.api import Establishment
from ruta.models.db import Establishment as EstablishmentDB

app = FastAPI()


@app.get("/establishments", response_model=list[Establishment])
def get_establishments(db_session: Session = Depends(get_session)) -> list[Establishment]:
    establishments = db_session.execute(select(EstablishmentDB)).scalars().all()
    return [Establishment.model_validate(e) for e in establishments]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # noqa: F821
