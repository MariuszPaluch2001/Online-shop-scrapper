from src.web_crawler.url import Cen_URL
from src.web_crawler.scrapper import Cen_Scrapper
from src.db_support_lib.mongodb_mod import MongoDB, MongoDB_Support

from src.web_crawler.scrap import scrap

import argparse

"""

    Script to run without any GUI.
    If you want more info about args type into terminal:

    python scrapper.py --help

"""
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number_pages", type=int, default = 1,
                    help="Number of page to scrap")
    parser.add_argument("-q", "--query", type=str,
                    help="Name of product to scrap")
    parser.add_argument("--do-print", default=False, action="store_true", 
                    help = "Print product info to terminal.")
    parser.add_argument("--no-write-db", default=False, action="store_true", 
                    help = "Do not write data to database.")
    args = parser.parse_args()
    url = Cen_URL()
    c_scrapper = Cen_Scrapper()
    db = MongoDB("scrapper")
    db_support = MongoDB_Support(db)
    scrap(args.query, args.number_pages, url, c_scrapper, db, db_support, args.do_print, args.no_write_db)
