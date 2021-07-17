from unicodedata import name

food = ['spam', 'spam', 'eggs', 'spam']
print(set(food))
print(list(set(food)))

needles = { 1, 2, 3, 4 }
haystack = { 0, 9, 21, 2, 3, 48, 6, 4, 43 }
union = needles | haystack
print(union)
intersection = needles & haystack
print(intersection)
intersection2 = needles.intersection(haystack)
print(intersection2)
complement = haystack - needles
print(complement)

difference = haystack ^ needles
print(difference)

print(frozenset(range(10)))
print({ chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '') })
