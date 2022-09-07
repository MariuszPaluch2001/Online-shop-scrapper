from src.web_crawler.get_page import get_page_html
from src.web_crawler.url import Cen_URL
from src.web_crawler.scrapper import Cen_Scrapper
from src.db_support_lib.mongodb_mod import MongoDB, MongoDB_Support, MongoDB_Queries
if __name__ == "__main__":
    max_page = 3
    query = "komputer"
    c_url = Cen_URL()
    c_scrapper = Cen_Scrapper()
    db = MongoDB("scrapper")
    db_support = MongoDB_Support(db)
    for url in c_url.multi_page_query(query, max_page):
        soup = get_page_html(url)
        result_gen = c_scrapper.scrap_product_info(soup)
        products = [res for res in result_gen]
        db_support.insert("data", [res.get_json() for res in products])
        for product in products:
            product.print()

    mongo_q = MongoDB_Queries(db_support)

    res = mongo_q.search_product("data", (500, 2000), None, None, "PLN")
    for r in res:
        print(r)