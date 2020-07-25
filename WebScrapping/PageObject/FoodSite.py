import WebScrapping.WebsiteDriver as web
search_box="input.search.form-control"
search_button="div.row .btn.btn-block"
resturant_lists="div .listing"
resturant_name="div>h1"
menuitme="div.menu__list li.d-flex>div>div.d-flex a>span"
pricelist="div.menu__list li.d-flex div.menu__price>span:nth-of-type(3)"


def clickonSearchButton():
    web.clickOnElement(search_button)

def searchbyvalue(text):
    web.SetText(search_box,text)
    clickonSearchButton()
    
def getresurantList():
    return web.FindElements(resturant_lists)
def clickonresturant(x):
    web.FindElements(resturant_lists)[x].click()
def getresturantListcount():
    resturant=web.FindElements(resturant_lists)
    return len(resturant)
def getresturantname():
    return web.GetElementText(resturant_name)

def getitem():
    return web.FindElements(menuitme)
def getpricelist():
    return web.FindElements(pricelist)
def wait():
    web.wait()
def navigateback():
    web.back()

