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
                    help="Minimal value in price bound")
    parser.add_argument("-p-max", "--price-max", type=int, default = None,
                    help="Maximal value in price bound")
    parser.add_argument("-d-min", "--date-min", type=str, default = None,
                    help=R"Begining date in date range. Date format: 'd/m/y H:M:S'")
    parser.add_argument("-d-max", "--date-max", type=str, default = None,
                    help=R"Ending date in date range. Date format: 'd/m/y H:M:S'")
    parser.add_argument("-q", "--query", type=str,
                    help="Name of product to query")
    parser.add_argument("-c", "--currency", type=str, default = "PLN",
                    help="Currency of product in query")
    parser.add_argument("--do-print", default=False, action="store_true", 
                    help = "Print product info to terminal.")
    
    args = parser.parse_args()


    db = MongoDB("scrapper")
    db_support = MongoDB_Support(db)
    mongo_q = MongoDB_Queries(db_support)
    
    date_min = datetime.strptime(args.date_min, '%d/%m/%y %H:%M:%S')
    date_max = datetime.strptime(args.date_max, '%d/%m/%y %H:%M:%S')

    query_search(mongo_q, "data", (args.price_min,args.price_max), (date_min, date_max), 
                args.query, args.currency, args.do_print
    )
