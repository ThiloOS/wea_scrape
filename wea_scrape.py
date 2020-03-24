import requests
from bs4 import BeautifulSoup
import re
import textwrap

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


# Format WEA Names
# Removing digits & '[' & ']'
def letters(input):
    input = input.replace('[', '')
    input = input.replace(']', '')
    return ''.join([i for i in input if not i.isdigit()])


# Find built date
def built_date(input):
    return input[:4]


for i in range(len(wrapper)-1):
    #print(letters(wrapper[i+1][0]) + ' ' +built_date(wrapper[i+1][1]))
    #print(built_date(wrapper[i+1][1]))
    print(wrapper[i+1][4])