# Compute elements in sequence

def element():
    n = int(input("Input a number: "))
    x_n = (n ** 2) + 1
    print(x_n)

element()


def seq():
    n = int(input("Input a number: "))

    for x in range(1, n+1):
        print((x ** 2) + 1)

seq()