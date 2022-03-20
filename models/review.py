#!/usr/bin/python3
""" Review module for the HBNB project """
from os import environ

from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.testing.schema import Column

from models.base_model import BaseModel, Base

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class Review(BaseModel, Base):
    """ Review classto store review information """
    if storage_engine == "db":
        __tablename__ = "reviews"
        place_id = Column(String(60), ForeignKey("places.id"))
        user_id = Column(String(60), ForeignKey("users.id"))
        text = Column(String(1024), nullable=False)
        place = relationship("Place", back_populates="reviews")
    else:
        place_id = ""
        user_id = ""
        text = ""
