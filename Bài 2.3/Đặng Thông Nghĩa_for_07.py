
n = int(input("Nhập n = "))

# Kiểm tra nếu n < 2 thì n không phải là số nguyên tố
if n < 2:
    print(f"{n} không phải là số nguyên tố")
else:
    # Sử dụng vòng lặp for để duyệt các số từ 2 đến căn bậc hai của n
    for i in range(2, int(n**0.5) + 1):
        # Kiểm tra nếu n chia hết cho i thì n không phải là số nguyên tố
        if n % i == 0:
            print(f"{n} không phải là số nguyên tố")
            break
    # Nếu không có số nào chia hết cho n thì n là số nguyên tố
    else:
        print(f"{n} là số nguyên tố")
