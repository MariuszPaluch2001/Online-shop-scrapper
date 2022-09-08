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
    
    def delete(self, *args):
        raise NotImplementedError
    
    def query(self, *args):
        raise NotImplementedError

class DB_Querries:
    def __init__(self, crud : DB_Crud, *args) -> None:
        self.crud = crud
        self.current_query = None

    def search_product(self, price_bound, time_bound, name, currency, *product_info):
        raise NotImplementedError
