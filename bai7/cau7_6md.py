import os

def file_read_from_tail(fname, lines):
    bufsize = 8192
    fsize = os.stat(fname).st_size
    iter = 0

    with open(fname, "r") as f:
        if bufsize > fsize:
            bufsize = fsize - 1

        data = []

        while True:
            iter += 1
            # Di chuyển con trỏ đến vị trí cách cuối file bufsize*iter byte
            f.seek(max(fsize - bufsize * iter, 0))

            data.extend(f.readlines())

            # Nếu đã đủ số dòng hoặc đã tới đầu file thì in ra
            if len(data) >= lines or f.tell() == 0:
                print("".join(data[-lines:]))
                break


file_read_from_tail("test.txt", 2)
