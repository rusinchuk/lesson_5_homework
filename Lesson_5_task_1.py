def func_reverse(*args):
    list_k = list(set(args))
    list_k.sort()
    return list_k[1]


print(func_reverse(35, 20, 25, 63, 24, 20, 63, 28, 21, 69))

