import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url, timeout=15)
soup = BeautifulSoup(response.text, "html.parser")

books = []

for book in soup.select("article.product_pod"):
    title = book.h3.a["title"]
    price = book.select_one(".price_color").get_text(strip=True)
    price = price.replace("Â", " ").replace("Å", " ")
    availability = book.select_one(".availability").get_text(strip=True)
    rating = book.select_one(".star-rating")["class"][1]

    books.append({
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Availability": availability
    })

df = pd.DataFrame(books)
df.to_csv("books_data.csv", index=False, encoding="utf-8-sig")

print("Total books collected:", len(df))
print(df.head())
print("\nData saved to books_data.csv")