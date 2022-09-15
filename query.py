from src.db_support_lib.mongodb_mod import MongoDB, MongoDB_Support, MongoDB_Queries
from src.db_support_lib.top_utils import query_search
from datetime import datetime

if __name__ == "__main__":
    max_page = 3
    query = "Powerbank"
    db = MongoDB("scrapper")
    db_support = MongoDB_Support(db)
    mongo_q = MongoDB_Queries(db_support)
    date1 = datetime.strptime('6/9/22 12:00:00', '%d/%m/%y %H:%M:%S')
    date2 = datetime.strptime('15/9/22 16:00:00', '%d/%m/%y %H:%M:%S')

    query_search(mongo_q, "data", (0,1000), (date1, date2), "powerbank", "PLN", True)
