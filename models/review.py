#!/usr/bin/python3
""" Review module for the HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ 
    Review class to store review information

    Attr:
    place_id (str): id of place
    user_id (str): id of user
    text (str): text description of review
    """
    __tablename__="reviews"

    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
