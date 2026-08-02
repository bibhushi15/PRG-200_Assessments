# Name: Bibhushi Karki
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        return sum(self.marks) / len(self.marks)
    def grade(self):
        avg = self.average()
        if avg >= 80:
            return "A"
        elif avg >= 65:
            return "B"
        elif avg >= 50:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"
    def display(self):
        avg = self.average()
        if avg >= 40:
            result = "Pass"
        else:
            result = "Fail"
        print(f"{self.name} | Average: {avg:.2f} | Grade: {self.grade()} | {result}")

students = [
    Student("Aarav", [78, 85, 60, 90, 72]),
    Student("Sita", [45, 50, 38, 60, 55]),
    Student("Bishal", [30, 25, 40, 35, 28]),
    Student("Priya", [90, 88, 95, 92, 87])
]
for student in students:
    student.display()
    