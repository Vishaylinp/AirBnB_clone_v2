#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import os
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
    name = Column(String(128), nullable=False)

    if os.environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship("City", cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            """
            getter method for cities
            Return: list of City instance where state_id == State.id
            """
            from models import storage
            from models.city import City

            all_cities = storage.all(City)
            cities_list = []

            for city in all_cities.values():
                if City.state_id == self.id:
                    cities_list.append(city)

            return (cities_list)
