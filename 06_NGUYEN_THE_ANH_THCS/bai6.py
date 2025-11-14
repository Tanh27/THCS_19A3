nam = int(input("nhap nam: "))
nhuan = (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)
print(nam, "la nam nhuan" * nhuan + "khong phai nam nhuan" * (not nhuan))
