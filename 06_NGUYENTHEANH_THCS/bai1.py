x = int(input("Nhap so x: "))

i = 0
while i*i <= x:
    if i*i == x:
        print(x, "la so chinh phuong")
        break
    i += 1
else:
    print(x, "khong la so chinh phuong")
