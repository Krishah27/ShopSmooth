from .scrapers.amazon import search_amazon
from .scrapers.flipkart import search_flipkart
from .scrapers.myntra import search_myntra
from .scrapers.meesho import search_meesho

def compare_all(query):
    results = [
        search_amazon(query),
        search_flipkart(query),
        search_myntra(query),
        search_meesho(query)
    ]
    results = [r for r in results if r]
    cheapest = min(results, key=lambda x: x["price"])
    return {"cheapest": cheapest, "all": results}
