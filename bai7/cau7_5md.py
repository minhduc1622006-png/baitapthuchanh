def file_read(fname):
    # Mở tệp ở chế độ append để nối thêm nội dung
    with open(fname, "a") as myfile:
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises\n")

    # Mở lại tệp để đọc nội dung
    with open(fname, "r") as txt:
        print(txt.read())

file_read("abc.txt")
