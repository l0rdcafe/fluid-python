s = 'café'
print(len(s)) # 4

b = s.encode('utf8')
print(b) # b'caf\xc3\xa9'
print(len(b)) # 5
print(b.decode('utf8')) # café

cafe = bytes(s, encoding='utf_8')
print(cafe)
print(cafe[0]) # 99
print(cafe[:1]) # b'c'
cafe_arr = bytearray(cafe)
print(cafe_arr) # bytearray(b'caf\xc3\xa9')
print(cafe_arr[-1:]) # bytearray(b'\xa9')
