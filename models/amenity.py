#!/usr/bin/python3
"""
Amenity class module
"""
from os import environ
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models import BaseModel, Base
from models.place import place_amenity

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """
    Amenity Class
    """
    if (storage_engine == "db"):
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenity = relationship(
            "Place",
            secondary=place_amenity, back_populates="amenities"
        )
    else:
        name = ""
