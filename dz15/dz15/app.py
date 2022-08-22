from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import News

engine = create_engine('sqlite:///spiders/dz15.db', connect_args={'check_same_thread': False})  
DBSession = sessionmaker(bind=engine)
session = DBSession()


app = FastAPI()

@app.get("/")
async def index():
    news = session.query(News).all()
    json_news_all={}
    for i in news:
        json_news={}          
        json_news["source"]=i.sourse
        json_news["title"]=i.title
        json_news["link"]=i.link  
        json_news_all[f"{i.id}"]=json_news
        #json_news.clear()
        #print(len(json_news_all))
    return  json_news_all
