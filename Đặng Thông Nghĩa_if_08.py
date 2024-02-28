# Đề xuất sửa chữa máy tính
nam_san_xuat = int(input('Nhập năm sản xuất:'))
if nam_san_xuat >= 15:
    print('Nên thay thế')
elif nam_san_xuat >= 10 and nam_san_xuat < 15:
    print('Nên bảo trì')
else:
    print('Không có đề xuất')  
