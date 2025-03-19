import requests
from bs4 import BeautifulSoup

class WebScraper:
    def fetch_data(self, query):
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        result = soup.find("h3")
        return result.text if result else "No data found."
