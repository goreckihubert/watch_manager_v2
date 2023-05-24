from sqlalchemy import Column, String, Boolean
from database import Base


class Watch(Base):
    __tablename__ = 'watches'

    kod_produktu = Column(String(50), primary_key=True)
    proba = Column(String(50))
    grawer = Column(Boolean)
    dla_kogo = Column(String(50))
    rodzaj = Column(String(50))
    styl = Column(String(50))
    pochodzenie = Column(String(50))
    szkielko = Column(String(50))
    rodzaj_koperty = Column(String(50))
    szerokosc_koperty = Column(String(50))
    grubosc_koperty = Column(String(50))
    typ_paska_bransolety = Column(String(50))
    kolor_paska_bransolety = Column(String(50))
    wodoszczelnosc = Column(String(50))
    mechanizm = Column(String(50))
    gwarancja = Column(String(50))
    kolor_tarczy = Column(String(50))
