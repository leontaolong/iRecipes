
# coding: utf-8

# In[223]:


import requests
from bs4 import BeautifulSoup

# Pages to be scaped
pages = ['https://www.yummly.com/recipes/lunch',
        'https://www.yummly.com/recipes/dinner',
        'https://www.yummly.com/browse/recommended',
        'https://www.yummly.com/browse/seasonal',
        'https://www.yummly.com/browse/popular-now',
        'https://www.yummly.com/browse/quick-and-easy']

base_url = 'https://www.yummly.com/#recipe/'

for page in pages:
    
    # Request webpage information
    page_req = requests.get(page)
    page_soup = BeautifulSoup(page_req.text, 'html.parser')
    
    recipe_grids = page_soup.find_all("div", {"class" : "single-recipe"})
    for recipe_grid in recipe_grids:
        recipe_link = base_url + recipe_grid.get('data-url')
        
        recipe_req = requests.get(recipe_link)
        recipe_soup = BeautifulSoup(recipe_req.text, 'html.parser')
        
        
        print(recipe_link)





# In[224]:


# driver = webdriver.Chrome('/Users/leon/desktop/chromedriver')
# driver.get('https://www.yummly.com/#recipe/Loaded-Bacon_-Cheddar_-and-Ranch-French-Fries-2037020')

# elements = driver.find_elements_by_xpath("//div[@class='RecipeContainer']/div")

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# print(len(elements))
# ActionChains(driver).move_to_element(element).perform()



# while True:
#     driver.execute_script("window.scrollBy(0, 1000);")
#     time.sleep(1)
#     hover = ActionChains(driver).move_by_offset(400,400)
#     hover.perform()
# driver.execute_script("Document.getElementsByClassName('RecipeContainer').animate({ scrollTop: '100px' })")

    

