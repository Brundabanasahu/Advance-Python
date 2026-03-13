def number():
    for i in range(1,11):
        yield i*i
for j in number():
    print(j)