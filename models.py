from database import Base
from sqlalchemy import Column, Integer, String

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), primary_key=True, unique=True)
    name = Column(String(50))
    password = Column(String(100))