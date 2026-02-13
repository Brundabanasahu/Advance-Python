# x=200 #global variable
# def display():
#     global x
#     x=300   #local variable
#     print(x)

# display()
# print(x)    


# x=200
# def display():
#      x=300   #local variable
#      def show():
#           x=400
#           print(x)
#      print(x) 

# display()
# print(x)


# def display():
#     x=200
#     print(x) #before function
#     def show():
#         nonlocal x #nested function
#         x=300
#         print(x) # innner fuction
#     show()
#     print("After function",x)
# display()        


# x="global value"
# def outer_function():
#     x="outer value"
#     def inner_function():
#         x="inner value"
#         print(x)
#     inner_function()
#     print(x)
# outer_function()    
# print(x)


x="non-global value"
def outer_function():
    x="outer value"
    def inner_function():
        x="inner value"
        print(x)
    inner_function()
    print(x)
outer_function()    
print(x)