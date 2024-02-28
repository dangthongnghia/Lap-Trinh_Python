thang = int(input('Nhập tháng: '))
nam = int(input('Nhập năm:'))
if thang in (1,3,5,7,8,10,12):
    print(f'Tháng {thang} có 31 ngày.')
elif thang in (4,6,9,11):
    print(f'Tháng {thang} có 30 ngày.')
if thang == (2):
# Tính năm nhuận và không nhuận
 if(nam % 4 == 0 and nam % 100 !=0) or nam % 400 == 0:
      print(f'Tháng {thang} có 29 ngày.')
 else:
      print(f'Tháng {thang} có 28 ngày.')