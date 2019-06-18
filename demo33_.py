import demo32_

print "demo33"

print demo32_.foo(5, 6)
print demo32_.bar(7, 8)

import demo32_ as d

print d.foo(9, 10), d.bar(11, 12)

from demo32_ import foo

print foo(13, 14)

from demo32_ import bar as b

print b(15, 16)

from demo32_ import foo as f1, bar as f2

print f1(17, 18), f2(19, 20)

from demo32_ import none as n1, foo as f1, bar as b1

print n1(1, 2, 3), f1(2, 5), b1(5, 5)
