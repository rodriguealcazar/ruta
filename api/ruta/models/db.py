from dataclasses import asdict, dataclass
from typing import Optional

from geoalchemy2 import Geometry, WKBElement
from sqlalchemy import BigInteger, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import TypeDecorator


class Base(DeclarativeBase):
    pass


@dataclass
class EstablishmentTags:
    amenity: Optional[str]
    name: Optional[str] = (
        None  # TODO: filter out records with no name when ingesting data
    )
    drink: Optional[bool] = None
    food: Optional[bool] = None
    cuisine: Optional[str] = None  # TODO: auto-parse ';' separated list of str


class EstablishmentTagsType(TypeDecorator):
    """Custom type to store EstablishmentTags as JSONB."""

    impl = JSONB
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        if isinstance(value, EstablishmentTags):
            return asdict(value)
        # Fallback: assume it's already a mapping-like object
        return dict(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        # Value should be a dict loaded from JSONB
        return EstablishmentTags(**value)


class Establishment(Base):
    __tablename__ = "establishment"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    place: Mapped[WKBElement] = mapped_column(Geometry(geometry_type="POINT"))
    osm_type: Mapped[str] = mapped_column(String)
    osm_id: Mapped[int] = mapped_column(BigInteger)
    tags: Mapped[EstablishmentTags] = mapped_column(EstablishmentTagsType)
