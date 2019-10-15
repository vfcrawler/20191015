import copy
a = {1: [1, 2, 3]}  # a是一个可变对象(字典)
b = copy.deepcopy(a)
print('修改前 ', 'a:', a, 'b:', b)
a[1].append(4)
print('修改后 ', 'a:', a, 'b:', b)
