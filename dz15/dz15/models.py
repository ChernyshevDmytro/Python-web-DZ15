from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime

from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base() 

class News(Base):
    __tablename__ = "news"    
    id = Column(Integer, primary_key=True)
    sourse = Column(String(20), nullable=False)
    title = Column(String(50), nullable=False)
    link = Column(String(50), nullable=False)

engine = create_engine('sqlite:///dz15.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)          
