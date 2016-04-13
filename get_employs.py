from lxml import etree
import requests
import json

all_urls = []
with open('urls.txt', 'r') as url_details:
	for each in url_details:
		all_urls.append(each)

all_names = []
with open('names.txt', 'r') as names_details:
	for each in names_details:
		all_names.append(each)

employeesRe = {}
for i in range(0, 504, 1):
	url_to_call = "https://en.wikipedia.org"+str(all_urls[i]).strip()
	r = requests.get(url_to_call)
	doc = etree.fromstring(r.text)
	e = doc.xpath('//table[@class="infobox vcard"]/tr[th/div/text()="Number of employees"]/td')
	try:
		number_of_employees = e[0].text.split()[0]
		number_of_employees = number_of_employees.replace(',', '')
		employeesRe[all_names[i]] = int(number_of_employees)
	except:
		try:
			e = doc.xpath('//table[@class="infobox vcard"]/tr[th/div/text()="Employees"]/td')
			number_of_employees = e[0].text.split()[0]
			number_of_employees = number_of_employees.replace(',', '')
			employeesRe[all_names[i]] = int(number_of_employees)
		except LookupError:
			employeesRe[all_names[i]] = -1



print(employeesRe)
with open('employees.json', 'w') as emp_fi:
	json.dump(employeesRe, emp_fi)

# my_string = str(all_urls[0]).strip()
# url = "https://en.wikipedia.org"+my_string
# print(url)
# r = requests.get(url)
# doc = etree.fromstring(r.text)
# e = doc.xpath('//table[@class="infobox vcard"]/tr[th/div/text()="Number of employees"]/td')
# print(e[0].text)
