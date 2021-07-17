from collections import namedtuple
import os

lax_coords = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

lat, lng = lax_coords
print(lat, lng)

arr = os.path.split('/home/iarafa/.ssh/idrsa.pub')
print(arr)
_, filename = arr
print(_, filename)

t = (20, 8)
print(divmod(*t)) # (2, 4)
quotient, remainder = divmod(*t)
print(quotient) # 2
print(remainder) # 4

a, b, *rest = range(5)
print(a, b, rest) # 0 1 [2, 3, 4]

a, *body, c, d = range(5)
print(a, body, c, d) # 0 [1, 2] 3 4

*head, b, c, d = range(5)
print(head, b, c, d) # [0, 1] 2 3 4

metro_areas = [
  ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
  ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
  ('Mexico City', 'MX', 20.142, (10.433333, -99.133333)),
  ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
  ('Sao Paolo', 'BR', 19.649, (-23.547778, -46.635833))
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'lng.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (lat, lng) in metro_areas:
    if lng <= 0:
        print(fmt.format(name, lat, lng))

City = namedtuple('City', 'name country population coords')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.coords)
print(tokyo.population)
print(tokyo[1])

print(City._fields)

LatLng = namedtuple('LatLng', ['lat', 'lng'])
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLng(28.613889, 77.208889))
delhi = City._make(delhi_data)
delhi2 = City(*delhi_data)
print(delhi._asdict())

for key, val in delhi2._asdict().items():
    print(key + ':', val)

l =list(range(10))
print(l) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l[2:5] = [20, 30]
print(l) # [0, 1, 20, 30, 5, 6, 7, 8, 9]
del l[5:7]
print(l) # [0, 1, 20, 30, 5, 8, 9]
l[3::2] = [11, 22]
print(l) # [0, 1, 20, 11, 5, 22, 9]
l[2:5] = [100]
print(l) # [0, 1, 100, 22, 9]

l2 = [1, 2, 3]
print(l2 * 5) # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
print(5 * 'abcd') # abcdabcdabcdabcdabcd

board = [['_'] * 3 for i in range(3)]
print(board) # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[1][2] = 'X'
print(board) # [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]

buggy_board = [['_'] * 3] * 3 # * 3 dupes list reference, so nested list has 3 references to same list
print(buggy_board) # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
buggy_board[1][2] = 'O' # this mutates the main list copy and therefore all 3 references
print(buggy_board) # [['_', '_', 'O'], ['_', '_', 'O'], ['_', '_', 'O']]

l3 = [1, 2, 3]
print(id(l3))
l3 *= 2
print(l3)
print(id(l3)) # same id since lists are mutable

t = (1, 2, 3)
print(id(t))
t *= 2
print(t)
print(id(t)) # new id since tuples are immutable
