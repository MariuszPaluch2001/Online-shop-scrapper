from src.web_crawler.get_page import get_page_html
from src.web_crawler.url import Cen_URL
from src.web_crawler.scrapper import Cen_Scrapper
from src.db_support_lib.mongodb_mod import MongoDB, MongoDB_Support, MongoDB_Queries
from datetime import datetime

if __name__ == "__main__":
    c_url = Cen_URL()
    c_scrapper = Cen_Scrapper()
    db = MongoDB("scrapper")
    db_support = MongoDB_Support(db)

