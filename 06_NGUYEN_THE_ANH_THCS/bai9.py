kwh = float(input("nhap so kWh tieu thu: "))
bac1 = min(kwh, 100)
bac2 = max(min(kwh - 100, 100), 0)
bac3 = max(min(kwh - 200, 100), 0)
gia1 = 1678
gia2 = 1734
gia3 = 2014
tong_tien = bac1 * gia1 + bac2 * gia2 + bac3 * gia3
print("tong tien dien phai tra:", tong_tien)
