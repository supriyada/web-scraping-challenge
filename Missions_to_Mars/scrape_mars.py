import pandas as pd

import requests
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape():

    # Scrape the Mars News Site and collect the latest News Title and Paragraph Text
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    headline_url = "https://redplanetscience.com/"
    browser.visit(headline_url)
    headline_html = browser.html
    soup = bs(headline_html, "html.parser")

    news_title = soup.find('div', class_='content_title').text
    print(news_title)
    news_p = soup.find('div', class_='article_teaser_body').text
    print(news_p)

    browser.quit()

    return (news_title,news_p)

scrape()