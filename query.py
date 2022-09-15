from src.db_support_lib.mongodb_mod import MongoDB, MongoDB_Support, MongoDB_Queries
from src.db_support_lib.top_utils import query_search

from datetime import datetime
import argparse

"""

    Query script to run without any GUI.
    If you want more info about args type into terminal:

    python query.py --help

"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p-min", "--price-min", type=int, default = None,
                    help="Number of page to scrap")
    parser.add_argument("-p-max", "--price-max", type=int, default = None,
                    help="Number of page to scrap")
    parser.add_argument("-q", "--query", type=str,
                    help="Name of product to scrap")
    parser.add_argument("-c", "--currency", type=str, default = "PLN",
                    help="Name of product to scrap")
    parser.add_argument("--do-print", default=False, action="store_true", 
                    help = "Print product info to terminal.")
    
    args = parser.parse_args()


    db = MongoDB("scrapper")
    db_support = MongoDB_Support(db)
    mongo_q = MongoDB_Queries(db_support)
    date1 = datetime.strptime('6/9/22 12:00:00', '%d/%m/%y %H:%M:%S')
    date2 = datetime.strptime('15/9/22 16:00:00', '%d/%m/%y %H:%M:%S')
    print((args.price_min,args.price_max))
    query_search(mongo_q, "data", (args.price_min,args.price_max), (date1, date2), args.query, args.currency, args.do_print)
