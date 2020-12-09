#!/usr/bin/env python
# coding: utf-8



import pandas as pd
from sqlalchemy import create_engine
#from datetime import datetime
import datetime as dt
import matplotlib.pyplot as plt
import webbrowser
#pip install selenium
from splinter import Browser
import matplotlib.pyplot as plt




# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager




#executable_path = {'executable_path': ChromeDriverManager().install()}
executable_path = {'executable_path': 'C:\\Users\\nagen\\OneDrive\\Documents\\GitHub\\GT-ATL-DATA-PT-09-2020-U-C-2\\GT-ATL-DATA-PT-09-2020-U-C-2\\12-Web-Scraping-and-Document-Databases\\Homework\\Resources\\chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)




# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)




# Define database and collection
db = client.mars_db
collection = db.items





# visit URL of page to be scraped
url = 'https://mars.nasa.gov/news/'
browser.visit(url)





html = browser.html
# HTML parsing with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')





news_title =  soup.find('div', class_='content_title').text
news_title





news_p = soup.find('div', class_='article_teaser_body').text
news_p









# Visit URL of the page to be scraped
url_1 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url_1)




html = browser.html
soup = BeautifulSoup(html, 'html.parser')




#Find the URL for the Image
image_url_1 = soup.find('li',class_='slide').a['data-fancybox-href']
image_url_1



#Combine main website to image for full URL
main = 'https://www.jpl.nasa.gov/'
featured_image_url_1 = main + image_url_1
featured_image_url_1




carousel_item =  soup.find('article', class_='carousel_item')
carousel_item



# URL of page to be scraped
url_2 = 'https://space-facts.com/mars/'
browser.visit(url_2)




html = browser.html
soup = BeautifulSoup(html, 'html.parser')





soup.body





soup.body.text





soup.body.find_all('p')





soup.find_all('div')




html = browser.html
soup = bs(html, 'html.parser')

soup




tables= pd.read_html('https://space-facts.com/mars/')
tables


# Take second table for Mars facts
df = tables[1]

# Rename columns and set index
df.columns=['Index','description', 'value']
#del df['Index']
df





# Convert table to html
mars_facts_table = [df.to_html(classes='data table table-borderless', index=False, header=False, border=0)]
mars_facts_table




# visit browser to USGS Astrogeology site
browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')





html = browser.html
soup = bs(html, 'html.parser')

hemisphere_names = []

# Search for the names of all four hemispheres
results = soup.find_all('div', class_="collapsible results")
hemispheres = results[0].find_all('h3')

# Get text and store in list
for name in hemispheres:
    hemisphere_names.append(name.text)

hemisphere_names





# thumbnail links search 
thumbnail_results = results[0].find_all('a')
thumbnail_links = []

for thumbnail in thumbnail_results:
    
    # If the thumbnail element has an image...
    if (thumbnail.img):
        
        # then grab the attached link
        thumbnail_url = 'https://astrogeology.usgs.gov/' + thumbnail['href']
        
        # Append list with links
        thumbnail_links.append(thumbnail_url)

thumbnail_links



full_imgs = []

for url in thumbnail_links:
    
    # Click through each thumbanil link
    browser.visit(url)
    
    html = browser.html
    soup = bs(html, 'html.parser')
    
    # Scrape each page for the relative image path
    results = soup.find_all('img', class_='wide-image')
    relative_img_path = results[0]['src']
    
    # Combine the reltaive image path to get the full url
    img_link = 'https://astrogeology.usgs.gov/' + relative_img_path
    
    # Add full image links to a list
    full_imgs.append(img_link)

full_imgs





# Zip together the list of hemisphere names and hemisphere image links
mars_hemi_zip = zip(hemisphere_names, full_imgs)

hemisphere_image_urls = []

# Iterate through the zipped object
for title, img in mars_hemi_zip:
    
    mars_hemi_dict = {}
    
    # Add hemisphere title to dictionary
    mars_hemi_dict['title'] = title
    
    # Add image url to dictionary
    mars_hemi_dict['img_url'] = img
    
    # Append the list with dictionaries
    hemisphere_image_urls.append(mars_hemi_dict)

hemisphere_image_urls












