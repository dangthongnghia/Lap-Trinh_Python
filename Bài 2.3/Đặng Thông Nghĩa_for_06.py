n = int(input('Nhập số nguyên N: '))

# Tạo một dãy số từ 1 đến n
numbers = range(1, n + 1)

# Sử dụng vòng lặp for để tính bình phương của mỗi số và in ra dãy số
for i in numbers:

    print(f' {i}: {i*i}', end="  ") # In ra số và bình phương của nó, cách nhau bởi dấu phẩy


    