from src.db_support_lib.mongodb_mod import MongoDB, MongoDB_Support, MongoDB_Queries
from src.db_support_lib.top_utils import delete_from_db

from datetime import datetime
import argparse

"""

    Deleting script to run without any GUI.
    If you want more info about args type into terminal:

    python delete.py --help

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
    parser.add_argument("-q", "--query", type=str, default= None,
                    help="Name of product to query")
    parser.add_argument("-c", "--currency", type=str, default = None,
                    help="Currency of product in query")
    
    args = parser.parse_args()


    db = MongoDB("scrapper")
    db_support = MongoDB_Support(db)
    mongo_q = MongoDB_Queries(db_support)
    
    if args.date_min is not None:
        date_min = datetime.strptime(args.date_min, '%d/%m/%y %H:%M:%S')
    else:
        date_min = None

    if args.date_max is not None:
        date_max = datetime.strptime(args.date_max, '%d/%m/%y %H:%M:%S')
    else:
        date_max = None
        
    delete_from_db(mongo_q, "data", (args.price_min,args.price_max), (date_min, date_max), 
                args.query, args.currency
    )
