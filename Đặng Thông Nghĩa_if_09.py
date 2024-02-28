diem_trung_binh = float(input('Vui lòng nhập điểm trung bình:'))
if diem_trung_binh >= 9:
   print('Bạn được nhận học bổng là 5.000.000')
elif diem_trung_binh >= 8 and diem_trung_binh < 9:
      print('Bạn được nhận học bổng là 3.000.000')
elif diem_trung_binh >= 7 and diem_trung_binh < 8:
      print('Bạn nhận được học bổng là 1.000.000') 
else:
   print('Bạn không được nhận học bổng.')
