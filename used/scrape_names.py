#Team: HackALink
#Names of the S&P 500 Companies --> List
#Source: Wikipedia
#Number of Companies more than 500 (504)
#Page Version Date --> 28 December 2015

import wikipedia
import bs4
from bs4 import BeautifulSoup
import urllib2

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
for each in allNames:
	if(counter == 10):
		break
	try:
		summary = wikipedia.page(each)
	except wikipedia.exceptions.DisambiguationError:
		a = wikipedia.search(each)
		summary = wikipedia.page(a[0])
	
	categories = summary.categories

	for x in range(0, len(categories), 1):
		if("articles" in categories[x] or "Articles" in categories[x] or "dates from" in categories[x] or "Companies listed on the New York Stock Exchange" in categories[x]
			or "Wikidata" in categories[x]):
			categories[x] = ""
	print((categories))
	print
	counter = counter + 1



