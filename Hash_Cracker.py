#module supports a wide rande of algorithms
import hashlib
#creates banner
import pyfiglet

#banner context
ascii_banner = pyfiglet.figlet_format("TryHackMe \n Python 4 Pentest \n Hash Cracker for MD 5")
#print banner
print(ascii_banner)

#wordlist location file input() to prompt the user to input wordlist
wordlist_location = str(input('Enter wordlist file location: '))

#Hash to be cracked
hash_input = str(input('Enter hash to be cracked: ' ))

#open file location as "file" name
with open(wordlist_location, "r") as file:
	#make forloop to read line each line
	for line in file.readlines():
		#use hashlib sha256 to hash wordlist password with line.strip white space removed the encode() method is used in this code to convert a Unicode string into a bytes object so that it can be used as input to the hashlib.md5() function.
		hash_ob = hashlib.sha256(line.strip().encode())
#hexdigest() method on the hash object to get the hashed password as a hexadecimal string.
		hashed_pass = hash_ob.hexdigest()
		#the hexdigest() method is used in this code to convert the binary representation of an MD5 hash into a more convenient and human-readable hexadecimal string representation.
		if hashed_pass == hash_input:
			print("Found cleartext password! " + line.strip())
			exit(0)
