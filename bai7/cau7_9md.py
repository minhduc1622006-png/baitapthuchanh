def copy_file(source, destination):
    with open(source, "r") as src:
        with open(destination, "w") as dest:
            for line in src:
                dest.write(line)

# Ví dụ sử dụng
copy_file("a.txt", "b.txt")
print("Đã sao chép nội dung từ a.txt sang b.txt")
