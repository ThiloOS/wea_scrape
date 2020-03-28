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

# Format WEA Names
# Removing digits & '[' & ']'
def letters(input):
    input = input.replace('[', '')
    input = input.replace(']', '')
    return ''.join([i for i in input if not i.isdigit()])


# Format built date
def built_date(input):
    return input[:4]


# Format Location
def location(input):
    return re.sub(r"(?<=\w)([A-Z])", r" \1", input)

# Format WEA type
def type(input):
    input = input.replace(',', '.')
    list = input.replace(')', '),').split(',')
    list.pop()
    return list

# Format and transform coordinates



data = []
for i in range(len(wrapper)-1):
    dict = {'name':letters(wrapper[i+1][0]), 'built':built_date(wrapper[i+1][1]), 'in_use':True, 'power':wrapper[i+1][2], 'number':wrapper[i+1][3], 'type':type(wrapper[i+1][4]), 'location':location(wrapper[i+1][5]), 'zip':wrapper[i+1][6], 'coordinates':wrapper[i+1][7], 'owner':wrapper[i+1][8]}
    data.append(dict)

with open(file_name , 'w', encoding='utf8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
    print('file created')




   
