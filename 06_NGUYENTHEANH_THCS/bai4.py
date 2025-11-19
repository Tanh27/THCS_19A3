n = int(input("Nhap n: "))

for x in range(2, n):
    kt = True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            kt = False
            break
    if kt:
        print(x, end=" ")
45