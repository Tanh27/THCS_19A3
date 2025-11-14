tien_gui = float(input("nhap so tien gui ban dau: "))
lai_suat = float(input("nhap lai suat hang nam (%): ")) / 100
lai_1_thang = tien_gui * lai_suat * (1/12)
lai_2_quy = tien_gui * lai_suat * (6/12)
lai_3_nam = tien_gui * lai_suat * 3

print("Lai sau 1 tháng:", lai_1_thang)
print("Lai sau 2 quý:", lai_2_quy)
print("Lai sau 3 năm:", lai_3_nam)
