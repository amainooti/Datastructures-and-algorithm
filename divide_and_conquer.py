# say we have to sum nums in an array using a loop


def sum(num):
    sumed = 0
    for i in num:
        sumed += i
    return sumed


# print(sum(num))


def sum(n):
    if n == []:
        return 0
    return n[0] + sum(n[1:])


n = [1, 2, 5, 9]

print(sum(n))


def count(n):
    if n == []:
        return 0

    return 1 + count(n[1:])


print(count(n))


n = [0, 9]


def sort(n):
    for i in range(len(n)):
        if n[0] < n[i]:
            n[0] = n[i]
            print(n[0])
        return n[i]


print(sort(n))
