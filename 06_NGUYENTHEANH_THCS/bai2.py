a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))

while b != 0:
    r = a % b
    a = b
    b = r

print("UCLN =", a)
