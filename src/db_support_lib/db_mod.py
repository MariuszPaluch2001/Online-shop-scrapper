class DB_Support:
    
    def __init__(self, db) -> None:
        self.db = db

    def insert(self, *args):
        raise NotImplementedError
    
    def remove(self, *args):
        raise NotImplementedError
    
    def query(self, *args):
        raise NotImplementedError
