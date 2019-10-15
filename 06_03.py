def duplicateList(alist):
    ret = []
    for li in alist:
        if li not in ret:
            ret.append(li)
    return ret

if __name__ == '__main__':
    alist = [1, 2, 2, 3, 4, 4, 6, 7, 7]
    print(duplicateList(alist))