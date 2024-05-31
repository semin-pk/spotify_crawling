from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
import pymongo
import os
from dotenv import load_dotenv
load_dotenv()
USERNAME = os.getenv("DATABASE_USERNAME")
PASSWORD = os.getenv("DATABASE_PASSWORD")
HOST = os.getenv("DATABASE_HOSTAME")
PORT = os.getenv("DATABASE_PORT")
DB = os.getenv("DATABASE_NAME")
DB_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'

MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT")
MONGO_DB = os.getenv("MONGO_DB")
 
# Create a MongoDB client

MONGO_DB_URL = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"

class engineconn:
    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle = 500)

    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
    
    def connection(self):
        conn = self.engine.connect()
        return conn
    
class MongoDB:
    def __init__(self):
        self.client = MongoClient(MONGO_DB_URL)
    
    def get_database(self, db_name):
        return self.client[db_name]
    
    def get_collection(self, db_name, collection_name):
        db = self.get_database(db_name)
        return db[collection_name]
    
