from sqlalchemy import Column, String, Integer
from database import Base


class Attribute(Base):
    __tablename__ = 'attributes'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __init__(self, name):
        self.name = name
