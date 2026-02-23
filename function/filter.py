# l=[1,2,3,4,5]
# result=filter(lambda x:x%2==0,l)
# print(list(result))


l=["apple","banana","grape","orange"]
result=filter(lambda name:len(name)>3,l)
print(list(result))