can_nang = float(input("nhap can nang (kg): "))
chieu_cao = float(input("nhap chieu cao (m): "))

bmi = can_nang / (chieu_cao ** 2)

print("BMI cua ban =", round(bmi, 2))
