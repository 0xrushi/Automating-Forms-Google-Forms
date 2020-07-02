# importing the requests library 
import requests 
import urllib

# Replace the viewForm from orignal url with formResponse
URL = "https://docs.google.com/forms/d/e/1FAIpQLSc11NqG6fWqNn327qdb479z6QTrmC7QEwbvH7sB-CQ59iA_ZQ/formResponse"

raw_headers='''
Host: docs.google.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://docs.google.com/forms/d/e/1FAIpQLSc11NqG6fWqNn327qdb479z6QTrmC7QEwbvH7sB-CQ59iA_ZQ/viewform?fbzx=5050709467963863140
Content-Type: application/x-www-form-urlencoded
Content-Length: 365
Origin: https://docs.google.com
Connection: close
Cookie: S=spreadsheet_forms=ptyYIUGTE-Wce1eMmds7LWc60bZe_XGHOQKjxWnzIHk; NID=204=0wAwj_KBdtmVpuWOQvMGbyhQS7w9LewGgXAnULqYY-ElcRmhGC1_LeJHUB__Fl7nRmGA89EjUK_6PDO4ihZ0fbL0mohFj5zYKpwCZ3j-DoGFtMo2gzQ0Ck9XabjFSDOGgYvjQXFVE6YuhD9SzX9XKub9zsG7o6KPKNThIYz0f5I; ANID=AHWqTUm_MzyyXf3yDhw_L2TZ3Gx9IL62BowaziQCT57iFP7NiOWn86NfU5A3FRyo
Upgrade-Insecure-Requests: 1
'''

headrs= dict([[h.partition(':')[0], h.partition(':')[2].strip()] for h in raw_headers.split('\n')])
del headrs['Cookie']
del headrs['']

raw_data='entry.2092238618=test1&entry.1556369182=test1%40gmail.com&entry.479301265=asdasd&entry.1753222212=Day+1&entry.1753222212=Day+3&entry.588393791=Vegetarian&entry.2109138769=Yes&entry.1753222212_sentinel=&entry.588393791_sentinel=&entry.2109138769_sentinel=&fvv=1&draftResponse=%5Bnull%2Cnull%2C%225050709467963863140%22%5D%0D%0A&pageHistory=0&fbzx=5050709467963863140'

raw_data= urllib.parse.unquote(raw_data)
raw_data=raw_data.split('&')
data={}
for x in raw_data[:-4]:
    data[x.split('=')[0]]=x.split('=')[1]

data= {k: v for k, v in data.items() if v is not ''}
print(data.keys())

data = {
        "entry.2092238618":"johnwick",
        'entry.1556369182': 'johnw@gmail.com',
        'entry.479301265': 'dheknyasorg',
        'entry.1753222212': ['Day 1', 'Day 3'],
        'entry.588393791': 'Vegan',
        'entry.2109138769': 'Yes',
    }


# sending post request and saving response as response object 
r = requests.post(url = URL, data = data, headers=headrs) 

# # extracting response text 
resp = r.status_code 
print("The ResponseL is:%s"%resp) 

