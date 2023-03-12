#make req
import requests 
#can add sys.argv to file.py
import sys 

#open file in read only
sub_list = open("wordlist2.txt").read() 
#split it to \n
directories = sub_list.splitlines()

#for loop run format http:{}/dir wordlist
for dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{dir}.html" 

    r = requests.get(dir_enum)
    #if 404 skipe
    if r.status_code==404: 
        pass
        #valid
    else:
        print("Valid directory:" ,dir_enum)
