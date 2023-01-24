

def primefac(n):

    div = 2

    while n > 1:
        if (n%div == 0):
            print(int(n), end=" ")
            n = n / div
        else:
            div += 1

primefac(40)