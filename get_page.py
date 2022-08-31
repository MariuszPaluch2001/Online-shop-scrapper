from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def get_page(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(f"Server is not responsing. Error: {e}")
        html = None
    except URLError as e:
        print(f"Client couldn't connect with server. Error: {e}")
        html = None
    return html

def get_page_html(url):
    html = get_page(url)
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
    except AttributeError as e:
        print(f"Client couldn't get page content. Error: {e}")
        bs = None

    return bs
