x = 5
print x, hex(id(x))
x = 6
print x, hex(id(x))
y = 5
print y, hex(id(y))
print x, hex(id(y))
l = [5]
print l, hex(id(l))
l[0] = 6
print l, hex(id(l))
z = [888]
print z , hex(id(z))