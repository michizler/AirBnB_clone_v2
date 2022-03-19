#!/usr/bin/python3
""" City Module for HBNB project """
from os import environ

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel
from models.state import State

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class City(BaseModel):
    """ The city class, contains state ID and name """
    if (storage_engine == "db"):
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey(State.id))
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        name = ""
        state_id = ""
