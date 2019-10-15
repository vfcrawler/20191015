import copy
a = "TEST_STRING"  # a是一个不可变对象(字符串)
b = copy.copy(a)
print('修改前 ', 'a:', a, 'b:', b)
a = a.lower()
print('修改后 ', 'a:', a, 'b:', b)
