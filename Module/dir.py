import module1
# print(dir(module1))
for i in dir(module1):
    if ("__" not in i):
        print(i)