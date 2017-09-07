#!/usr/bin/python3
"""
State Class from Models Module
"""

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """State class handles all application states"""

    if os.getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all, delete", backref='state')
    else:
        name = ""

    if os.getenv('HBNB_TYPE_STORAGE', 'fs') != 'db':
        def cities(self):
            city_list = []
            for city in storage.all('City'):
                city_list.append(city)
            return (city_list)

    def __init__(self, *args, **kwargs):
        """instantiates a new state"""
        super().__init__(self, *args, **kwargs)
