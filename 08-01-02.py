from collections import Counter


def countWords(alist):
    ret_count = Counter(alist)
    ret = dict(ret_count)
    return ret


if __name__ == '__main__':
    a = [
        'apple', 'banana', 'apple', 'tomato',
        'orange', 'apple', 'banana', 'watermeton'
    ]
    print(countWords(a))
