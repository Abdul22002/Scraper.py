import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape
URL = "http://books.toscrape.com/catalogue/category/books_1/index.html"

# Open a CSV file to save the data
with open("books_data.csv", "w", newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write the header row to the CSV
    csv_writer.writerow(["Title", "Price", "Rating"])

    def get_books_data(url):
        # Request page content
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all books on the page
        books = soup.find_all("article", class_="product_pod")
        for book in books:
            # Extract title
            title = book.h3.a["title"]
            
            # Extract price
            price = book.find("p", class_="price_color").text.strip()
            
            # Extract rating
            rating = book.p["class"][1]  # The second class in the list is the rating

            # Write the extracted data to CSV
            csv_writer.writerow([title, price, rating])
            print(f"Title: {title}, Price: {price}, Rating: {rating}")

    # Loop through the first 2 pages (you can adjust this range as needed)
    for page_num in range(1, 3):
        page_url = f"http://books.toscrape.com/catalogue/category/books_1/page-{page_num}.html"
        print(f"Scraping page {page_num}...")
        get_books_data(page_url)

print("Data scraping completed and saved to books_data.csv.")