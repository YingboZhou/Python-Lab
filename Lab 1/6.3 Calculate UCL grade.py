# Calculate UCL grade
averageMark = float(input("Enter the average module mark: "))
if averageMark >= 70 and averageMark <= 100:
    print("Your Grade is Distinction")
elif averageMark >= 50 and averageMark < 70:
    print("Your Grade is Pass")
elif averageMark >=0 and averageMark < 50:
    print("Your Grade is Fail.")
else:
    print("Invalid Input")




