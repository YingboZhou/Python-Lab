# All numbers included between 2000 and 4000 divisible by 9 but are not a multiple of 2.

def factors():
    num = []
    for x in range(2000, 4001):
        if x % 9 == 0 and x % 2 == 1:
            num.append(str(x))
    print(','.join(num))

factors()
