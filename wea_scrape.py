import requests
from bs4 import BeautifulSoup

URL = 'https://de.wikipedia.org/wiki/Liste_von_Windkraftanlagen_in_Bremen,_Hamburg_und_Niedersachsen'
page = requests.get(URL)

soup = BeautifulSoup(page.content ,'html.parser')

table = soup.table

# Save each table row into seperate list
wrapper = []
for row in table.find_all('tr'):
    wea = []
    for cell in row.find_all('td'):
        wea.append(cell.text.rstrip('\n'))
    wrapper.append(wea)   

for i in range(len(wrapper)-1):
    print(wrapper[i+1][9])


    

    

