n = int(input('Nhập một số nguyên N='))

t = 1
for i in range (1, n + 1, 2): # 1 là số start, n + 1 là số kết thúc, 2 là số  xác định khoảng cách 

    t *= i # cộng vào tích
print("Tổng các số lẻ là:", t )

