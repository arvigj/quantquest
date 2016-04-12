import wikipedia
from spacy.en import English
from Company import Company
import sys

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

with open(sys.argv[1]) as file:
    for line in file.readlines():
        companies.append(line)

pages = []

numOfComp = 0
for comp in companies:
    print(numOfComp)
    # if(numOfComp == 50):
    #     break
    try:
        if("Allergan plc" == comp):
            pages.append(wikipedia.page("Allergan, Inc."))
        else:
            pages.append(wikipedia.page(comp))
    except wikipedia.exceptions.DisambiguationError:
        query = wikipedia.search(comp)
        pages.append(wikipedia.page(query[0]))
    except wikipedia.exceptions.PageError:
        pass
    # numOfComp = numOfComp + 1

companies_obj = []
for company in pages:
    print(company.title)
    companies_obj.append(Company(company.title))
    for category in company.categories:
        # print(category)
        if(check_categories(category)):
           continue
        label = cat_max(category)
        companies_obj[-1].add_parameter(label,category)

compIndDic = {}

# print(companies_obj[0].data)
for each in companies_obj:
    for values in each.data:
        if(values == 'industry'):
            compIndDic[each.name] = each.data[values]


import json
with open('industry.json', 'w') as refer_files:
    json.dump(compIndDic, refer_files)
