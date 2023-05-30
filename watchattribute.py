from sqlalchemy import Column, ForeignKey, Integer
from database import Base
from sqlalchemy.types import String


class WatchAttribute(Base):
    __tablename__ = 'watch_attribute'

    watch_kod_produktu = Column(String(50), ForeignKey('watches.kod_produktu'), primary_key=True)
    attribute_id = Column(Integer, ForeignKey('attributes.id'), primary_key=True)
