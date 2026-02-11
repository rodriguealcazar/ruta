from dataclasses import asdict

from geoalchemy2 import WKBElement
from geoalchemy2.shape import to_shape
from pydantic import BaseModel, field_validator

from ruta.models.db import EstablishmentTags


class Establishment(BaseModel):
    model_config = {"from_attributes": True}

    id: int
    place: str
    osm_type: str
    osm_id: int
    tags: dict  # TODO: create pydantic model

    @field_validator("place", mode="before")
    @classmethod
    def validate_place(cls, v: WKBElement) -> str:
        return to_shape(v).wkt

    @field_validator("tags", mode="before")
    @classmethod
    def validate_tags(cls, v: EstablishmentTags) -> dict:
        return asdict(v)
