 #make req function
import requests

#url
url = 'https://assets.tryhackme.com/img/THMlogo.png'
#get req download
r = requests.get(url, allow_redirects=True)
#open file
open('THMlogo.png', 'wb').write(r.content)
