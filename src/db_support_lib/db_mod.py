class DB_Connect:
    def __init__(self, *args) -> None:
        pass
    
    def get_db(self, * args):
        raise NotImplementedError
        
class DB_Crud:
    
    def __init__(self, db) -> None:
        self.db = db

    def insert(self, *args):
        raise NotImplementedError
    
    def remove(self, *args):
        raise NotImplementedError
    
    def query(self, *args):
        raise NotImplementedError

class DB_Querries:
    def __init__(self, crud : DB_Crud, *args) -> None:
        self.crud = crud

    def querry_periods(self, earlier_timestamp, later_timestamp):
        raise NotImplementedError

    def price_range(self, lower_limit, upper_limit):
        raise NotImplementedError

    def select_by_name