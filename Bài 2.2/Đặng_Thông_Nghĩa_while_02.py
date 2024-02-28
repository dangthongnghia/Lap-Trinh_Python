# Khởi tạo biến tổng và biến số chẵn
tong = 0
so_le = 1

# Lặp cho đến khi tổng vượt quá 50
while tong + so_le <= 100:
    tong += so_le
    so_le += 1

print(f"Tổng các số lẻ là: {tong}")

