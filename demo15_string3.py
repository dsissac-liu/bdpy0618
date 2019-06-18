a1 = "abc"
a2 = ['a', 'b', 'c']
print type(a1), len(a1), a1
print type(a2), len(a2), a2
print a1[1:], a2[1:]
a2[1] = 'B'
a2[2] = 'fuck'
print a2
# a1[1] = 'B'
###################################################

a3 = list("ABCDEFG1234567" * 2)
print a3
a3[:5] = 'T'
print a3
del a3[:5]
print a3
a3[::2]=',,,,,,,,,,'
print a3