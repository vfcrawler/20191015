def countWords(alist):
    ret = {}
    for li in alist:
        ret[li] = ret.get(li, 0) + 1
    return ret

if __name__ == '__main__':
    a = [
            'apple','banana','apple','tomato',
            'orange','apple','banana','watermeton'
        ]
    print(countWords(a))

