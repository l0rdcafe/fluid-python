fruits = ['grape', 'raspberry', 'apple', 'banana']
# creates new list
print(sorted(fruits)) # ['apple', 'banana', 'grape', 'raspberry']
# preserves old list
print(fruits) # ['grape', 'raspberry', 'apple', 'banana']

print(sorted(fruits, reverse=True)) # ['raspberry', 'grape', 'banana', 'apple']
print(sorted(fruits, key=len)) # ['grape', 'apple', 'banana', 'raspberry']
print(sorted(fruits, reverse=True, key=len)) # ['raspberry', 'banana', 'grape', 'apple']
print(fruits) # OG list
fruits.sort() # mutates OG list
print(fruits) # ['apple', 'banana', 'grape', 'raspberry']
