#FileNotFoundError

try:
    x = open("Data.txt")
except FileNotFoundError as f:
    print(f)