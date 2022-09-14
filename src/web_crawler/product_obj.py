import pprint

class Product:
    
    def __init__(self, name, link, price, currency, timestamp, product_info) -> None:
        self.name = name
        self.link = link
        self.price = price
        self.currency = currency
        self.product_info = product_info
        self.timestamp = timestamp
    
    def get_json(self):
        return  {
                "product_name" : self.name,
                "link" : self.link,
                "price" : self.price,
                "currency" : self.currency,
                "timestamp" : self.timestamp,
                "product_info" : self.product_info
            }

    def print(self):
        print(f"Product name: {self.name}")
        print(f"Price: {self.price} {self.currency}")
        print(f"Link: {self.link}")
        print(f"Timestamp: {str(self.timestamp)}")
        pprint.pprint(self.product_info)
        print("-"*50)

