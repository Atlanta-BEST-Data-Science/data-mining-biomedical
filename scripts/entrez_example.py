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

