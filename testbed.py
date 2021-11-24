# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import *
import json
from pprint import pprint
import pandas as pd
from selenium.webdriver.common.keys import Keys
import threading
import concurrent.futures
from pprint import pprint
#
oi={'23': ['Total Price',
        '₹15,00,000',
        'Resale or Primary',
        '-',
        'Per Sq ft',
        '₹2,904',
        'Area Type',
        'carpet',
        'RERA Code',
        'P52100020578',
        'Floor',
        '4',
        'Property Description',
        '1) पालिकेचे नाव:बारामतीइतर वर्णन :, इतर माहिती: गाव मौजे तांदुळवाडी '
        'येथील गट नं.214/अ/1 यासी क्षेत्रफळ 3994.40 चौ.मी. या मिळकतीवर '
        'बांधण्यात येणा-या स्प्रिंग व्हिलेज 1 अॅफोर्डेबल हौसिंग या स्किम मधील '
        'विंग 1 ब्लॉक बी मधील चौथ्या मजल्यावरील फलॅट क्र.401 यासी कार्पेट '
        'क्षेत्र 47.98 चौ.मी. + बाल्कनी क्षेत्र 3.15 चौ.मी. ही फलॅट मिळकत या '
        'करारनाम्याचा विषय असे विभाग क्र.11/2.( ( GAT NUMBER : 214/अ/1 ; ) )']}



# with open(r"D:\python folder\PycharmProjects\pythonProject2\Baner_Index.json","r+") as f:
#     data = json.load(f)
#     pprint(data)
#     data.update(oi)
#     f.seek(0)
#     json.dump(data,f)

with open('Baramati_Index.json',"r+",encoding="utf8") as f:
        data = json.load(f)
        data.update(oi)
        f.seek(0)
        json.dump(data,f,ensure_ascii=False)

# from textblob import TextBlob
#
# # print(blob.detect_language())
#
# p="पालिकेचे नाव:इतर वर्णन :(विभाग नं.32/502 दर रु.39600/- प्रति चौ.मी.) घोरपडी येथील सि.टी.एस.नं.2/3ते2/9 बी.जे.रोड या मिळकतीवरील डि.एस.के.फ्रान्जीफॅनी मधील विंग बी मधील दुसऱ्या मजल्यावरील फलॅट नं.202 यांसी क्षेत्र 86.21 चौ.मी. म्हणजेच 928 चौ.फुट कारपेट लगतचे टेरेस क्षेत्र 16.63 चौ.मी.म्हणजेच 179 चौ.फुट कारपेट असे एकुण कापेट क्षेत्र 102.84 चौ.मी. म्हणजेच 1107 चौ.फुट तसेच स्टील्ट फलोअर मधील कार पार्किंग नं.10 यांसी क्षेत्र 9.29 चौ.मी. म्हणजेच 100 चौ.मी."
#
# v=p.split()
#
# stringy=""
#
# for i in v:
#         print(i)
#         blob = TextBlob(i)
#         try:
#                 print(blob.translate(to='en'))
#                 stringy=stringy+" "+blob.translate(to='en')
#         except:
#                 print(i)
#                 stringy=stringy+" "+i
#         print("*********")



