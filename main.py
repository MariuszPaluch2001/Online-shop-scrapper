from src.web_crawler.get_page import get_page_html
from src.web_crawler.url import Cen_URL
from src.web_crawler.scrapper import Cen_Scrapper


if __name__ == "__main__":
    max_page = 3
    query = "Stanislaw Lem"
    c_url = Cen_URL()
    c_scrapper = Cen_Scrapper()
    for url in c_url.multi_page_query(query, max_page):
        soup = get_page_html(url)
        result_gen = c_scrapper.scrap_product_info(soup)
        for res in result_gen:
            res.print()