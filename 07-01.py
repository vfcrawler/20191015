def import_args(test,*args):
    print('param1:',test)
    for item in args:
        print('other param:',item)

import_args('123','hello',2019)

