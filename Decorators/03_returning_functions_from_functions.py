def parent(num):
    def first_child():
        print("secret number is" , num)
        return "Hi, I am Emma"


    return first_child



first = parent(1)
print(first)
next_first = parent(2)
print(next_first)


print("testing --------------------------")

print(first())
print(next_first())
