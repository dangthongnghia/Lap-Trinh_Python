n = float(input('Nhập vào một số bất kì:'))
# kiểm tra có phải là số nguyên không
if n != 0:
   print(f'{n}là số nguyên')
else:
   print(f'{n} không phải là số nguyên')

# Kiểm tra có phải là số chẳn lẻ không
if n % 2 == 0:
   print(f'{n} là số chẳn')
elif n % 2 != 0:
   print(f'{n} là số lẻ')

#Kiểm tra có phải là số chẳn dương không
if n % 2 == 0 and n > 0:
   print(f'{n} là số chẳn dương')
elif  n % 2 != 0 and n > 0:
   print(f'{n} là số lẻ dương')
# Kiểm tra có phải là số chẳn lẻ âm
if n % 2 == 0 and n < 0:
   print(f'{n} là số chẳn âm')
elif  n % 2 != 0 and n < 0:
   print(f'{n} là số lẻ âm')
# Kiểm tra có phải là số chính phương hay không
check = False
for i in range(1, int(n**0.5) + 1):
    if i**2 == n:
        check = True
        break

if check:
    print(f"{n} là số chính phương")
else:
    print(f"{n} không phải là số chính phương")
