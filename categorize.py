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
        for case in label:
            case = unicode(case)
            check = nlp(cat_entry).similarity(nlp(case)) > label_max
            if (check > label_max):
                label_max = check
        if label_max > sim_val:
            sim_cat = label
            sim_val = label_max
    #val = 0.5 #confidence level
    #if (sim_val < val):
    #   return 'misc'
    return sim_cat

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

for c in companies:
    print c

pages = []

for comp in companies:
    try:
        pages.append(wikipedia.page(comp))
    except wikipedia.exceptions.DisambiguationError:
        query = wikipedia.search(comp)
        pages.append(wikipedia.page(query[0]))
    except wikipedia.exceptions.PageError:
        pass

companies_obj = []
for company in pages:
    companies_obj.append(Company(company.title))
    for category in company.categories:
        label = cat_max(category)
        companies_obj[0].add_parameter(label,category)


