import os
from pprint import pprint

from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv

from src.db_support_lib.db_mod import DB_Crud, DB_Connect, DB_Querries

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

    def delete(self, collection_name, query):
        collection = self.db.get_collection(collection_name) 
        collection.delete_many(query)
    
    def query(self, collection_name, query):
        collection = self.db.get_collection(collection_name) 
        return collection.find(query)

class MongoDB_Queries(DB_Querries):
    def __init__(self, crud : DB_Crud) -> None:
        super().__init__(crud)
    
    def check_price_price_bound(self, price_bound):
        if all(map(lambda x: x is not None, price_bound)):
            return {"price": {"$gte": price_bound[0], "$lte": price_bound[1]}}
        elif price_bound[0]:
            return {"price": {"$gte": price_bound[0]}}
        elif price_bound[1]:
            return {"price": {"$gte": price_bound[1]}}

    def check_time_bound(self, time_bound):
        if all(map(lambda x: x is not None, time_bound)):
            return {"timestamp": {"$gte": time_bound[0], "$lte": time_bound[1]}}
        elif time_bound[0]:
            return {"timestamp": {"$gte": time_bound[0]}}
        elif time_bound[1]:
            return {"timestamp": {"$gte": time_bound[1]}}

    def get_query(self,price_bound, time_bound, name, currency, *product_info):
        query_parts = []
        
        result = self.check_price_price_bound(price_bound)
        if result is not None:
            query_parts.append(result)

        result = self.check_time_bound(time_bound)
        if result is not None:
            query_parts.append(result)

        if name is not None:
            query_parts.append({"product_name" : {"$regex" : name}})
        
        if currency is not None:
            query_parts.append({"currency" : {"$eq" : currency}})

        query = {"$and": query_parts}
        return query

    def search_product(self, collection_name, price_bound, time_bound, name, currency, *product_info):
        
        criteria = self.get_query(  price_bound, 
                                    time_bound, 
                                    name, currency, 
                                    product_info)

        return self.crud.query(collection_name, criteria)

    def delete_product(self, collection_name, price_bound, time_bound, name, currency, *product_info):
        criteria = {"$and": [
                    {"price": {"$gte": price_bound[0], "$lte": price_bound[1]}},
                    {"product_name" : {"$regex" : name}},
                    {"timestamp": {"$gte": time_bound[0], "$lte": time_bound[1]}}, 
                    {"currency" : {"$eq" : currency}}
                ]}
        return self.crud.delete(collection_name, criteria)