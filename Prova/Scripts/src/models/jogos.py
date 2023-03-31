from models.base import Base
from sqlalchemy import Column, Integer, String

class Jogo(Base):
    __tablename__ = "Jogo"
    id = Column(Integer, primary_key = True)
    nome = Column(String)
    plat = Column(String)
    preco = Column(Integer)
    quant = Column(Integer)

    def __repr__(self) -> str:
        return f"jogos(id={self.id}, nome ={self.nome}, plataforma ={self.plat}, preço ={self.preco}, quantidade ={self.quant})"