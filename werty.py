# -*- coding: utf-8 -*-
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import *
import json
from pprint import pprint
import pandas as pd
from selenium.webdriver.common.keys import Keys
import threading
import concurrent.futures
from pprint import pprint
from newspaper import Article
import codecs
##### USERSSSSSSSSSSSSSS
# user="yogesh.aurumproptech@gmail.com"
# pa='proptech1492'
# # #
# user="rahul.shinde0904@gmail.com"

# user="ayushimathur434@gmail.com"
# pa="mathur123"

user = "aurumprop17@gmail.com"
pa='aurum@1234'

# zayleigh@fqreleased.com
# user="jayce4@fqreleased.com"
# pa="proptech123#"
def scroll_to_bottom(driver):

    old_position = 0
    new_position = None

    while new_position != old_position:
        # Get old scroll position
        old_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))
        # Sleep and Scroll
        sleep(1)
        driver.execute_script((
                "var scrollingElement = (document.scrollingElement ||"
                " document.body);scrollingElement.scrollTop ="
                " scrollingElement.scrollHeight;"))
        # Get new position
        new_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))

# ### installing chrome manager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.indextap.com/")
login = driver.find_element_by_css_selector("#navbarNav > ul > li:nth-child(5) > a")
loginclick=login.get_attribute("href")
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(loginclick)
user_insert = driver.find_element_by_css_selector("#loginform-email")
user_insert.send_keys(user)
sleep(1)
pass_insert=driver.find_element_by_css_selector("#loginform-password")
pass_insert.send_keys(pa)
scroll_to_bottom(driver)
sleep(2)
h=driver.find_element_by_name('login-button')
h.click()

sleep(2)

sale_button=driver.find_elements_by_css_selector(".custom-button-group.mb-5.btn-group-toggle .btn.btn-secondary ")
sale_button[1].click()
href_cities = driver.find_elements_by_css_selector(".col-12.col-md-2.col-sm-6.mb-5 a")
aa=href_cities[1].get_attribute('href')
driver.get(aa)
driver.find_element_by_css_selector("#searchform-type > label:nth-child(2)").click()
driver.find_element_by_css_selector('#search-form > div:nth-child(4) > span > span.selection > span').click()
sleep(1)

list_pr=driver.find_elements_by_css_selector('#select2-searchform-locality-results li')

locality_name="Baramati"
ab=[]
for i in list_pr:
    ab.append(i.text)

print(ab)

sleep(1)
print(ab)

driver.find_element_by_xpath(f'//*[@id="select2-searchform-locality-results"]/li[contains(text(),"{locality_name}")]').click()
sleep(1)

ft = driver.find_elements_by_css_selector("#index-data-container .row.transactions")
print(len(ft))
##### important variables and data structures
data_dict={}
oi = {}

locality=[]
dated=[]
building=[]
wingnumber=[]
flat=[]
area=[]

a=0
b=0
y=0
nn=0

ft[0].click()
sleep(1)
try:
    sleep(2)
    driver.find_element_by_xpath('//*[@id="purchase-pop-container"]/div/div/a[2]').click()
    print("CLICCCCCCCCCCCCCCKKKKKKKKKKEEEEEEEEEEEDDDDDDDDDD")
except:
    pass
ht=[]
fdd=[]
ft[22].click()
sleep(2)

# ft[0].click()
# sleep(2)

qw= driver.find_elements_by_css_selector(".row.mb-2 div")
for p in qw:
    if p.text == "":
        pass
    else:
        ht.append(p.text)
        fdd.append(p.text)
        print(p.text)

ftt={}

description= driver.find_elements_by_css_selector('.col-12.px-md-3.pt-md-3.px-2.pt-2 p')
prop_desc=driver.find_elements_by_css_selector(".col-12.px-md-3.pt-md-3.px-2.pt-2 h2")
print(len(description))
print("00000",description[0].text)
ht.append(prop_desc[0].text)
ht.append(description[0].text)
fdd.append(prop_desc[1].text)
print("1111",prop_desc[1].text)
fdd.append(description[1].text)
oi.update({'23':ht})
ftt.update({'23':fdd})
print(f"{locality_name} ")
pprint(oi)
print("*"*30)
pprint(ftt)

print("*"*30)

# import json
# with open("Baneryyyy_Index.json", "w") as outfile:
#     json.dump(oi, outfile)

# with open('Baneryyyy_Index.json',"w",encoding="utf8") as outfile:
#     json.dump(oi,outfile)

# open('Baneryyyy_Index.json',"w",encoding="utf8").write(json.dumps(oi,ensure_ascii=False))
# 19


## Baramati_index.json file doesnt extract any value for 23rd index
## Daund has no data
