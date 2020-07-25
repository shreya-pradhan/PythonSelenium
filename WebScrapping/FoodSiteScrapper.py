import WebScrapping.PageObject.FoodSite as site

AllitemLis=[]
item=[]
price=[]
name=[]
application="https://foodmandu.com/";

site.wait()
site.searchbyvalue("Newari")
site.wait()
resturantList=site.getresurantList()
resturantCount=len(resturantList)
for x in range(resturantCount):
    site.clickonresturant(x)
    site.wait()
    name.append(site.getresturantname())
    item=item.append([x.text for x in site.getitem()])
    price=price.append([x.text for x in site.getpricelist()])
    item.append('*')
    price.append('*')
    site.navigateback()



