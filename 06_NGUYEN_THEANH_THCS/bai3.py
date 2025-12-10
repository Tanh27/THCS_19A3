def kiem_tra_so_armstrong(n):
    tong = 0
    temp = n
    while temp > 0:
        so = temp % 10
        tong += so**3
        temp //= 10
    return tong == n
