tong_keo = int(input("nhap tong so keo: "))
so_hoc_sinh = int(input("nhap so hoc sinh: "))
moi_hs = tong_keo // so_hoc_sinh
con_thua = tong_keo % so_hoc_sinh

print("moii hoc sinh nhan:", moi_hs, "kẹo")
print("so keo con du:", con_thua)
