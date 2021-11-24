from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import *
import json
from pprint import pprint
import pandas as pd

### installing chrome manager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://maharerait.mahaonline.gov.in")
tab = driver.find_elements_by_css_selector(".search-pro-details")
tab[0].click()
driver.find_element_by_css_selector(".col-md-7.col-sm-7 #Promoter").click()
advance_search = driver.find_element_by_css_selector("#btnAdvance")
advance_search.click()

### select state
state_select = driver.find_element_by_css_selector(".col-md-3.col-sm-3 #State").click()
ss = driver.find_elements_by_css_selector(".col-md-3.col-sm-3 #State option")
ss[3].click()
sleep(1)
### select district
district_select = driver.find_element_by_css_selector(".col-md-3.col-sm-3 #District").click()
dist = driver.find_elements_by_css_selector(".col-md-3.col-sm-3 #District option")
for d in range(len(dist)):
    if dist[d].text == "Pune":
        dist[d].click()
    # if dist[d].text == "Mumbai City": dist[d].click()
sleep(1)

### project type select
ptype = driver.find_element_by_css_selector(".col-md-3.col-sm-3 #PType").click()
ptype_option = driver.find_elements_by_css_selector(".col-md-3.col-sm-3 #PType option")
for p in range(len(ptype_option)):
    if ptype_option[p].text == "Residential": ptype_option[p].click()

driver.find_element_by_css_selector(".row.text-center #btnSearch").click()

pages_str = driver.find_element_by_css_selector(".col-md-3.col-sm-3.text-center").text

t = pages_str.split(" T")

tot = t[1].split(":")
totalnumber_pages = int(tot[1])


def getList(dict):
    return list(dict.keys())

### list of features

vf=['Information Type','Name','Organization Type','Description For Other Type Organization','Do you have any Past Experience ?','Block Number',
    'Building Name','Street Name','Locality','Land mark','State/UT','Division','District','Taluka','Village','Pin Code','Office Number','Website URL',
    'Project Name','Project Status','Proposed Date of Completion','Revised Proposed Date of Completion','Litigations related to the project ?',
    'Project Type','Are there any Promoter(Land Owner/ Investor) (as defined by MahaRERA Order) in the project ?',
    'Plot Bearing No / CTS no / Survey Number/Final Plot no.','Boundaries East','Boundaries West','Boundaries North','Boundaries South',
    'State/UT','Division','District','Taluka','Village','Street','Locality','Pin Code','Area(In sqmts)','Total Building Count',
    'Sanctioned Buildings Count','Proposed But Not Sanctioned Buildings Count','Aggregate area(In sqmts) of recreational open space',
    'Built-up-Area as per Proposed FSI (In sqmts) ( Proposed but not sanctioned) ( As soon as approved, should be immediately updated in Approved FSI)',
    'Built-up-Area as per Approved FSI (In sqmts)','TotalFSI','Bank Name','IFSC Code','Extended Date of Completion','House Number','Father Full Name','Last Name']

new = ['Extended Date of Completion','House Number','Father Full Name','Last Name']
data_dict = {}
Litigation_dict={}

for page in range(0, totalnumber_pages):

    district_select = driver.find_element_by_css_selector(".col-md-3.col-sm-3 #District").click()
    dist = driver.find_elements_by_css_selector(".col-md-3.col-sm-3 #District option")
    for d in range(len(dist)):
        if dist[d].text == "Pune":
            dist[d].click()
        # if dist[d].text == "Mumbai City": dist[d].click()
    list_projects = driver.find_elements_by_css_selector(
        '#DivBind .x_content .grid-wrap .table.table-striped.grid-table tbody tr')
    link = driver.find_elements_by_xpath("//a[contains(text(),' View')]")


    #### Rera id
    ### rera id
    rera_id_list=[]
    rera_id_selector =  driver.find_elements_by_css_selector(".grid-cell:nth-child(7) a:nth-child(2)")
    for rera in rera_id_selector:
        rera_id = rera.get_attribute('data-docname')
        rera_id_list.append(rera_id)
