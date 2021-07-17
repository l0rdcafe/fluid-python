from array import array
from random import random
# array of doubles
floats = array('d', (random() for i in range(10**7)))
print(floats[-1])

file_ptr = open('floats.bin', 'wb')
floats.tofile(file_ptr)
file_ptr.close()

floats2 = array('d')
file_ptr = open('floats.bin', 'rb')
floats2.fromfile(file_ptr, 10**7)
file_ptr.close()
print(floats2[-1])
print(floats2 == floats)

nums = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(nums)
print(len(memv))
print(memv[0])

memv_octal = memv.cast('B')
print(memv_octal.tolist())
memv_octal[5] = 4
print(nums)
