class student:
    def __init__(self,mark):
        self.marks=mark

    def __add__(self,other):
        return self.marks+other.marks
    
s=student(20)
s1=student(30)
print("total mark",s+s1)