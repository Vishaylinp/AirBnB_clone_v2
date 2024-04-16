#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer


class Place(BaseModel, Base):
    """ A place to stay
    Attributes:
        city_id: city id
        user_id: user id
        name: name
        description: descript
        number_rooms: number of rooms
        number_bathrooms: number of bathroom
        max_guest:max number of guess
        price_by_night: price per night
        latitude: lat
        longitude: long
        amenity_ids: list
     """

    __tablename__ = "places"

    city_id = Column(String(60), nullable=False, ForeignKey("cities.id"))
    user_id = Column(String(60), nullable=False, ForeignKey("user.id"))
    name = Column(String(128), nullable=False))
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0))
    number_bathroom = Column(Integer, nullable=False, default=0))
    max_guest = Column(Integer, nullable=False, default=0))
    price_by_night = Column(Integer, nullable=False, default=0))
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
