# Khởi tạo biến tổng và biến số chẵn
tong = 0
so_chan = 2

# Lặp cho đến khi tổng vượt quá 50
while tong + so_chan <= 50:
    tong += so_chan
    so_chan += 2

print(f"Tổng các số chẵn là: {tong}")

