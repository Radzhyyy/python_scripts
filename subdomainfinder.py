#import modual for requests
import requests


domain = "10.10.249.238"


#make varible with function "open" to open file to read only 
wordlist_file = open('/usr/share/wordlists/PythonForPentesters/wordlist2.txt' , 'r')

#make varible = create "list" open file "f" to read and "split" it \n each lane.
subdomains = list(wordlist_file.read().split("\n"))

#print output
#print(subdomain)

#make for loop for subdomains
for i in subdomains:
	#subdomain.test.com  {}.{} puts wordlist of subdomains i each subdomain + domain 
	url = f"http://{i}.{domain}"
	#url = "http://{}.{}".format(i, domain)
	print(url)

	# req GET url 
	r = requests.get(url)
	if r.status_code != 404:
		print("URL subdomain {} valid".format(i))

#close file "f" stop function
wordlist_file.close()