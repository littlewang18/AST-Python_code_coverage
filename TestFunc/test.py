def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def compare(a, b):
    if a > b:
        a = 999
        return a
    elif a == b:
        a = 1000
        return 0
    else:
        b = 888
        return b

x = add(2, 3)
y = compare(2, 4)