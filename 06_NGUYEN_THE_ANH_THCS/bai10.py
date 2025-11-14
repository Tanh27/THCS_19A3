luong_co_ban = float(input("nhap muc luong co ban: "))
ngay_cong = float(input("nhap ngay cong: "))
luong_mot_ngay = luong_co_ban / 22
luong_chinh = luong_mot_ngay * ngay_cong
tien_thuong = luong_chinh * 0.10 * (ngay_cong > 22)
tien_phat = luong_chinh * 0.05 * (ngay_cong < 22)
luong_thuc_nhan = luong_chinh + tien_thuong - tien_phat

print("luong thuc nhan:", luong_thuc_nhan)
