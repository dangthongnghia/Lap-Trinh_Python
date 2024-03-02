# Nhập vào số nguyên dương n
n = int(input("Nhập n = "))

# Kiểm tra số n có phải là số nguyên tố không
if n == 1 or n == 2:
    print(n, "là số nguyên tố")
elif n % 2 == 0:
    print(n, "không phải là số nguyên tố")
else:
    flag = True # Giả sử n là số nguyên tố
    import math
    i = 3 # Khởi tạo biến lặp
    while i <= int(math.sqrt(n)): # Duyệt các số lẻ từ 3 đến căn bậc hai của n
        if n % i == 0: # Nếu n chia hết cho i
            flag = False # n không phải là số nguyên tố
            break # Thoát vòng lặp
        i += 2 # Tăng biến lặp
    if flag:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")
