# Clear code previous
import os
os.system("cls")

import json
from os import path
from order import Customer, Order, Address

from pymongo import MongoClient

# MongoDB connection
connection_string = "mongodb://localhost:27017/"
try:
    client = MongoClient(connection_string)
    database_name = "test"
    collection_name = "json_demo"

    db = client[database_name]
    collection = db[collection_name]

    if collection is None:
        print("Cannot connect")
    else:
        print("Connected successfully")
except Exception as e:
    print("Error connecting to MongoDB:", e)
    
def insert_db(path):
    if path is not None:
        with open(path) as file:
            file_data = json.load(file)
    if isinstance(file_data, list):
        collection.insert_many(file_data)
        print("Insert successfully")
    else:
        collection.insert_one(file_data)
        print("Insert successfully")
    
def readFileJson(path):
    if path is not None:
        with open(path, 'r') as content:
            order = json.load(content)
            print(order["orderID"])
            
            
def writeFileJson(order, path):
    if path is not None:
        with open(path, 'w') as file:
            json.dump(order.dict(),file,indent=4)
    
def convertJsonToObject(path):
    if path is not None:
        with open(path, 'r') as content:
            json_data = json.load(content)
    
        order = Order(**json_data)
        print(order.orderID)
    
            
if __name__ == '__main__':
    path = "./B8_file_json/order.json"
    # readFileJson(path)
    
    # order = Order (
    #     orderID = "854",
    #     customer = Customer(
    #         name = "Hieu New",
    #         email ="hieu_demo_NEW__@gmail.com",
    #         phone ="+84 127654789",
    #         address = Address(
    #             street ="Ton That Thuyet NEW",
    #             city ="Ha Noi",
    #             state ="HN",
    #             postalCode = "4353",
    #             country ="HN"
    #         )
    #     )
    # )
    # writeFileJson(order, path)
    # readFileJson(path)
    
    # convertJsonToObject(path)
    
    insert_db(path)