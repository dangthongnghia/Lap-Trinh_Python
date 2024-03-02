n = int(input('Nhập số nguyên n:')) # Nhập số nguyên từ bàn phím
tong = 0 # tạo biến tổng bằng 0
while n > 0:
    chu_so = n % 10 # Lấy chữ số cuối cùng
    tong += chu_so # Cộng vào tổng
    n //= 10 # Loại bỏ chữ số cuối cùng

print("Tổng các chữ số của n là:", tong)
