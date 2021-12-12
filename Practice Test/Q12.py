number = int(float(input("Enter an integer: ")))

def fibonacci(num):
    if num <= 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

for i in range(1, number + 1):
    print(fibonacci(i))