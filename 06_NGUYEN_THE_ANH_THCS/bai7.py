username = input("nhap ten dang nhap: ")
password = input("nhap mat khau: ")

truy_cap = (username == "admin") and (password != "password123")

print("truy cap thanh cong" * truy_cap + "truy cap khong thanh cong" * (not truy_cap))
