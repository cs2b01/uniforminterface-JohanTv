from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class Usuarios(connector.Manager.Base):
    __tablename__ = 'datosUsuario'
    usuario_id = Column(Integer, Sequence('book_id_seq'), primary_key=True)
    codigo=Column(Integer)
    nombre = Column(String(50))
    apellido = Column(String(50))
    password = Column(String(50))
