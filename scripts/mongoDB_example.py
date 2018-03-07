#Import statements
from pymongo import MongoClient

#Connect to the database
mongo_uri = 'mongodb://test_user:Emory18!@ds023455.mlab.com:23455/heroku_kn66qwrg'
client = MongoClient(mongo_uri)
database = client["heroku_kn66qwrg"]
#Make a new collection
your_name = "Doug" #<- INSERT YOUR NAME HERE
data = {} 
database[your_name + "_sequences"].insert_one(data)

print(database[your_name + "_sequences"])


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

#Create a temporary local file to hold the information
f = open('temp.fasta', 'w')
f.write(response.text)
f.close()

#load the FASTA files using biopython
from Bio import SeqIO

#Now save these to mongoDB
for seq_record in SeqIO.parse('temp.fasta', "fasta"):
    seq_data = dict()
    seq_data["sequence"] = str(seq_record.seq)
    seq_data["record_id"] = seq_record.id
    result = database[your_name + "_sequences"].insert_one(seq_data)
    print(result.inserted_id)
