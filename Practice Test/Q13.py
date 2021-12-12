class Student:
    def __init__(self, name, number, marks):
        self.name = name
        self.number = number
        self.marks = marks

    def getName(self):
        return self.name

    def getNB(self):
        return self.number

    def addMark(self, mark):
        self.marks.append(mark)

    def getMarks(self):
        return self.marks

    @staticmethod
    def computeAverage(marks):
        return sum(marks) / len(marks)


s = Student("Jane Doe", 12345, [70, 67, 68])
print(s.getName())
print(s.getNB())
s.addMark(70)
s.addMark(63)
print(s.marks)
average = Student.computeAverage(s.marks)
print("Average: ", average)