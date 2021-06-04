#!/env/bin python

def split_pairs(a):
    # your code here
    alist = []
    # if len of a is even number, no need for underscore
    if len(a) == 0:
        return a
    elif len(a) % 2 == 0:
        start_s = 0
        end_s = 2
        for i in a[start_s:end_s]:
            alist.append(a[start_s:end_s])
            start_s += 2
            end_s += 2
        return alist
    else:
        start_s = 0
        end_s = 2
        for i in a[start_s:end_s]:
            alist.append(a[start_s:end_s])
            start_s += 2
            end_s += 2
        last_spot = alist[-1]
        alist[-1] = last_spot+'_'
        return alist

if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
