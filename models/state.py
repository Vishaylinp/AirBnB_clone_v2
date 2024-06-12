#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    State class

    Attr:
    __tablename__ (str); name of table where instances will be stored
    name (str): 128 char name of state, cant be null
    """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade='all, delete', backref='state')
    else:
        name = ""

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """
            getter method for cities
            Return: list of City instance where state_id == State.id
            """
            all_cities = models.storage.all("City").values()
            cities_list = []

            for city in all_cities:
                if city.state_id == self.id:
                    cities_list.append(city)
            return (cities_list)
