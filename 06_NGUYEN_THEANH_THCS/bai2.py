def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0 and b == 0:
        print("Vô số nghiệm")
    elif a == 0 and b != 0:
        print("Vô nghiệm")
    else:
        x = -b / a
        print("Nghiệm x =", x)