# # # import pandas as pd
# # import json
# # #
# # # d = {3:"ww",4:"rr"}
# # # #
# # # # with open("aa.json","r+") as file:
# # # #     data = json.load(file)
# # # #     data.update(d)
# # # #     file.seek(0)
# # # #     json.dump(data,file)
# # #
# # # # with open('aa.json') as data_file:
# # # #     data = json.load(data_file)
# # # #     for element in data:
# # # #         del element["1"]
# # # import re
# # # jj = open(r'C:\Users\DELL\PycharmProjects\pythonProject2\aa.json',)
# # #
# # # data = json.load(jj)
# # #
# # # ko = data.keys()
# # # f = len(data.keys())
# # # r = "Moto e7 plus"
# # # for i,k in data.items():
# # #     if i == "Vivo Y11 2019 (3 GB/32 GB)":
# # #         print("YES")
# # #     else:
# # #         continue
# # # print(f)
# # #
# # # mo = []
# # # for k,v in data.items():
# # #     ee = re.findall(r,k,re.IGNORECASE)
# # #     if len(ee)>0:
# # #         mo.append([k,v])
# # #     else:
# # #         continue
# # # print(mo)
# # # f= {1:["2"]}
# # # c = {2:"1"}
# # # # print(f.keys())
# # # if 1 in f: f[1].append("3")
# # # f.update(c)
# # from pprint import pprint
# # f = [1,2,3,4,5]
# # ff={}
# # # ff = zip(range(0,len(f)),f)
# # # pprint(ff)
# # for i,v in enumerate(f):
# #     ff[i]=v
# # # pprint(ff)
# # # with open("RERA_link.json","r") as lnk:
# # #     dd=json.load(lnk)
# # #
# # # from webdriver_manager.chrome import ChromeDriverManager
# # # from selenium import webdriver
# # # from time import *
# # # # import json
# # # driver = webdriver.Chrome(ChromeDriverManager().install())
# #
# # dit = {}
# # dt = {"4":22}
# # # print(type(dit))
# # g = ["name","y","age",12,"city","mumbai","citizen","indian","criminal charge","no","hobby","footbal and singing"]
# # t = ["name","t","age",32,"city","mbai","citizen","indian","criminal charge","no","hobby","footbal and singing"]
# # if len(dt)==0:print("NNNNN")
# # else:
# #     print("YYYY")
# # for i,v in enumerate(g):
# #     if i%2==0:dit[v]={}
# #     else:dit[g[i-1]]=[v]
# # # print("Eazrlier",dit)
# # for k,x in enumerate(t):
# #     if t[k] in dit.keys():
# #         dit[t[k]].append(t[k+1])
# #         # print("On the verge",dit)
# # print("Final",dit)
# # import pandas as pd
# # df = pd.DataFrame(dit)
# # # print(df)
# #
# # vf=['Information Type','Name','Organization Type','Description For Other Type Organization','Do you have any Past Experience ?','Block Number',
# #     'Building Name','Street Name','Locality','Land mark','State/UT','Division','District','Taluka','Village','Pin Code','Office Number','Website URL',
# #     'Project Name','Project Status','Proposed Date of Completion','Revised Proposed Date of Completion','Litigations related to the project ?',
# #     'Project Type','Are there any Promoter(Land Owner/ Investor) (as defined by MahaRERA Order) in the project ?',
# #     'Plot Bearing No / CTS no / Survey Number/Final Plot no.','Boundaries East','Boundaries West','Boundaries North','Boundaries South',
# #     'State/UT','Division','District','Taluka','Village','Street','Locality','Pin Code','Area(In sqmts)','Total Building Count',
# #     'Sanctioned Buildings Count','Proposed But Not Sanctioned Buildings Count','Aggregate area(In sqmts) of recreational open space',
# #     'Built-up-Area as per Proposed FSI (In sqmts) ( Proposed but not sanctioned) ( As soon as approved, should be immediately updated in Approved FSI)',
# #     'Built-up-Area as per Approved FSI (In sqmts)','TotalFSI','Bank Name','IFSC Code']
# #
# # if 'Last Name' in vf:
# #     print("Y")
# # else:print("NOOOO")
# #
# # tt = []
# # if not tt:
# #     # print("EMPTY")
# #     tt.append('NULL')
# #     # print(tt)
# # # else:print("NOT EMPTY")
# # g = {1:'2',2:"4"}
# # # print(len(g))
# #
# # vf=['Information Type','Name','Organization Type','Description For Other Type Organization','Do you have any Past Experience ?','Block Number',
# #     'Building Name','Street Name','Locality','Land mark','State/UT','Division','District','Taluka','Village','Pin Code','Office Number','Website URL',
# #     'Project Name','Project Status','Proposed Date of Completion','Revised Proposed Date of Completion','Litigations related to the project ?',
# #     'Project Type','Are there any Promoter(Land Owner/ Investor) (as defined by MahaRERA Order) in the project ?',
# #     'Plot Bearing No / CTS no / Survey Number/Final Plot no.','Boundaries East','Boundaries West','Boundaries North','Boundaries South',
# #     'State/UT','Division','District','Taluka','Village','Street','Locality','Pin Code','Area(In sqmts)','Total Building Count',
# #     'Sanctioned Buildings Count','Proposed But Not Sanctioned Buildings Count','Aggregate area(In sqmts) of recreational open space',
# #     'Built-up-Area as per Proposed FSI (In sqmts) ( Proposed but not sanctioned) ( As soon as approved, should be immediately updated in Approved FSI)',
# #     'Built-up-Area as per Approved FSI (In sqmts)','TotalFSI','Bank Name','IFSC Code','Extended Date of Completion','House Number','Father Full Name','Last Name']
# # # print(len(set(vf)))
# #
# # g = ["w","r",'t']
# # fg = {"a":[1],"w":[2],"r":[0]}
# # # for k in g:
# # #     if k not in fg.keys():
# # #         fg[k]=[]
# # #         fg[k].append(2)
# # # # print(fg)
# # # fg.pop('w')
# # # print(fg)
# # # cv = [fg]
# # # print(cv, type(cv))
# #
# #
# # def getList(dict):
# #     return list(dict.keys())
# #
# # # Driver program
# # # dict = {1: 'Geeks', 2: 'for', 3: 'geeks'}
# # # print(getList(fg))
# # p=[1,1,2,3,4,5,3,5,6,7]
# # w={1:2,2:3,3:4,4:5,5:6,9:10}
# # u=getList(w)
# # for i in u:
# #     if i not in set(p):
# #         w.pop(i)
# #         print(w)
# # print(w)
# #
# # qw={"s":[1],"t":[5]}
# # op={"s":[6],"t":[8]}
# # oo={"s":[0],"t":[8]}
# # de = qw.copy()
# # if not len(de):
# #     de = qw.copy()
# # else:
# #     ko = getList(op)
# #     for i in ko:
# #         de[i].extend(op[i])
# # pprint(de)
# # import pandas as pd
# # # df = pd.DataFrame(qw)
# # # dd = pd.DataFrame(op)
# # # df1=pd.DataFrame(oo)
# # # new_df=df.append(dd,ignore_index = True)
# # # new_df=new_df.append(df1,ignore_index = True)
# # df = pd.DataFrame()
# # df = df.append(pd.DataFrame(qw),ignore_index = True)
# # print(df)
# # print("*"*14)
# # df = df.append(pd.DataFrame(op),ignore_index = True)
# # df.to_excel('Teeeest.xlsx')
# #
# #
# # hu = getList(qw)
# # fu = list(df.columns)
# # for i,v in enumerate(hu):
# #     if v == fu[i]:print("YES")
# #     else:print("No")
# # if hu==fu:print("YESSS")
# # else:print("NO")
# #
# # print(df.shape)
# #
# # f=[1,2,3,55,7,2,7,0,2,8]
# # if len(f)>1:
# #     f=f[-1]
# # print(f)
# #

