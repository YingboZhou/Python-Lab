nums = input("Enter three numbers: ")

total = 0
for i in nums:
    if i != ' ':
        total += int(float(i))
    else:
        pass

print("The sum is: ", total)