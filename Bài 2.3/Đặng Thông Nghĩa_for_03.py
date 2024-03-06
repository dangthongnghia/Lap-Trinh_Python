n = int(input('Nhập một số nguyên N='))

s = 1
for i in range (2, n + 1, 2): # 2 là số start, n + 1 là số kết thúc, 2 là số  xác định khoảng cách 

    s *= i # cộng vào tích
print("Tổng các số chẵn là:", s )

