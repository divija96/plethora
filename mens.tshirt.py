import requests
from bs4 import BeautifulSoup
r=requests.get("http://www.myntra.com/sweaters-and-sweatshirts-women-menu")
soup=BeautifulSoup(r.content)
g_data=soup.find_all("div",{"class":"brand"})
for item in g_data :
   print item
file=open("data.txt","w")
for item in g_data :
    file.write(str(item)+"\n")
g_data=soup.find_all("div",{"class":"sizes"})
for item in g_data :
   file.write(str(item)+"\n")
g_data=soup.find_all("div",{"class":"price"})
for item in g_data :
   file.write(str(item)+"\n")
g_data=soup.find_all("div",{"class":"product"})

for item in g_data :
    file.write(str(item)+"\n")
    
    
    
