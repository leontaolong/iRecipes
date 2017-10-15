import requests
import time
import os
import csv

from bs4 import BeautifulSoup
from selenium import webdriver

# Scrapes the website of interest, gather the required text data, 
# and place it into the correct format. This script outputs results to rawData_file_path
def scape(rawData_file_path):
    # Pages to be scaped
    # Note: It takes really a long time to run webdriver on each page and wait for the ads loading.
    #       Can comment out the rest and leave only one page for testing purpose
    pages = [
            'https://www.yummly.com/recipes/lunch',
            'https://www.yummly.com/recipes/dinner',
            'https://www.yummly.com/browse/recommended',
            'https://www.yummly.com/browse/seasonal',
            'https://www.yummly.com/browse/popular-now',
            'https://www.yummly.com/browse/quick-and-easy'
            ]

    # Download webdriver from: https://chromedriver.storage.googleapis.com/index.html?path=2.33/
    # and put it in the same directory of the scripts
    # Download selenium from: https://pypi.python.org/pypi/selenium
    driver_path = os.path.dirname(os.path.abspath("__file__")) + '/chromedriver'
    driver = webdriver.Chrome(driver_path)

    f = open(rawData_file_path, 'w')
    writer = csv.writer(f, delimiter=',')

    # recipe page base url
    base_url = 'https://www.yummly.com/#recipe/'

    for page in pages:

        # Request webpage information
        page_req = requests.get(page)
        page_soup = BeautifulSoup(page_req.text, 'html.parser')
        recipe_grids = page_soup.find_all("div", {"class" : "single-recipe"})

        first_time=True
        for recipe_grid in recipe_grids: # go to each recipe from the links in recipe_grids
            recipe_link = base_url + recipe_grid.get('data-url')
            page = driver.get(recipe_link)

            # Sleep for page loading: first time 3 secs, and 1 secs for the rest
            if first_time:
                time.sleep(3)
                first_time = False
            else:
                time.sleep(1)

            # Extract the information    
            recipe_page = driver.page_source
            recipe_soup = BeautifulSoup(recipe_page, 'html.parser')
            if recipe_soup.find("div", {"class" : "primary-info-text"}):
                recipe_name = recipe_soup.find("div", {"class" : "primary-info-text"}).find({"h1"}).get_text()
                ingredient_elements = recipe_soup.find_all("span", {"class" : "ingredient"})
                ingredients = [(*map(lambda ele:ele.get_text(), ingredient_elements))]
                for ingredient in ingredients:         
                    writer.writerow([recipe_link, recipe_name, ingredient])
    f.close()