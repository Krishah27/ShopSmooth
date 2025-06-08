import requests
from bs4 import BeautifulSoup

def search_amazon(query):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.amazon.in/s?k={query.replace(' ', '+')}"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    try:
        result = soup.select_one("div.s-main-slot div[data-component-type='s-search-result']")
        title = result.select_one("h2 span").text
        price = result.select_one(".a-price-whole").text.replace(",", "")
        link = "https://www.amazon.in" + result.select_one("h2 a")["href"]
        return {"site": "Amazon", "title": title, "price": float(price), "link": link}
    except:
        return None
