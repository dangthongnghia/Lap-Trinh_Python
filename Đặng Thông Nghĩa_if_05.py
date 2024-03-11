
print("Nhập vào số a: ")
a = float(input())
print("Nhập vào số b: ")
b = float(input())
print("Nhập vào số c: ")
c = float(input())

# Tính Delta
delta = b**2 - 4 * a * c

# Xác định nghiệm
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    x = -b / (2 * a)
    print(f"Phương trình có nghiệm kép x1 = x2 = {x:.2f}")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"Phương trình có hai nghiệm phân biệt:")
    print(f"x1 = {x1:.2f}")
    print(f"x2 = {x2:.2f}")
