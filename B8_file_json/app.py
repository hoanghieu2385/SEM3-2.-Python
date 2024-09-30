# Clear code previous
import os
os.system("cls")

import json
from os import path
from order import Customer, Order, Address

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
    
    convertJsonToObject(path)