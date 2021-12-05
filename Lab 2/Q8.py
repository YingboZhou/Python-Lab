# Intersection of two lists

listA = [5, 23, 7, 89, 7, 90]
listB = [89, 25, 89, 7, 14, 76, 5, 11, 5]
listC = []

def method1():
    listC = set(listA) & set(listB)
    print(listC)

method1()


def method2():
    for x in listA:
        for y in listB:
            if x == y:
                listC.append(x)
    print(list(dict.fromkeys(listC)))

method2()