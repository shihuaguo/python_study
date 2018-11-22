# list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(classmates[0])

classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
print(classmates[0])

single_tuple = ('single',)
print(single_tuple)

# if
age = 18
if age <= 6:
    print("age=", age)
elif age >= 12:
    print("age=", age)

# 循环
for name in classmates:
    print(name)

# dict and set
dict1 = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(dict1['Michael'])
set1 = {1, 2, 3}
set1.add(4)
for s in set1:
    print(s)
