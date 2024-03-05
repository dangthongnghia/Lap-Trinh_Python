# Nhập giá trị N từ bàn phím
N = int(input("Nhập một số N: "))

# Khởi tạo biến tổng
tong = 0

# Duyệt qua các số từ 1 đến N
for i in range(1, N + 1):
    if i % 2 != 0:
        tong += i

# In tổng các số lẻ
print(f"Tổng các số lẻ từ 1 đến {N} là: {tong}")
