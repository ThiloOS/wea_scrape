import requests, re, json
from bs4 import BeautifulSoup

print()
URL = 'https://de.wikipedia.org/wiki/Liste_von_Windkraftanlagen_in_Bremen,_Hamburg_und_Niedersachsen'#input('paste url here: ')
page = requests.get(URL)
print()

if page.status_code == 200:
    print('success. status code ' + str(page.status_code))
else:
    print('error. status code ' + str(page.status_code))
print()

file_name_input =  'test'#input('filename: ')
file_name = file_name_input + '.json'

soup = BeautifulSoup(page.content ,'html.parser')

table = soup.table

# Save each table row into seperate list
wrapper = []
for row in table.find_all('tr'):
    wea = []
    for cell in row.find_all('td'):
        wea.append(cell.text.rstrip('\n'))
    wrapper.append(wea)   


# Format and transform coordinates
def coordinates(coordinates):

    def transformation(input):
        new_coordinates = []
        symbols = ('°','′','″')
        for symbols in symbols:
            input = input.replace(',','.')
            new_coordinates.append(input.partition(symbols)[0].replace('\xa0','').replace(' ',''))
            input = input.replace(input.partition(symbols)[0], '').replace(symbols,'')

        trans_coordinates = int(new_coordinates[0]) + ((int(new_coordinates[1])*60 + float(new_coordinates[2]))/3600)
        return trans_coordinates    

    new_input = coordinates.split('N,')

    results = map(transformation, new_input)
    return(list(results))

count = 1
for j in range(len(wrapper)-1):
    print(wrapper[j+1][0])
    print(coordinates(wrapper[j+1][7]))