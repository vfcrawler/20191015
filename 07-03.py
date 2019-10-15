def import_args(test,**kwargs):
    print('param1:',test)
    for key,value in kwargs.items():
        print(key,value)

d = {'name': 'jack', 'age': 26}
import_args('123',**d)

