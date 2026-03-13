class number:
    def __iter__(self):
        self.num = 1
        return self
    
    def __next__(self):
        x = self.num
        self.num +=1
        return x

n = number()
it = iter(n)

print(next(it))
print(next(it))
print(next(it))
print(next(it))