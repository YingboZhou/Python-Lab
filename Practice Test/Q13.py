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
        average = sum(marks) / len(marks)
        print(f"Average: {average}")


s = Student("Jane Doe", 12345, [70, 67, 68])
print(s.getName())
print(s.getNB())
s.addMark(70)
s.addMark(63)
print(s.marks)
Student.computeAverage(s.marks)
