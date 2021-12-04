# Sort three numbers
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))
if x >= y:
    if y >= z:
        print(x, y, z)
    else:
        if x >= z:
            print(x, z, y)
        else:
            print(z, x, y)
else:
    if x >= z:
        print(y, x, z)
    else:
        if z >= y:
            print(z, y, x)
        else:
            print(y, z, x)