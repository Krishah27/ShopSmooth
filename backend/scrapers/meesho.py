import requests
from bs4 import BeautifulSoup

def search_meesho(query):
    url = f"https://www.meesho.com/search?q={query.replace(' ', '%20')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    try:
        product = soup.select_one(".SearchProductCard")
        title = product.select_one("p").text
        price = product.select_one("h5").text
        price = int(''.join(filter(str.isdigit, price)))
        link = "https://www.meesho.com" + product.select_one("a")["href"]
        return {"site": "Meesho", "title": title, "price": price, "link": link}
    except:
        return None
