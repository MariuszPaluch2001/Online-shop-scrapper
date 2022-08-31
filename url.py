class Generic_URL:

    MAIN_URL = None
    
    def __init__(self) -> None:
        pass

    def concat_url(self, *args):
        return "".join(args)

    def create_page_suffix(self, query, page_index):
        raise NotImplementedError

    def create_page_url(self ,query ,page_index):
        raise NotImplementedError
        
class Cen_URL(Generic_URL):
    
    MAIN_URL = "https://www.ceneo.pl/"

    def __init__(self) -> None:
        super().__init__()

    def create_page_suffix(self, query, page_index):
        query_part = f";szukaj-{query}"
        if page_index > 0:
            next_page_part = f";0020-30-0-0-{page_index}.htm"
        else:
            next_page_part = ""

        return "".join(
            (query_part, next_page_part)
        )

    def create_page_url(self ,query ,page_index):
        suffix = self.create_page_suffix(query, page_index)

        return self.concat_url(self.MAIN_URL, suffix)
