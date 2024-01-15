#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    Attributes:
    __tablename__ (str): The table name of the class
    id (int): The State id of the class
    name (str): The State name of the class
    state_id (int): id of state city belongs
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
