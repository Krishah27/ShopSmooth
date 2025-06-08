import requests
from bs4 import BeautifulSoup
import re

def search_flipkart(query):
    url = f"https://www.flipkart.com/search?q={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    try:
        title = soup.select_one("._4rR01T").text
        price = soup.select_one("._30jeq3").text
        link = "https://www.flipkart.com" + soup.select_one("._1fQZEK")["href"]
        price = float(re.sub(r"[^\d]", "", price))
        return {"site": "Flipkart", "title": title, "price": price, "link": link}
    except:
        return None
