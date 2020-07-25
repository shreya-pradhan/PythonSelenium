from bs4 import BeautifulSoup
import requests
import selenium
import chromedriver_binary
from selenium import webdriver as wb
import ExcelWriter as writer
menuitme="div.menu__list li.d-flex>div>div.d-flex a>span"
pricelist="div.menu__list li.d-flex div.menu__price>span:nth-of-type(3)"
AllitemLis=[]
item=[]
price=[]
name=[]
driver=wb.Chrome()
driver.maximize_window()
driver.get("https://foodmandu.com/")
driver.implicitly_wait(200)
driver.find_element_by_css_selector('input.search.form-control').send_keys('Newari')
driver.find_element_by_css_selector('div.row .btn.btn-block').click()
driver.implicitly_wait(200)
resturantList=driver.find_elements_by_css_selector('div .listing')
resturantCount=len(resturantList)
for x in range(resturantCount):
    driver.find_elements_by_css_selector('div .listing')[x].click()
    driver.implicitly_wait(200)
    name.append(driver.find_elements_by_css_selector('div>h1'))
    item=item.append([x.text for x in driver.find_elements_by_css_selector(menuitme)])
    price=price.append([x.text for x in driver.find_elements_by_css_selector(pricelist)])
    item.append('*')
    price.append('*')

    driver.back()
writer.CreateWorkBook(name,item,price)

