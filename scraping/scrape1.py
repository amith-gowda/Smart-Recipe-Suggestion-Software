from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request, urllib.parse, urllib.error




driver = webdriver.Chrome("../data/chrome-driver/chromedriver")

recipes=[] #List to store name of the product
ingredients=[] #List to store price of the product
driver.get("https://www.allrecipes.com/recipe/19694/green-bean-bundles/?internalSource=rotd&referringId=76&referringContentType=Recipe%20Hub")


content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'recipe-summary clearfix'}):
    rec=a.find('h1', attrs={'class':'recipe-summary__h1'})
    ing=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    recipes.append(rec.text)
    ingredients.append(ing.text)
    
df = pd.DataFrame({'Recipe Name':recipes,'Ingredients':ingredients}) 
df.to_csv('all-recipes.csv', index=False, encoding='utf-8')
