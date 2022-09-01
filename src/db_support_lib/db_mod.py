class DB_Support:
    
    def __init__(self) -> None:
        pass

    def insert(self, *args):
        raise NotImplementedError
    
    def remove(self, *args):
        raise NotImplementedError
    
    def query(self, *args):
        raise NotImplementedError

class MongoDB_Support(DB_Support):

    def __init__(self) -> None:
        super().__init__()
    
    def insert(self):
        raise NotImplementedError

    def remove(self):
        raise NotImplementedError
    
    def query(self):
        raise NotImplementedError