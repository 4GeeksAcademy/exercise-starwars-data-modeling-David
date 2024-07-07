import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    apellido = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    fecha_de_subscripcion = Column(DateTime, nullable=False)
    email = Column(String(100), nullable=False)

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship(Usuario)
    planeta_id = Column(Integer, ForeignKey('planetas.id_planeta'))
    planeta = relationship("Planetas")
    vehiculo_id = Column(Integer, ForeignKey('vehiculos.id_vehiculos'))
    vehiculo = relationship("Vehiculos")
    nombre_id = Column(Integer, ForeignKey('personas.id_persona'))
    nombre = relationship("Nombres")

class Planetas(Base):
    __tablename__ = 'planetas'  
    id_planeta = Column(Integer, primary_key=True)
    nombre_planeta = Column(String(100), nullable=False)
    periodo_rotacion = Column(Integer, nullable=False)
    diametro = Column(Float, nullable=False)
    clima = Column(String(50), nullable=False)
    terreno = Column(String(50), nullable=False)

class Personas(Base):
    __tablename__ = 'personas'
    id_persona = Column(Integer, primary_key=True)
    nombre_persona = Column(String(100), nullable=False)
    peso = Column(Integer, nullable=False)
    color_de_piel = Column(String(20), nullable=False)
    color_de_pelo = Column(String(20))
    genero = Column(String(20))
    birth_year = Column(Integer, nullable=False)

class Vehiculos(Base):
     __tablename__ = 'vehiculos'
     id_vehiculos = Column(Integer, primary_key=True)
     nombre_vehiculos = Column(String(100), nullable=False)
     modelo = Column(String(50), nullable=False)
     longitud = Column(Float, nullable=False)     
     tripulacion = Column(Integer, nullable=False)
     

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')