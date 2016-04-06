import wikipedia
from urlparse import urlparse
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
dicRef = {}
dicRef[allNames[0]] = []
dicRef[allNames[1]] = []

for each in allNames:
	if(counter == 2):
		break
	try:
		page = wikipedia.page(each)
	except wikipedia.exceptions.DisambiguationError:
		a = wikipedia.search(each)
		page = wikipedia.page(a[0])

	for url in page.references:
		o = urlparse(url)
		if(o.netloc not in dicRef[each]):
			dicRef[each].append(o.netloc)
	counter = counter + 1

print(dicRef)