class Person:
    name = 'Lily'

p1 = Person()
p2 = Person()
p1.name = 'Bob'
print(p1.name)
print(p2.name)
print(Person.name)