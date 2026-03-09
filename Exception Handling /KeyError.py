#Key Error

try:
    student = {"Name ": "Aditya", "Rollno": "23cse704", "Age":21}
    print(student["City"])

except KeyError as key:
    print("You have entered the wrogn key!")