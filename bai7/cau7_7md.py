def count_lines(filename):
    count = 0
    with open(filename, "r") as f:
        for line in f:
            count += 1
    return count

# Ví dụ sử dụng
filename = "a.txt"
print("Số dòng trong tệp là:", count_lines(filename))
