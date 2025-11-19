tu = int(input("Nhap tu so: "))
mau = int(input("Nhap mau so: "))
a = tu
b = mau
while b != 0:
    r = a % b
    a = b
    b = r
ucln = a

print("Phan so toi gian:", tu//ucln, "/", mau//ucln)
