x = 8
print "x=", x, ", x id=", hex(id(x))
x = 9
print "x=", x, ", x id=", hex(id(x))
x = 10
print "x=", x, ", x id =", hex(id(x))


class Person:
    def __init__(self, age):
        self.age = age


p1 = Person(8)
print "p1 id=", hex(id(p1)), ", p1.age=", p1.age, " ,p1.age id=", hex(id(p1.age))
p1.age = 9
print "p1 id=", hex(id(p1)), ", p1.age=", p1.age, " ,p1.age id=", hex(id(p1.age))

p2 = Person(1)
#p2.age = 88
print "p2 id=", hex(id(p2)), ", p2.age=", p2.age, " ,p2.age id=", hex(id(p2.age))
