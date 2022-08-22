# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import News


class Dz15Pipeline:
    def process_item(self, item, spider):            
        engine = create_engine("sqlite:///spiders/dz15.db")
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        if item["title"] and item["link"] and item["source"]:
            new_name = News(sourse=item["source"], title=item["title"], link=item["link"])
            session.add(new_name)
            session.commit()

        return item
