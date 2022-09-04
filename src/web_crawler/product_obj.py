import pprint

class Product:
    
    def __init__(self, name, link, price, currency, product_info) -> None:
        self.name = name
        self.link = link
        self.price = price
        self.currency = currency
        self.product_info = product_info
    
    def get_json(self):
        return  {
                "product_name" : self.name,
                "link" : self.link,
                "price" : self.price,
                "currency" : self.currency,
                "product_info" : self.product_info
            }

    def print(self):
        pprint.pprint(self.get_json())