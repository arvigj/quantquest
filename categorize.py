import wikipedia
from spacy.en import English
import Company

base = {}

#TODO populate base dict with cases
base['location'] = []
base['industry'] = []
base['time'] = []
base['products'] = []

companies = []

with open("names.txt") as file:
    for line in file.readlines():
        companies.append(line)

for c in companies:
    print c

pages = []

for comp in companies:
    try:
        pages.append(wikipedia.page(comp))
    except wikipedia.exceptions.DisambiguationError:
        query = wikipedia.search(each)
        pages.append(wikipeida.page(query[0]))

#function to get category max
def cat_max(cat_entry):
    cat_entry = unicode(cat_entry)
    sim_val = 0
    sim_cat = ''
    for label in base.keys:
        label_max = 0
        for case in label:
            case = unicode(case)
            check = nlp(cat_entry).similarity(nlp(case)) > label_max
            if (check > label_max):
                label_max = check
        if label_max > sim_val:
            sim_cat = label

    return sim_cat

companies_obj = []

for company in pages:
    companies_obj.append(Company(comany.name))
    for category in company.categories:
        label = cat_max(category)
        companies_obj[-1].add_parameter(label,category)


