import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    username=Column(String(20), nullable=False, unique=True)
    firstname=Column(String(20), nullable=False)
    lastname=Column(String(20), nullable=False)
    email=Column(String(50), nullable=False, unique=True)
    password=Column(String(10), nullable=False)
    created_at=Column(DateTime(), default=datetime.now())

class Character(Base):
    __tablename__='characters'
    id = Column(Integer, primary_key = True)
    films = Column (String(250), nullable=False) 
    name = Column (String(250), nullable=False) 
    species = Column (String(250), nullable=False) 
    starships = Column (String(250), nullable=False) 
    role_by = Column (String(250), nullable=False)
    birth_year = Column (String(250), nullable=False)
    eye_color =  Column (String(250), nullable=False)   # "Blue",
    gender= Column (String(250), nullable=False)        # "Male",
    hair_color=Column (String(250), nullable=False)     # "Blond",
    height= Column (String(250), nullable=False)        #"172",
    homeworld= Column (String(250), nullable=False)     # "https://swapi.dev/api/planets/1/",
    mass= Column (String(250), nullable=False)          # "77",
    skin_color=Column (String(250), nullable=False)     #"Fair",
    user_id= Column(Integer, ForeignKey('users.id'), nullable=False)
    planet_id=Column(Integer, ForeignKey('planets.id'), nullable=False)
    species_id=Column(Integer, ForeignKey('species.id_especies'), nullable=False)
    species=relationship('Species', uselist=False)
    planet=relationship('Planet', uselist=False)
    user=relationship('User', uselist=False)

class Planet(Base):
    __tablename__='planets'
    id = Column(Integer, primary_key=True)
    name =Column(String(20), nullable=False) 
    diameter=Column(String(20), nullable=False) 
    rotation_period =Column(String(20), nullable=False) 
    orbital_period =Column(String(20), nullable=False)
    gravity =Column(String(20), nullable=False)
    population=Column(String(20), nullable=False) 
    climate=Column(String(20), nullable=False) 
    terrain=Column(String(20), nullable=False)
    surface_water=Column(String(20), nullable=False)
    user_id= Column(Integer, ForeignKey('users.id'), nullable=False)
    user=relationship('User', uselist=False)
    # residents array 

class Species(Base):
    __tablename__='species'
    id_species = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    classification = Column(String(20), nullable=False)
    designation = Column(String(20), nullable=False)
    average_height= Column(String(20), nullable=False)
    average_lifespan= Column(String(20), nullable=False)
    eye_colors = Column(String(20), nullable=False)
    hair_colors = Column(String(20), nullable=False)
    skin_colors= Column(String(20), nullable=False)
    language = Column(String(20), nullable=False)
    homeworld = Column(String(20), nullable=False)
    people= Column(String(20), nullable=False)
    user_id= Column(Integer, ForeignKey('users.id'), nullable=False)
    user=relationship('User', uselist=False)

class FavoriteCharacter(Base):
    __tablename__= 'favoritecharacters'
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('users.id'), nullable=False)
    characters_id =Column(Integer, ForeignKey('characters.id'), nullable=False)
    user=relationship('User', uselist=False)
    character=relationship('Character', uselist=False)

class FavoritePlanet(Base):
    __tablename__= 'favoriteplanets'
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('users.id'), nullable=False)
    planet_id =Column(Integer, ForeignKey('planets.id'), nullable=False)
    user=relationship('User', uselist=False)
    planet=relationship('Planet', uselist=False)

render_er(Base, 'diagram.png')