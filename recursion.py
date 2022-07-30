# recursion is a method of programming in which a function calls itself


def count_down(i):
    print(f"{i} ...")
    if i <= 0:
        return
    else:
        count_down(i-1)


print(count_down(0))


# stack

def compliment(name):
    print(f"{name} is such a nice name")
    greet()
    bye()


def greet(name):
    print(f"how are you {name}")


def bye():
    print("Ok now bye! :-)")


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(11))
