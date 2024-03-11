n = int(input("Nhập số nguyên N: "))
def So_Chan():
# In ra các số chẵn
    print("Các số chẵn:")
    for i in range(1, n):
        if i % 2 == 0:
         print(i, end=" ")

def So_Le():
# In ra các số lẻ
    print("\nCác số lẻ:")
    for i in range(1, n):
        if i % 2 != 0:
            print(i, end=" ")

def Menu():
    while (True):
        print("1. Nhập vào số nguyên N: ")
        print('2. In ra số chẳn:')
        print('3. In ra số lẻ:')
luachon = int(input('Nhập vào lựa chọn của bạn:'))
if( luachon > 0 and luachon < 4):
    print(' ')
else:
    print('Lựa chọn không hợp lệ.')
    if(luachon == 1):
        n = int(input('Nhập vào số nguyên N:'))
    elif(luachon == 2):
        print('In ra các số chẳn')
        So_Chan(n)
    elif(luachon == 2):
        print('In ra các số chẳn')
        So_Le(n)