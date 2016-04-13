import bs4
from bs4 import BeautifulSoup
import urllib2
import wikipedia

wiki = "https://en.wikipedia.org/w/index.php?title=List_of_S%26P_500_companies&oldid=697200065"
page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page, "html.parser")
table = soup.find("table", { "class" : "wikitable sortable" })

allUrls = []
numberOfCompanies = 0
i = 1

values = table.findAll("td")
while(numberOfCompanies < 510):
	try:
		allUrls.append(values[i].contents[0].get("href"))
	except:
		pass
	i += 8
	numberOfCompanies += 1


ny = wikipedia.page("New York")
for each in allUrls:
	ny.url = "https://en.wikipedia.org/"+str(each)
	print(ny.summary)