# def greeting(name):
#     print("My name is ",name)


# def student1(name,rollno,age,section):
#     print(f"My Name is : {name} and Roll No is : {rollno} and my Age is : {age} and my Section is : {section}")

# student1("Brundabana", "23CSE584", 20, "J")   


# def student2(name,rollno,age,section="J"):
#     print(f"My Name is : {name} and Roll No is : {rollno} and my Age is : {age} and my Section is : {section}")
# student2(name="Brundabana", rollno="23CSE584", age=20, section="I") 

# def fruit(name):
#     for i in name:
#         print(i)  
# x=["apple","banana","orange"]        
# fruit(x)


# def country(name):
#     for i in name:
#         print(i)  
# x=["india","UK","Aus"]        
# country(x)


# print("only values")
# print("--------------")
# def students(info):
#     for key,value in info.items():
#         print(value)

# x={"name":"Brundabana", "rollno":"23CSE584", "age":20, "section":"J"}
# students(x)

# print("only keys")
# print("--------------")
# def students(info):
#     for key in info.keys():
#         print(key)

# x={"name":"Brundabana", "rollno":"23CSE584", "age":20, "section":"J"}
# students(x)


print("Arbitary positional arguments")
print("-----------------------------")

def students(*name):
    for i in name:
        print(f"Hi {i}, have a nice day")


students("Brundabana","Ayush","Sagar","Subrat")