#Import statements
import requests

#get the webpage
web_page = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?"
db = 'db=nuccore'
term = "term=mrsa"
retmax = "retmax=100"
response = requests.get(web_page + db + '&' + term + '&' + retmax)
print(response)
print(response.text)

#Parse the response using lxml
from lxml import html

tree = html.fromstring(response.content)
ids = tree.xpath('//id/text()')

#Fetech the data using efecth
web_page = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
db = 'db=nuccore'
id_lookup = "id="
for uid in ids:
    id_lookup += uid +","
#Remove the last ,
id_lookup = id_lookup[:-1]

ret_type = "rettype=fasta&retmode=text"
#Now fecth the data
response = requests.post(web_page + db + '&' + id_lookup + '&' + ret_type)
print(response)
print(response.text[0:1000])
