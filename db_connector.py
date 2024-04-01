from dotenv import dotenv_values

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

db_conn_config = dotenv_values('.env')

DB_HOST = db_conn_config['DB_HOST']
DB_USER = db_conn_config['DB_USER']
DB_PORT = db_conn_config['DB_PORT']
DB_PASSWORD = db_conn_config['DB_PASSWORD']
DB_NAME = db_conn_config['DB_NAME']

url = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(url)

session = sessionmaker(engine)

Base = declarative_base()

class Meme(Base):
    __tablename__ = 'meme'
    
    id = Column(Integer, primary_key=True)
    url = Column(String)
    country = Column(String)
    first_source = Column(String)
    second_source = Column(String)

with session() as db:
    meme = db.query(Meme).all()
    print(meme[0].__dict__)