#!/usr/bin/python3
"""
Contains State class that inherits from Base
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

md = MetaData()
Base = declarative_base(metadata=md)


class State(Base):
    """
    Class with id and name attributes
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
