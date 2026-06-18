import requests
import json
from bs4 import BeautifulSoup
url = 'https://quotes.toscrape.com/'
response = requests.get(url)
quotes = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author') 

for quote, author in zip(quotes, authors):
    print(f"Quote: {quote.text}")
    print(f"Author: {author.text}")
    print("-----------") 
    
data = []
for quote, author in zip(quotes, authors):
    data.append({
        'quote': quote.text,
        'author': author.text
    })
with open ("quotes.json", 'w') as f:
    json.dump(data, f, indent=4)
print("Quotes saved to quotes.json")

    