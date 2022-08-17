from flask import Flask, jsonify
from flask_swagger import swagger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import News

engine = create_engine('sqlite:///dz15.db', connect_args={'check_same_thread': False})  
DBSession = sessionmaker(bind=engine)
session = DBSession()


app = Flask(__name__)

@app.route("/doc")
def doc():
    return jsonify(swagger(app))

@app.route("/")
def index():

    news = session.query(News).all()
    list_of_news=[]
    json_news={}
    json_news_all={}
    for i in news:  
        json_news["source"]=i.sourse
        json_news["title"]=i.title
        json_news["link"]=i.link  
        json_news_all[f"{i.id}"]=json_news
    return  json_news_all


if __name__ == "__main__":
    Flask.run(app)