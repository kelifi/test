from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import sqlite3
import requests

app = FastAPI()

@app.get("/")
def scrape_facebook_page(url: str):
    '''
    web scrapping service. It takes in a parameter url which is a string and represents the URL of a Facebook page.
    
    Input:
    url: URL of the Facebook page that you want to scrape

    '''
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    page_content = soup.find_all("p")
    data = [content.get_text() for content in page_content]
    save_to_database(data)
    return {"data": data}

def save_to_database(data):
    '''
    The function will store each item in the data list as a separate row in the database.

    Input:
    data:the text data that will be stored in the SQLite database
    '''
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS scraper (data text)")
    c.executemany("INSERT INTO scraper (data) VALUES (?)", [(item,) for item in data])
    conn.commit()
    conn.close()





