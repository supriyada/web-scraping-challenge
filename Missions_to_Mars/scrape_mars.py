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

    # The image url for the current Featured Mars Image is scraped from the Featured Space Image site here and assigned the url string
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    img_url = "https://spaceimages-mars.com"
    browser.visit(img_url)
    img_html = browser.html
    soup = bs(img_html, "html.parser")

    image_url = soup.find('img', class_='headerimage fade-in' )["src"]
    print(image_url)

    featured_image_url = f'{img_url}/{image_url}'
    print(featured_image_url)

    browser.quit()

    #From the Mars Facts webpage here, the table containing facts about the planet is scraped using pandas.
    fact_url = 'https://galaxyfacts-mars.com'
    mars_facts_table = pd.read_html(fact_url)
    facts_df = mars_facts_table[0]
    fact_df = facts_df.rename(columns={0:"Description", 1:"Mars", 2:"Earth"})
    mars_fact_df= fact_df.set_index("Description")
    mars_fact_html_table = mars_fact_df.to_html(classes="table table-hover table-striped table-responsive", \
                                       border=1,index=True,table_id='Mars_fact_table')

    #mars_dict = mars_fact_df.to_dict()
    

    #From the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    hemisphere_url = 'https://marshemispheres.com/'
    browser.visit(hemisphere_url)   

    hemisphere_html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(hemisphere_html, 'html.parser')
    # Retrieve all elements that contain mars hemisphere information
    items = soup.find_all('div', class_='item')

    hemisphere_image_urls = []

    for item in items:
        title = item.find('h3').text
        mars_img_url = item.find('img',class_='thumb')['src']
        full_mars_img_url = f'{hemisphere_url}{mars_img_url}'
        hemisphere_image_urls.append({"title":title,"img_url":full_mars_img_url})

    hemisphere_image_urls

    browser.quit()

    mars_info_dict = {"News_Title":news_title,
                    "News_P":news_p,
                    "Featured_Image":featured_image_url,
                    "Mars_fact":mars_fact_html_table,
                    "Mars_hemisphere":hemisphere_image_urls
                    }

    return (mars_info_dict)

