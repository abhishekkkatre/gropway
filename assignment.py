import requests
from bs4 import BeautifulSoup
 
url = "https://quotes.toscrape.com/"

quotes = requests.get(url)
soup = BeautifulSoup(quotes.text, 'html.parser')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')

for quote, author in zip(quotes, authors):
    if quote.text == "Albert Einstein":
        print(f"Quote: {quote.text}")
        print(f"Author: {author.text}")
        print("-----------")