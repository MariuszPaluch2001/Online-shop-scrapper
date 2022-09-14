from src.web_crawler.get_page import get_page_html

def scrap(query, numb_pages, url, scrapper, db, db_support, print_flag = False, no_add_to_db = False):
    for page in url.multi_page_query(query, numb_pages):
        soup = get_page_html(page)
        result_gen = scrapper.scrap_product_info(soup)
        products = list(result_gen)
        if print_flag:
            for product in products:
                product.print()
        
        if not no_add_to_db:
            db_support.insert("data", [res.get_json() for res in products])