# print(rera_id_list)



    cc=0
    for gy in range(len(link)):
        cc+=1
        href = link[gy].get_attribute('href')
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(href)
        sleep(1)
        try:

            hola = []
            realestate_datadict = {}
            dert = driver.find_elements_by_css_selector('.col-sm-3')
            for ko in dert:
                if ko.text is "":
                    continue
                else:
                    hola.append(ko.text)

            for ind, val in enumerate(hola):
                if val in realestate_datadict.keys():
                    if val in vf:realestate_datadict[val].append([hola[ind+1]])
                    else:
                        pass
                else:
                    if val in vf:
                        realestate_datadict[val]=[]
                    else:
                        realestate_datadict[hola[ind-1]]=[val]

            for k,v in realestate_datadict.items():
                if not v:v.append("NULL")

            for key_ls in vf:
                if len(realestate_datadict) < len(set(vf)):
                    if key_ls not in realestate_datadict.keys():
                        realestate_datadict[key_ls]=[]
                        realestate_datadict[key_ls].append("NULL")
                else:
                    keys_list = getList(realestate_datadict)
                    for dictkeys in keys_list:
                        if dictkeys not in set(vf):
                            realestate_datadict.pop(dictkeys)
            for k, v in realestate_datadict.items():
                if len(v) > 1:
                    v=v[0]
                    realestate_datadict[k]=[v]
                else:continue

            # uy=driver.find_element_by_css_selector('#DivCaseDetails > div')

            realestate_datadict['Rera ID']=rera_id_list[gy]
            # pprint(realestate_datadict)
            try:
                driver.find_element_by_css_selector('#DivCaseDetails > label')
                # realestate_datadict["Litigation_Project_Name"]=["Null"]
                # realestate_datadict["Litigation_Court_Name"]=["Null"]
                # realestate_datadict["Litigation_Case_Number"]=["Null"]
                # realestate_datadict["Litigation_Case_Type"]=["Null"]
                # realestate_datadict["Litigation_Preventive_Injunction_Interim_Order_is_Passed"]=["Null"]
                # realestate_datadict["Litigation_Petition_Name"]=["Null"]
                # realestate_datadict["Litigation_Other_Petition_Details"]=["Null"]
                # realestate_datadict["Litigation_year"]=["Null"]
                # realestate_datadict["Litigation_Present_Status"]=["Null"]
                # realestate_datadict["Litigation_Documents"]=["Null"]
                print("NO litigration. !!!!!!!!!!!!!!!!!!!!!!!!!!11")
            except:
                opp=driver.find_elements_by_css_selector("#fldindtxt > div.x_panel > table > tbody tr")
                for lp in opp:
                    sx=lp.find_elements_by_css_selector("th")
                    vg=lp.find_elements_by_css_selector("td")
                    print("LENNNNNNNNNNNNNN",len(vg))
                    # for bh in sx:
                    #     print(bh.text)
                    # print("+"*15)
                    Litigation_Project_Name_list=[]
                    Litigation_Court_Name_list=[]
                    Litigation_Case_Number_list=[]
                    Litigation_Case_Type_list=[]
                    Litigation_Preventive_Injunction_Interim_Order_is_Passed_list=[]
                    Litigation_Petition_Name_list=[]
                    Litigation_Other_Petition_Details_list=[]
                    Litigation_year_list=[]
                    Litigation_Present_Status_list=[]
                    Litigation_Documents_list=[]

                    for ml in range(len(vg)):
                        print(vg[ml].text)
                        if ml%10==1:Litigation_Court_Name_list.append(vg[ml].text)
                        elif ml%10==2:Litigation_Case_Number_list.append(vg[ml].text)
                        elif ml%10==3:Litigation_Case_Type_list.append(vg[ml].text)
                        elif ml%10==4:Litigation_Preventive_Injunction_Interim_Order_is_Passed_list.append(vg[ml].text)
                        elif ml%10==5:Litigation_Petition_Name_list.append(vg[ml].text)
                        elif ml%10==6:Litigation_Other_Petition_Details_list.append(vg[ml].text)
                        elif ml%10==7:Litigation_year_list.append(vg[ml].text)
                        elif ml%10==8:Litigation_Present_Status_list.append(vg[ml].text)
                        elif ml%10==9:Litigation_Documents_list.append(vg[ml].text)
                        elif ml%10==0:Litigation_Project_Name_list.append(ln.text).append(vg[ml].text)
                        else:print("LOVELYYYYYYYYYYYYYYYYY")

                    realestate_datadict["Litigation_Project_Name"]=Litigation_Project_Name_list
                    realestate_datadict["Litigation_Court_Name"]=Litigation_Court_Name_list
                    realestate_datadict["Litigation_Case_Number"]=Litigation_Case_Number_list
                    realestate_datadict["Litigation_Case_Type"]=Litigation_Case_Type_list
                    realestate_datadict["Litigation_Preventive_Injunction_Interim_Order_is_Passed"]=Litigation_Preventive_Injunction_Interim_Order_is_Passed_list
                    realestate_datadict["Litigation_Petition_Name"]=Litigation_Petition_Name_list
                    realestate_datadict["Litigation_Other_Petition_Details"]=Litigation_Other_Petition_Details_list
                    realestate_datadict["Litigation_year"]=Litigation_year_list
                    realestate_datadict["Litigation_Present_Status"]=Litigation_Present_Status_list
                    realestate_datadict["Litigation_Documents"]=Litigation_Documents_list


                        # print(ln.text)
            print("+"*15)
            pprint(realestate_datadict)
            print("Length of litigation dict",len(litigation_dict.keys()))
            fut = getList(realestate_datadict)
            print("LENGHT OF FINALE dict", len(fut))

            if not len(data_dict):
                data_dict=realestate_datadict.copy()
            else:
                ko = getList(realestate_datadict)
                for c in ko:
                    data_dict[c].extend(realestate_datadict[c])

            print(cc)
            print("*" * 100)
        except:
            pass

        # sleep(1)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    next_page = driver.find_element_by_css_selector(".col-md-5.col-sm-5.text-center #btnNext").click()
    sleep(1)

ser = {}
dttt=sorted(data_dict)
for j in dttt:
    ser[j]=data_dict[j]

import json
with open("ThaneREALjson.json", "w") as outfile:
    json.dump(ser, outfile)

try:
    dtt = pd.DataFrame(ser,ignore_index = True)
    dtt.to_excel('RealestateData.xlsx')
except:
    print("NOT POSSIBLE")

try:
    df = pd.DataFrame.from_dict(ser, orient='index')
    df = df.transpose()
    df.to_excel('thaneRealestateData.xlsx')
except:
    print("ANOTHER NOT PSO")


