import re

value = []
items = [x for x in input("Nhập mật khẩu: ").split(",")]

for p in items:
    if not (6 <= len(p) <= 12):
        continue
    if re.search("[a-z]", p) and \
       re.search("[0-9]", p) and \
       re.search("[A-Z]", p) and \
       re.search("[$#@]", p) and \
       not re.search(r"\s", p):
        value.append(p)
print("Mật khẩu hợp lệ:", ",".join(value))
