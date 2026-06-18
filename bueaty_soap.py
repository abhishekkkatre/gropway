import requests
from bs4 import BeautifulSoup
url = 'https://www.playstation.com/en-in/'
response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')

title = soup.title.text
print(f"Title: {title}")

h1 = soup.find('h1')
print(f"H1: {h1.text}")

p = soup.find('p')
print(f"Paragraph: {p.text}")

links = soup.find_all('a')
for link in links:
    print(link.text)
    print(link.get['href'])

