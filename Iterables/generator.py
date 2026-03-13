def number():
        yield 1
        yield 2
        yield 3
n = number()
for i in n:
    print(i)