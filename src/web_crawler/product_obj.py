import pprint

class Product:
    
    def __init__(self, name, link, price, currency, timestamp, product_info) -> None:
        self.name = name
        self.link = link
        self.price = self.__convert_sting_to_int(price)
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
        pprint.pprint(self.get_json())

    def __convert_sting_to_int(self, number_str : str) -> int:
        return int(number_str.replace(" ", "")) 