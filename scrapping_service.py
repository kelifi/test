from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import sqlite3


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



'''
Some times when you run the scrape_facebook_page you get an empty list, these are some reasons could explain this problem:

It's possible that the website you're trying to scrape is blocking your request. 
Some websites have anti-scraping measures in place to prevent automated scraping.

Another possible reason for getting an empty dictionary is if the elements you are 
trying to scrape are not in the "p" HTML tag. Try inspecting the source code of the 
page you're trying to scrape and make sure the information you're looking for is in the "p" tag.

It's also possible that the website's structure has changed, which can break your code. 
If that's the case, you'll need to update your code to match the new structure of the website.
'''

