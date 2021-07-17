from collections import defaultdict

a = dict(one=1, two=2, three=3)
b = { 'one': 1, 'two': 2, 'three': 3 }
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({ 'three': 3, 'one': 1, 'two': 2 })
print(a == b == c == d == e)

DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan')
]

country_codes = { country: code for code, country in DIAL_CODES }
print(country_codes)

transformed_country_codes = { code: country.upper() for country, code in country_codes.items() if code < 66 }
print(transformed_country_codes)

d = defaultdict(list)
print(d)

d2 = dict([('2', 'two'), ('4', 'four')])
print(d2['2'])
print(d2['4'])
print(d2.get('1', 'N/A'))
print('1' in d2)
