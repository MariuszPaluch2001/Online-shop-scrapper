class Generic_Scapper:

    def __init__(self) -> None:
        pass

    def scrap_product_rows(self, soup):
        raise NotImplementedError

    def scrap_product_info(self,soup):
        rows = self.scrap_product_rows(soup)
        
        for row in rows:
            name = self.scrap_name(row)
            link = self.scrap_link_suffix(row)
            price = self.scrap_price(row)
            currency = self.scrap_currency(soup)
            product_info = self.scrap_info(row)
            
            yield {
                "product_name" : name,
                "link" : link,
                "price" : price,
                "currency" : currency,
                "product_info" : product_info
            }

    def scrap_name(self, soup) -> str:
        raise NotImplementedError

    def scrap_link_suffix(self, soup) -> str:
        raise NotImplementedError

    def scrap_price(self, soup) -> str:
        raise NotImplementedError
    
    def scrap_currency(self, soup) -> str:
        raise NotImplementedError

    def scrap_info(self, soup) -> tuple:
        raise NotImplementedError

class Cen_Scrapper(Generic_Scapper):
    
    def __init__(self) -> None:
        super().__init__()

    def scrap_product_rows(self, soup):
        return soup.find_all("div", {"class": "cat-prod-row__content"})

    def scrap_name(self, soup) -> str:
        return soup.find("strong", {"class" : "cat-prod-row__name"}).text.strip()

    def cen_link_find(self, soup):
        res = soup.find("a", {"class" : "go-to-product js_conv js_clickHash js_seoUrl"})
        if res is None:
            res = soup.find("a", {"class" : "go-to-shop js_conv js_clickHash js_seoUrl"})
        if res is None:
            res = soup.find("a", {"class" : "go-to-shop js_conv js_seoUrl"})
        if res is None:
            return None
        
        return res

    def scrap_link_suffix(self, soup) -> str:
        res = self.cen_link_find(soup)
        if res is None:
            return "NO LINK"
        return res["href"]

    def scrap_price(self, soup) -> str:
        return soup.find("span", {"class" : "value"}).text

    def scrap_currency(self, *args) -> str:
        return "PLN"

    def scrap_info_gen(self, soup):
        res = soup.find("ul", {"class" : "prod-params cat-prod-row__params"})

        if res is None:
            return {}

        res = res.find_all("li")
        for elem in res:
            children = tuple(elem.children)
            yield {children[0] : children[1].text}

    def scrap_info(self, soup) -> tuple:
        return tuple(self.scrap_info_gen(soup))