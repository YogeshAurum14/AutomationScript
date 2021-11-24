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

# user="yogesh.aurumproptech@gmail.com"
pa='proptech1492'
# # # # # # #
user="rahul.shinde0904@gmail.com"

# user="ayushimathur434@gmail.com"
# pa="mathur123"

# user = "aurumprop23@gmail.com"
# pa='aurum@1234'

# user="toddler49@fqreleased.com"
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
pass_insert=driver.find_element_by_css_selector("#loginform-password")
pass_insert.send_keys(pa)
scroll_to_bottom(driver)
sleep(2)
h=driver.find_element_by_name('login-button')
h.click()

sleep(2)
try:
    sale_button=driver.find_elements_by_css_selector(".custom-button-group.mb-5.btn-group-toggle .btn.btn-secondary ")
    sale_button[1].click()
    print("CSSSSSSS SELECTOR")
except:
    sale_button=driver.find_element_by_xpath('//*[@id="loginform-password"]')
    sale_button.click()
    print("Xpaaaaath")
href_cities = driver.find_elements_by_css_selector(".col-12.col-md-2.col-sm-6.mb-5 a")
aa=href_cities[1].get_attribute('href')
driver.get(aa)
driver.find_element_by_css_selector("#searchform-type > label:nth-child(2)").click()
driver.find_element_by_css_selector('#search-form > div:nth-child(4) > span > span.selection > span').click()
sleep(1)
list_pr=driver.find_elements_by_css_selector('#select2-searchform-locality-results li')
locality_name='Balewadi'
ab=[]
for i in list_pr:
    ab.append(i.text)
sleep(1)

driver.find_element_by_xpath(f'//*[@id="select2-searchform-locality-results"]/li[contains(text(),"{locality_name}")]').click()
sleep(1)

ft = driver.find_elements_by_css_selector("#index-data-container .row.transactions")
# print(len(ft))

##### important variables and data structures
data_dict={}


locality=[]
dated=[]
building=[]
wingnumber=[]
flat=[]
area=[]
oi = {}

a=0
b=0
y=0
nn=38
clicked=0
for j in range(len(ft)):

    ht=[]
    y+=1
    a=a+1
    b=b+2
    if j >= nn:
        oi = {}
        ft[j].click()
        clicked+=1
        sleep(2)
        try:
            sleep(1)
            # driver.find_element_by_xpath("/html/body/section[2]/div/div[2]/div[1]/div[9]/div/div/div/a[2]").click()
            driver.find_element_by_xpath('//*[@id="purchase-pop-container"]/div/div/a[2]').click()
            print("CLICCCCCCCCCCCCCCKKKKKKKKKKEEEEEEEEEEEDDDDDDDDDD")
        except:
            pass
        try:
            description= driver.find_elements_by_css_selector('.col-12.px-md-3.pt-md-3.px-2.pt-2 p')
            prop_desc=driver.find_elements_by_css_selector(".col-12.px-md-3.pt-md-3.px-2.pt-2 h2")
            # print(len(prop_desc),len(description))
            # print(prop_desc[clicked-1].text)
            # print(description[clicked-1].text)
            qw= driver.find_elements_by_css_selector(".row.mb-2 div")
            for p in qw:
                if p.text == "":
                    pass
                else:
                    ht.append(p.text)

                    print(p.text)
            ht.append(prop_desc[clicked-1].text)
            ht.append(description[clicked-1].text)
            # print(ht)
            if j==nn+1:
                pass
            elif ((len(ht)<4) and (j != (0))):
                # pass
                break
            else:
                oi.update({y:ht})
        except:
            print("NOT GOTTT DATAAAA")
        pprint(oi)
        # description= driver.find_elements_by_css_selector('.col-12.px-md-3.pt-md-3.px-2.pt-2 p')
        # prop_desc=driver.find_elements_by_css_selector(".col-12.px-md-3.pt-md-3.px-2.pt-2 h2")
        # print(len(prop_desc),len(description))
        # print(prop_desc[clicked-1].text)
        # print(description[clicked-1].text)

        # print(len(prop_desc),len(description))
        # ht.append(prop_desc[clicked-1].text)
        # ht.append(description[clicked-1].text)



        # date=driver.find_elements_by_css_selector(" .col-md-2.col-6.p-3.text-center.text-md-left")
        # building_name = driver.find_elements_by_css_selector(".col-md-3.col-10.p-3.text-truncate.text-center.text-md-left")
        # wing = driver.find_elements_by_css_selector(".col-md-2.col-4.p-3.text-truncate.text-center.text-md-left")
        # flat_no = driver.find_elements_by_css_selector(".col-md-1.col-4.p-3.text-center.text-md-left")



        # print("Locality",date[b-1].text)
        # print("Date",date[a-1].text)
        # print("Buidling",building_name[j].text)
        # print("Wing",wing[j].text)
        # print("Flat number",flat_no[a-1].text)
        # print("Area",flat_no[b-1].text)
        #
        # if b == len(date):
        #     b=-1

        # locality.append(date[a].text)
        # dated.append(date[b].text)
        # building.append(building_name[j].text)
        # wingnumber.append(wing[j].text)
        # flat.append(flat_no[b].text)
        # area.append(flat_no[a].text)
        #
        # a=b

        # data_dict = {"Locality":locality,
        #              "Date":dated,
        #              "Building_Name":building,
        #              "Wing":wingnumber,
        #              "Flat_no":flat,
        #              "Area":area}

        ############## later code for more rera data update
        # try:
        #     with open("Baner_Index.json","r+") as f:
        #         data = json.load(f)
        #         data.update(oi)
        #         f.seek(0)
        #         json.dump(data,f)
        # except:
        #     pass
        try:
            with open('Balewadi_Index.json',"r+",encoding="utf8") as f:
                data = json.load(f)
                data.update(oi)
                f.seek(0)
                json.dump(data,f,ensure_ascii=False)
                print("SAVEDDDDDDDDDDDDD")

        except:
            pass
        # pprint(data_dict)
        # try:
        #     description= driver.find_element_by_css_selector(".col-12.px-md-3.pt-md-3.px-2.pt-2 p").text
        #     prop_descr=driver.find_element_by_css_selector(".col-12.px-md-3.pt-md-3.px-2.pt-2 h2").text
        #     print(prop_descr)
        #     print(description)
        # except:
        #     print("%%%%%% NOT FOUND %%%%%%%")
        print("*"*15)
    else:
        print("NOT IN RANGEEEEEEEEEEEE")


########## created a new json file
# import json
# # # # with open("Baner1_Index.json", "w") as outfile:
# # # #     json.dump(oi, outfile)
# # #
# open('Balewadi_Index.json',"w",encoding="utf8").write(json.dumps(oi,ensure_ascii=False))

# with open("Anand_Nagar_tapioca.json", "w") as outfile:
#     json.dump(data_dict, outfile)
# pprint(data_dict)

######### updating the already existing json file

# with open("Anand_Nagar_tapioca.json","r+") as f:
#     data = json.load(f)
#     data.update(data_dict)
#     f.seek(0)
#     json.dump(data,f)

# with open("Anand Nagar.json","r+") as f:
#     data = json.load(f)
#     data.update(oi)
#     f.seek(0)
#     json.dump(data,f)


