n = int(input('Nhập một số nguyên N='))

s = 0
for i in range (1, n + 1, 2): # 1 là số start, n + 1 là số kết thúc, 2 là số  xác định khoảng cách 

    s += i # cộng vào tổng
print("Tổng các số lẻ là:", s )

