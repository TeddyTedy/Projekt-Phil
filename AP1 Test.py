#Imports

from requests import get
from json import loads

#Definition der URL
url="https://instagram.com/#Benutzername"

#Parameter
parameter={'__a': 1, '__d': 1}

#Cookie
cookie={'sessionid': 123}

#Antwort im Falle von Zusage
def onsuccess(response):
    responsenc= response.text #unklare Textfile ausgabe nc=not clear
    responsejson= loads(responsenc)

    print("Username:", responsejson["graphql"]["user"]["full_name"])

#Antwort im Falle abgeblockt
def onfailure(response):
    print(response.status_code)
    print(response.reason)

response= get(url,params=parameter,cookies=cookie)

if response.status_code==200:
    onsuccess(response)
else:
    onfailure(response)







