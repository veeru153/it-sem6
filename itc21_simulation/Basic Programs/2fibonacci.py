n1 = 0
n2 = 1
i = 0

print("Fibonacci Series upto 10")

while i < 10:
    print(n1, end=" ")
    n = n1 + n2
    n1 = n2
    n2 = n
    i += 1

print("\n")