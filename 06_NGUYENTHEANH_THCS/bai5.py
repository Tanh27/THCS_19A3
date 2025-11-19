n = int(input("Nhap n: "))

s1 = 0
for i in range(1, n+1):
    s1 += i

print("S1 =", s1)
n = int(input("Nhap n: "))

s2 = 1
for i in range(1, n):
    s2 *= i

print("S2 =", s2)
n = int(input("Nhap n: "))

s3 = 0
for i in range(1, n+1):
    if i % 2 == 1:
        s3 += 1/i
    else:
        s3 -= 1/i

print("S3 =", s3)
n = int(input("Nhap n: "))

s4 = 0
for k in range(0, n+1):
    s4 += k / (k + 2)

print("S4 =", s4)
