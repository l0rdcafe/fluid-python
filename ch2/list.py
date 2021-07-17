import array

symbols = '$ç£¥€☐'
codes = [ord(symbol) for symbol in symbols]
print(codes)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors
                         for size in sizes]
print(tshirts)

tup = tuple(ord(symbol) for symbol in symbols)
print(tup)

arr = array.array('I', (ord(symbol) for symbol in symbols))
print(arr)

for tshirt in ('%s %s' % (c, s) for c in colors
                                for s in sizes):
    print(tshirt)
