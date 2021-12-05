# TempConvert.py
TempStr = input("Enter temperature: ")
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("Temperature after conversion{:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
    print("Temperature after conversion{:.2f}F".format(F))
else:
    print("Input format error")