# # gh = pd.DataFrame(ff)
# try:
#     df = pd.DataFrame.from_dict(ff, orient='index')
#     df = df.transpose()
#     df.to_excel('HstateData.xlsx')
# except:
#     print("ANOTHER NOT PSO")
# # print(gh.head())

########## scraping goooogle ##############
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium import webdriver
# from time import *
# import json
# from pprint import pprint
# import pandas as pd
# from selenium.webdriver.common.keys import Keys
# from pandas import read_excel
#
# seet="Sheet1"
# driver = webdriver.Chrome(ChromeDriverManager().install())
# df = read_excel(r'D:\python folder\PycharmProjects\pythonProject2\HOLAestateData.xlsx', sheet_name = seet)
#
# locality = df['Locality']
# coord_dict={}
# locality_l = list(locality.unique())
# for i,v in enumerate(locality_l):
#     print(i,"*"*10,v)
#     search_string=f"coordinate of {v}"
#     driver.get("https://www.google.com/search?q=" +
#                                      search_string + "&start=")
#     sleep(1)
#     try:
#         coord=driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div[1]').text
#         coord_dict[coord]=v
#         pprint(coord_dict)
#         print("*"*20)
#     except:pass
###################### To create an empty json file
# import json
# from pandas import read_excel
# import pandas as pd
# doodle={}
# jsn_ob=json.dumps(doodle)
# with open("YOLO.json","w") as a:
#         a.write(jsn_ob)



# seet="Sheet1"
# df = read_excel(r'D:\python folder\PycharmProjects\pythonProject2\HOLAestateData.xlsx', sheet_name = seet)
# locality = df['Locality']
#
# with open(r'D:\python folder\PycharmProjects\pythonProject2\Coordinates.json') as f:
#   data = json.load(f)
# dg = pd.DataFrame()
# ferr={}
# cm=0
# def getList(dict):
#     return list(dict.values())
# vv = getList(data)
# for ind,val in locality.iteritems():
#
#     for i,v in data.items():
#         if val.lower()==v.lower():
#             cm+=1
#             dg['locality']=[val]
#             dg['coord']=[i]
#
#             # print(dg)
#         else:
#             cm+=1
#             dg['locality'] = ['Null']
#             dg['coord'] = ['Null']
#
#
# print(dg)
# print(cm)
#
#
#
#
#





