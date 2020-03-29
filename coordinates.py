import re

test = "53° 13′ 0″ N, 8° 31′ 31,5″ O53.2166666666678.5252777777778"
new_input = test.split(',')
print(new_input)


def transform(coordinates):
    d = re.findall(r'(\d+)°', coordinates)
    m = re.findall(r'(\d+)′', coordinates)
    s = re.findall(r'(\d+\*,\d+)″', coordinates)
    coordinates = [d, m, s]
    return coordinates

print(list(map(transform, new_input)))