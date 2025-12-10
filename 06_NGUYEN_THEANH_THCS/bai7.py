def tinh_tong_so_hoan_hao(a, b):
    tong = 0
    for n in range(a, b + 1):
        uoc = 0
        for i in range(1, n):
            if n % i == 0:
                uoc += i
        if uoc == n:
            tong += n
    return tong
