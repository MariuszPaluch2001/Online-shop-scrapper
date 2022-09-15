from src.db_support_lib.db_mod import DB_Querries
from src.web_crawler.product_obj import Product

def query_search(query_obj : DB_Querries, table_name, price_interval, date_interval, product_name, currency, do_print = False):
    results = query_obj.search_product(table_name, price_interval, date_interval, product_name, currency)
    products = [Product(prod["product_name"],
                        prod["link"],
                        prod["price"],
                        prod["currency"],
                        prod["timestamp"],
                        prod["product_info"]) for prod in results]

    if do_print:
        for product in products:
            product.print()

    return products

def remove_from_db():
    ...