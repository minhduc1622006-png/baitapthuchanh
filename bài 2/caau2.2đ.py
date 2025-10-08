import math

x1 = float(input("Nhập x1: "))
y1 = float(input("Nhập y1: "))
x2 = float(input("Nhập x2: "))
y2 = float(input("Nhập y2: "))

khoang_cach = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Khoảng cách giữa hai điểm là: {khoang_cach:.2f}")
