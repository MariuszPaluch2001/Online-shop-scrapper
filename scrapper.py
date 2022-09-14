from src.web_crawler.url import Cen_URL
from src.web_crawler.scrapper import Cen_Scrapper
from src.db_support_lib.mongodb_mod import MongoDB, MongoDB_Support
from src.web_crawler.scrap import scrap

import argparse

            
if __name__ == "__main__":
    url = Cen_URL()
    c_scrapper = Cen_Scrapper()
    db = MongoDB("scrapper")
    db_support = MongoDB_Support(db)
    scrap("Mongo", 3, url, c_scrapper, db, db_support, True, False)
