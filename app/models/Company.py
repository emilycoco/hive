from flask import Flask
from flask_sqlalchemy import SQLAlchemy, declarative_base
from app import db
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import *

Base = declarative_base()


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=True)

    def __repr__(self):
        return '<Company %r>' % self.__tablename__
