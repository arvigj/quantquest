#Team: HackALink
#Names of the S&P 500 Companies --> List
#Source: Wikipedia
#Number of Companies more than 500 (504)
#Page Version Date --> 28 December 2015

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
while(numberOfCompanies < 504):
	allNames.append(values[i].text)
	i += 8
	numberOfCompanies += 1

