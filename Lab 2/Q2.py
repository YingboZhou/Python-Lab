# The value of R.

import math as m

def formula(X = 70, H = 25):
    n = input("What values of Y would you like to use: ")

    Y_values = n.split(",")

    y_values = []

    for y in Y_values:
        Y = int(y)
        y_values.append(Y)

    Y_results = []

    for y in y_values:
        R = m.sqrt((3 * X * y) / H)
        r = str(round(R))
        Y_results.append(r)

    answers = ",".join(Y_results)
    print(answers)


formula()