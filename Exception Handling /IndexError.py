#indexed Error

try:
    l=[10,20,30]
    print(l[3]) 
except IndexError as i:
    print("U have entered Wrong index")