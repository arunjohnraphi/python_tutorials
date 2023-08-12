def sum(*a):
    print("type of a = " )
    print(type(a))
    sum = 0
    for i in a:
        sum = sum + i
    return sum

print(sum(5))
