l1 = list('abcdefg')
l2 = l1
l3 = l1[:]
l4 = list(l1)
a = list(l2)
print hex(id(l1)), hex(id(l2)), hex(id(l3)), hex(id(l4)), hex(id(a))
a = l1
print l1, a
print hex(id(l1)), hex(id(a))
print l1, l2, l3, l4, a
l2[0] = 'A'
l1[1] = 'B'
l3[2] = 'C'
l4[3] = 'D'
a[5] = 'Z'
print l1, l2, l3, l4, a
