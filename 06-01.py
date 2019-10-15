def duplicateList(alist):
    keys = {}
    keys = keys.fromkeys(alist)
    ret = list(keys)
    return ret

if __name__ == '__main__':
    alist = [1, 2, 2, 3, 4, 4, 6, 7, 7]
    print(duplicateList(alist))


