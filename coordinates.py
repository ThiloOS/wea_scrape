test = '52° 28′ 37,5″ N, 8° 24′ 29″ O52.4770833333338.4080555555556'

def coordinates(coordinates):

    def transformation(input):
        new_coordinates = []
        symbols = ('°','′','″')
        for symbols in symbols:
            new_coordinates.append(input.partition(symbols)[0].replace('\xa0','').replace(' ',''))
            input = input.replace(input.partition(symbols)[0], '').replace(symbols,'')

        trans_coordinates = int(new_coordinates[0]) + ((int(new_coordinates[1])*60 + int(new_coordinates[2]))/3600)
        return trans_coordinates    

    new_input = coordinates.split(',')
    results = map(transformation, new_input)
    return(list(results))


x = coordinates(test)
print(x)