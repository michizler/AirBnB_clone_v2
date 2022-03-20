#!/usr/bin/python3
""" State Module for HBNB project """
from os import environ

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

import models
from models.base_model import BaseModel, Base

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    if storage_engine == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """
            cities list
            """
            result = []
            for j, i in models.storage.all(models.city.City).items():
                if i.state_id == self.id:
                    result.append(i)
            return result
