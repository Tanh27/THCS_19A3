gia = float(input("nhap gia sp: "))
so_luong = int(input("nhap so luong: "))

tong_chi_phi = gia * so_luong

vat = tong_chi_phi * 0.10

tong_tien = tong_chi_phi + vat

print("tong tien phai tra:", round(tong_tien, 2))
