from src.web_crawler.get_page import get_page_html
from src.web_crawler.url import Cen_URL
from src.web_crawler.scrapper import Cen_Scrapper
from src.db_support_lib.mongodb_mod import MongoDB, MongoDB_Support, MongoDB_Queries

from datetime import datetime
import pprint
def test_scrap():
    for url in c_url.multi_page_query(query, max_page):
        soup = get_page_html(url)
        result_gen = c_scrapper.scrap_product_info(soup)
        products = [res for res in result_gen]
        db_support.insert("data", [res.get_json() for res in products])


def test_query():
    mongo_q = MongoDB_Queries(db_support)
    date1 = datetime.strptime('6/9/22 12:00:00', '%d/%m/%y %H:%M:%S')
    date2 = datetime.strptime('8/9/22 16:00:00', '%d/%m/%y %H:%M:%S')
    res = mongo_q.search_product("data", (0, 10000), (date1, date2), "love", "PLN")
    for r in res:
        print(r["product_name"])

def test_remove():
    db_support.delete("data", {})

if __name__ == "__main__":
    max_page = 3
    query = "figurka"
    c_url = Cen_URL()
    c_scrapper = Cen_Scrapper()
    db = MongoDB("scrapper")
    db_support = MongoDB_Support(db)
    # test_scrap()
    # test_remove()
    test_query()
