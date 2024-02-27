# Nhập số từ người dùng
print('Nhap so thu nhat:')
a = int(input())
print('nhap so thu hai:')
b = int(input())
print('nhap so thu ba:')
c = int(input())
#Điều kiện để tìm số lớn nhất
max= a
if max < b: max = b
if max < c: max = c
print('So lon nhat la', max)