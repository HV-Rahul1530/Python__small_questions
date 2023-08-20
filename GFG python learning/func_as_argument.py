def fun(a, b):
    return a+b

def func_1(func, lst1, lst2):
    result = []
    for i in range(len(lst1)):
        result.append(func(lst1[i], lst2[i]))
    return result

f = func_1(fun, [3, 5, 3, 6, 23], [3, 5, 45, 64, 3])
print(f)
            