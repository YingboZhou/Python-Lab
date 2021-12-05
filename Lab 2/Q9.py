# functions to check string is palindrome or not
x = input("Enter a string: ")


def Palindrome1(x):
    return x == x[::-1]
y1 = Palindrome1(x)
if y1:
    print("String is palindrome.")
else:
    print("String is not palindrome.")


def Palindrome2(x):
    for i in range(0, int(len(x)/2)):
        if x[i] != x[len(x)-i-1]:
            return False
    return True
y2 = Palindrome2(x)
if y2:
    print("String is palindrome.")
else:
    print("String is not palindrome.")


# Method using one extra variable
w = ""
for i in x:
    w = i + w

if(x == w):
    print("String is palindrome.")
else:
    print("String is not palindrome.")


# Method using flag
j = -1
flag = 0
for i in x:
    if i != x[j]:
        j = j - 1
        flag = 1
        break
    j = j - 1

if flag == 1:
    print("String is not palindrome.")
else:
    print("String is palindrome.")


# Method using recursion
def Palindrome3(x):
    x = x.lower()
    l = len(x)
    if l < 2:
        return True
    elif x[0] == x[l - 1]:
        return Palindrome3(x[1:l-1])
    else:
        return False

y3 = Palindrome3(x)
if y3:
    print("String is palindrome.")
else:
    print("String is not palindrome.")


def palindrome():
    word = input("Please input a word to check if it is a palindrome or not: ")
    list_1 = []
    list_2 = []

    for x in word:
        list_1.append(x)
        list_2.append(x)

    list_2.reverse()

    if list_1 == list_2:
        print(f"The word {word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")

palindrome()