
import requests
from bs4 import BeautifulSoup
import json

url="http://books.toscrape.com/"


def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
         print("Fail to load page")
         return

    response.encoding = response.apparent_encoding
    # print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    # print(books)
    books_data = []  # list to store all book dicts

    for book in books:
         title = book.h3.a['title']
     
         price_string = book.find('p', class_='price_color').text
         currency = price_string[0]
         price = float(price_string[1:])
         
         # Add to list as dictionary
         books_data.append({
            "title": title,
            "currency": currency,
            "price": price })
    
       # convert to JSON string
    json_data = json.dumps(books_data, indent=2)

    # print JSON string
    print(json_data)

   

       
book = scrape_books(url)

with open("book.json","w") as f:
    f.write(json_data)