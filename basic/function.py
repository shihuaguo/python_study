def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-90))


# return multi value
def return_multi_value(x, y, z):
    return x * 10, y + 20, z / 10


print(return_multi_value(10, 20, 30))


# 可变参数
def un_verified_params(*param):
    for v in param:
        print(v)


un_verified_params(1, 2, 3, 4, 5)
list2 = ['a', 'b', 'c', 'd', 'e']
un_verified_params(*list2)


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


dict2 = {"key1": "value1", "key2": "value2", "key3": 300};
person("name", 18, **dict2)
