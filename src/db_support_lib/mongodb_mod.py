import os

from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv

from src.db_support_lib.db_mod import DB_Crud, DB_Connect

class MongoDB(DB_Connect):

    def __init__(self, db_name) -> None:
        load_dotenv(find_dotenv())
        password = os.environ.get("MONGODB_PWD")
        connect_str = f"""mongodb+srv://mariuszpaluch:{password}@myprojects.z9jwiv9.mongodb.net/?retryWrites=true&w=majority&authSource=admin"""    
        self.client = MongoClient(connect_str)
        self.db = self.client.get_database(db_name)

    def get_collection(self, collection_name):
        return self.db.get_collection(collection_name)

    def get_db(self):
        return self.db

class MongoDB_Support(DB_Crud):

    def __init__(self, db : MongoDB) -> None:
        super().__init__(db)
    
    def insert(self, collection_name, documents):
        collection = self.db.get_collection(collection_name)
        id = collection.insert_many(documents).inserted_ids
        return id

    def remove(self):
        raise NotImplementedError
    
    def query(self):
        raise NotImplementedError