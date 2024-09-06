from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#Crear una instacion de la base para crear tablas
Base= declarative_base()

#Listado de modelos de la APP

#USUARIO 
class Usuario(Base):
    __tablename__="usuarios"
    id= Column(Integer, primary_key=True, autoincrement=True) 
    nombre= Column(String(50))
    edad= Column(Integer)
    telefono= Column(String(12))
    correo= Column(String(20),unique=True)
    contraseña = Column(String(10))
    fechaDeRegistro = Column(Date)
    ciudad= Column(String(50))
#GASTO
class Gasto(Base):
    __tablename__="Gasto"
    id= Column(Integer,primary_key=True,autoincrement=True)
    monto = Column(Integer)
    fecha = Column(Date)
    descripcion = Column(String(100),nullable=True)
    nombre = Column(String(50))
#CATEGORIAS
class Categorias(Base):
    __tablename__="Categorias"
    id= Column(Integer,primary_key=True,autoincrement=True)
    nombreCategoria=Column(String(50))
    descripcion=Column(String(100),nullable=True)
    fotoicono=Column(String(300))

#METODO DE PAGO
class MetodoPago(Base):
    __tablename__="Metodo de pago"
    id= Column(Integer,primary_key=True,autoincrement=True)
    nombreMetodo=Column(String(50))
    descripcion=Column(String(100),nullable=True)
#FACTURAS
class Facturas(Base):
    pass