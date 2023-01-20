import requests
from bs4 import BeautifulSoup
import sys 

#page = requests.get('https://www.sportovnivozy.cz/znacka-33-subaru')
# Create a BeautifulSoup object

with open("/home/toor/Desktop/zadek/Subaru.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

#soup = BeautifulSoup(page.text, 'html.parser')
# get the repo list
# repo = soup.find(class_="repo-list")

#print(type(soup))
#print(soup.)

inzeraty = soup.find_all(class_="vypisDilo W100pc T100pc prechod1") 
#nadpis = soup.find_all(class_="nadpis")
#cena = soup.find_all(class_="inzeratycena")
pozice = 0
for tag in inzeraty:
    print(pozice)
    print(tag.get_text())
    
    nadpis = soup.find(class_='h40')
    #print(type(nadpis))
    #<class 'bs4.element.Tag'>
    nadpis_plain = nadpis.get_text().strip()
    #print(nadpis_plain)
    
    cena = soup.find(class_='vb')
    cena_plain = cena.get_text().strip("Kč")
    #print(cena_plain)
  
    #print(cena_plain[0:-3])
    pozice += 1


print("Celkový počet inzerátů", pozice - 1)

sys.exit()

