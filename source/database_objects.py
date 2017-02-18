#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column,
                        Integer,
                        Float,
                        ForeignKey)
from sqlalchemy.orm import relationship

database_name = 'random_matrix_generation_database'
Base = declarative_base()


class Matrix(Base):
  """Class to interface with the matrix table
  in the database via sqlalchemy"""
  __tablename__ = 'matrix'
  id = Column(Integer, primary_key=True)
  number_of_dimensions = Column(Integer)
  dimensions = relationship('Dimension', back_populates='matrix')
  points = relationship('Point', back_populates='matrix')


class Dimension(Base):
  """Class to interface with the dimension table
  in the database via sqlalchemy"""
  __tablename__ = 'dimension'
  id = Column(Integer, primary_key=True)
  matrix_id = Column(Integer, ForeignKey('matrix.id'))
  index = Column(Integer)
  size = Column(Integer)
  matrix = relationship('Matrix', back_populates='dimensions')


class Point(Base):
  """Class to interface with the point table
  in the database via sqlalchemy"""
  __tablename__ = 'point'
  id = Column(Integer, primary_key=True)
  matrix_id = Column(Integer, ForeignKey('matrix.id'))
  index = Column(Integer)
  value = Column(Float)
  matrix = relationship('Matrix', back_populates='points')
