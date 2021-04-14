from sqlalchemy import String, Column, Integer, Float, ForeignKey, Float
from inicializacao import db


class Info(db.Model):
    __tablename__ = 'info'
    id = Column('id', Integer, primary_key=True)
    open = Column('open', Float)
    high = Column('high', Float)
    low = Column('low', Float)
    close = Column('close', Float)
    real_volume = Column('tick_volume', Float)
    hora = Column('hora', Integer)
    minuto = Column('minuto', Integer)

    def __init__(self,open,high,low,close,real_volume,hora,minuto):  
        
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.real_volume = real_volume
        self.hora = hora
        self.minuto = minuto
    
