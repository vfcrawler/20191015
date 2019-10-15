def import_args(test,*args):
    print('param:',test)
    for item in args:
        print('other params:',item)

args = ['hello',2019]
import_args('123',*args)

