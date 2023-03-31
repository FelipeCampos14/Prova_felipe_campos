from flask import Flask, render_template, request

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models.base import Base
from models.jogos import Jogo

# Setando o Banco de Dados
engine = create_engine("sqlite+pysqlite:///prova.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

jogo1 = Jogo(nome = "DEAD SPACE REMAKE", plat = "PS5", preco = 350.0, quant = 10)
jogo2 = Jogo(nome = "FORSPOKEN", plat = "PC", preco = 299.0, quant = 8)
jogo3 = Jogo(nome = "DEAD ISLAND 2", plat = "PS5", preco = 350.0, quant = 10)
jogo4 = Jogo(nome = "HOGWARTS LEGACY", plat = "PC", preco = 219.0, quant = 7)  
jogo5 = Jogo(nome = "WILD HEARTS", plat = "Xbox Series", preco = 350.0, quant = 7)    
jogo6 = Jogo(nome = "RESIDENT EVIL 4", plat = "PS5", preco = 289.0, quant = 10)       
jogo7 = Jogo(nome = "THE LEGEND OF ZELDA: TEARS OF THE KINGDOM", plat = "Switch", preco = 350.0, quant = 10)                       
             
session.add(jogo1)
session.add(jogo2)
session.add(jogo3)
session.add(jogo4)
session.add(jogo5)
session.add(jogo6)
session.add(jogo7)

# Rotas
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/jogos", methods = ["GET"])
def jogos():
    session.commit()
    jogos_front = session.query(Jogo).all()
    return render_template("index.html", jogos_front = jogos_front)

if __name__ == "__main__":
    app.run(debug=True)