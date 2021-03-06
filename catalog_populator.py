"""
Load test data into the database.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

# Connect to Database and create database session in Vagrant Virtual Machine
engine = create_engine('postgresql+psycopg2://vagrant:vagrant'
                       + '@localhost/itemcatalog.db', echo=True)

# Connect to Database and create database session in Ubuntu Web Server
# engine = create_engine('postgresql+psycopg2://ubuntu:ubuntu'
#                        + '@localhost/itemcatalog.db', echo=False)

# engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


user1 = User(name="Matt-Bott", email="heddy@ahed.com")
session.add(user1)
session.commit()


category1 = Category(name="Computer Processors")
session.add(category1)
session.commit()


item1 = Item(user_id=1, name="Intel i7-7700K",
             description="4 cores, 8 threads running at base-clock of 4.2GHz",
             category=category1)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Intel i5-7600K",
             description="4 cores, 4 threads running at base-clock of 3.8GHz",
             category=category1)
session.add(item2)
session.commit()


category2 = Category(name="Graphics Cards")
session.add(category2)
session.commit()


item3 = Item(user_id=1, name="Nvidia GTX 1080", description="Nvidia GPU built on the Pascal architecture, has 2560 CUDA cores, and 8GB of GDDR5X Memory",
             category=category2)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="AMD RX 580 8GB", description="AMD GPU built on the Polaris architecture, has 2304 stream processors, and 8GB of GDDR5 Memory",
             category=category2)
session.add(item4)
session.commit()


category3 = Category(name="Computer Monitors")
session.add(category3)
session.commit()


item5 = Item(user_id=1, name=" ASUS VN248H-P",
             description="24 inch 1080p IPS monitor with built in speakers, a VESA mounting point, and 2 HDMI inputs",
             category=category3)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="HP OMEN 25", description="24.5 inch 1080p TN monitor with a 144Hz refresh rate and HDMI & Displayport inputs",
             category=category3)
session.add(item6)
session.commit()


print "Added Items & Categories to App!"
