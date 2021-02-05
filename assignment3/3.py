from urllib.request import urlopen
import re

#Test if the string is http format
regex = re.compile(r"^https?://(\w+\.)?\w+\.\w+(/.*)?$")

url = input("Please give URL: ")
#If string doesn't match on regex pattern stops
if not re.match(regex, url):
    print("Not a valid URL")
else: 
    #All good, asks user for filename
    filename = input("Please give name for the file: ")
    if not filename:
        print("Not a valid filename")
    else:
        #Finally if url address is correct form and filename is given, program tries to save it to file.
        #Program does not check if the website is really working
        try:   
            with urlopen(url) as response:
                data = response.read()
                with open(filename, "wb") as f:
                    f.write(data)
        except OSError:
            print("Error!")
