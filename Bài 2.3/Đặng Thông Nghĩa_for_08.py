n =int(input('Nhập số nguyên N: '))
# Khởi tạo tổng bằng 0
tong = 0
#Chuyển số nguyên dương n thành dạng chuỗi
n_str = str(n)
# dùng vòng lặp duyệt qua từng chuỗi
for i in str(n):
    # Cộng dồn giá trị số của từng chữ số vào biến tổng   
    tong += int(i)

print('Tổng các chữ số N là: ', tong) 
