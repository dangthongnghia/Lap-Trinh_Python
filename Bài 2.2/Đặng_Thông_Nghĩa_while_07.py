# Hàm vòng lặp while để tìm ƯCLN(m,n)
def ucln(m, n):
    while n != 0:
        r = m % n
        m = n
        n = r
    return m

# Nhập 2 số nguyên m và n từ bàn phím
m = int(input("Nhập số nguyên m: "))
n = int(input("Nhập số nguyên n: "))

# In ra kết quả
print(f"Ước chung lớn nhất của {m} và {n} là: {ucln(m, n)}")
