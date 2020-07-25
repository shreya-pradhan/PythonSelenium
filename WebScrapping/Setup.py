import selenium
import chromedriver_binary
from selenium import webdriver as wb
application="https://foodmandu.com/";
def Setup():
    drive=wb.Chrome()
    drive.maximize_window()
    drive.get(application)
    drive.implicitly_wait(200)
    return drive
