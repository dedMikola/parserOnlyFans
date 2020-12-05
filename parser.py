from selenium import webdriver
from bs4 import BeautifulSoup
import requests


# set browser settings
option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled', False)
option.set_preference('general.useragent.override',
                          'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36')


driver = webdriver.Firefox(executable_path='/Users/ded/Develop/SGparser/geckodriver', options=option)
driver.get('https://www.suicidegirls.com/members/asswithsass/followers/')


try:
    while True:
        driver.find_element_by_xpath('//*[@id="load-more"]').click()
except:
        requiredHtml = driver.page_source


soup = BeautifulSoup(requiredHtml, 'html.parser')
soupLinks = soup.select('article div h3 a')

listLinks = []
for key in soupLinks:
    listLinks.append(key)

newListLinks = []
for i in listLinks:
    newListLinks.append(str(i).replace('<a href="', 'https://www.suicidegirls.com'))

usersLinks = []
for x in newListLinks:
    z = x.rfind('">')
    newSlice = x[0:z]
    usersLinks.append(newSlice)


HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0', 'accept':'*/*'}

OfUsersData =[]
for URL in usersLinks:
    r = requests.get(URL, headers=HEADERS, params=None)
    soup = BeautifulSoup(r.text,'html.parser')
    link = soup.select('.icon-onlyfans')
    OfUsersData.append(link)
