#Import statements
import requests

#get the webpage
web_page = "https://www.ncbi.nlm.nih.gov/"
response = requests.get(web_page)
print(response)
print(response.text)

#post to the webpage
#get the webpage
web_page = "https://www.ncbi.nlm.nih.gov/"
response = requests.post(web_page, data=[])
print(response)
print(response.text)
