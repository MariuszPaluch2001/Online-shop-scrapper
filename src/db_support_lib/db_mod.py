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
