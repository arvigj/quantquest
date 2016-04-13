
import bs4
from bs4 import BeautifulSoup
import urllib2
from spacy.en import English
from Company import Company
import sys
import wikipedia

#function to get category max
def cat_max(cat_entry):
    cat_entry = unicode(cat_entry)
    sim_val = 0
    sim_cat = ''
    for label in base.keys():
        label_max = 0
        for case in base[label]:
            check = nlp(cat_entry).similarity(nlp(unicode(case)))
            # print(cat_entry, case, check)
            if (check > label_max):
                label_max = check
        if label_max > sim_val:
            sim_cat = label
            sim_val = label_max
    val = 0.55 #confidence level
    if (sim_val < val):
      return 'misc'
    return sim_cat

def check_categories(category):
    if("Dow Jones" in  category or "New York Stock Exchange" in category 
        or "NASDAQ" in category or "Wikidata" in category 
        or "needing additional references" in category
        or "infobox" in category):
        return True
    else:
        return False

base = {}

#TODO populate base dict with cases
base['location'] = ["Based in","Located in"]
base['industry'] = ["Technology Company","Financial","Consulting","Manufacturing"]
base['time'] = ["Established in","Created in"]
base['products'] = ["Produces","Creates","Develops","Provides"]
base['misc'] = []

companies = []
nlp = English()

############################################

wiki = "https://en.wikipedia.org/w/index.php?title=List_of_S%26P_500_companies&oldid=697200065"
page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page, "html.parser")
table = soup.find("table", { "class" : "wikitable sortable" })

allNames = []
numberOfCompanies = 0
i = 1

values = table.findAll("td")
while(numberOfCompanies < 510):
    try:
        allNames.append(values[i].text)
    except:
        pass
    i += 8
    numberOfCompanies += 1

counter = 0
dicRef = {}

for each in allNames:
    dicRef[each] = []

companies_pages = []
for each in allNames:
    try:
        page = wikipedia.page(each)
        companies_pages.append(page)
    except:
        try:
            a = wikipedia.search(each)
            page = wikipedia.page(a[0])
            companies_pages.append(page)
        except:
            companies_pages.append("NA")
    counter = counter + 1

print(len(companies_pages))

companies_obj = []
for i in range(0, 504, 1):
    companies_obj.append(Company(allNames[i]))
    comp_cats = companies_pages[i].categories
    for category in comp_cats:
        if(check_categories(category)):
           continue
        label = cat_max(category)
        companies_obj[-1].add_parameter(label,category)  

print(len(companies_obj))
compIndDic = {}

# print(companies_obj[0].data)
for each in companies_obj:
    for values in each.data:
        if(values == 'time'):
            try:
                a = str(each.data[values][0])
                time_value = (int(filter(str.isdigit, a)))
                compIndDic[each.name] = time_value
            except:
                compIndDic[each.name] = -1

print(compIndDic)
import json
with open('time.json', 'w') as refer_files:
    json.dump(compIndDic, refer_files)



