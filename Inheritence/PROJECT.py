class Student:
    def input_student(self):
        self.name = input("Enter Student Name: ")
        self.sec = input("Enter Section: ")
        self.rollno = int(input("Enter Roll Number: "))


class Academic(Student):
    def input_academic(self):
        print("\nEnter Marks for 5 Subjects (Out of 100)")
        self.java = int(input("Java: "))
        self.python = int(input("Python: "))
        self.os = int(input("OS: "))
        self.c = int(input("C: "))
        self.dbms = int(input("DBMS: "))

        self.academic_total = (
            self.java + self.python + self.os + self.c + self.dbms
        )


class Sports(Student):
    def input_sports(self):
        self.sports_marks = int(input("\nEnter Sports Marks (Out of 20): "))


class Result(Academic, Sports):
    def display(self):
        grand_total = self.academic_total + self.sports_marks
        percentage = (grand_total / 520) * 100

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        if percentage >= 40:
            status = "PASS"
        else:
            status = "FAIL"


        print("\n" + "=" * 45)
        print("           STUDENT RESULT CARD")
        print("=" * 45)
        print(f"Name       : {self.name}")
        print(f"Section    : {self.sec}")
        print(f"Roll No    : {self.rollno}")
        print("-" * 45)
        print("ACADEMIC MARKS")
        print("-" * 45)
        print(f"Java       : {self.java}")
        print(f"Python     : {self.python}")
        print(f"OS         : {self.os}")
        print(f"C          : {self.c}")
        print(f"DBMS       : {self.dbms}")
        print("-" * 45)
        print(f"Total (500): {self.academic_total}")
        print(f"Sports(20) : {self.sports_marks}")
        print("-" * 45)
        print(f"Grand Total (520): {grand_total}")
        print(f"Percentage : {percentage:.2f}%")
        print(f"Grade      : {grade}")
        print(f"Result     : {status}")
        print("=" * 45)


obj = Result()
obj.input_student()
obj.input_academic()
obj.input_sports()
obj.display()