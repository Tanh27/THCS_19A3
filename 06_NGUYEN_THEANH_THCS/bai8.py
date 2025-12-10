a = int(input("Nhập số a: ")   )
b = int(input("Nhập số b: ")   )
c = int(input("Nhập số c: ")   )
def tim_so_le_lon_nhat(a, b, c):
    ds = [a, b, c]
    so_le = [x for x in ds if x % 2 != 0]
    if len(so_le) == 0:
        return -1
    return max(so_le)
print("Số lẻ lớn nhất là:", tim_so_le_lon_nhat(a, b, c))