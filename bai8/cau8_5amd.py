import tkinter as tk

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Ví dụ Radio Buttons")

# 1. Khởi tạo biến điều khiển (IntVar)
# Biến này sẽ giữ giá trị số nguyên của lựa chọn hiện tại.
v = tk.IntVar()
v.set(1) # Thiết lập giá trị mặc định là 1 (tương ứng với Python)

# Danh sách các lựa chọn (text, value)
languages = [
 ("Python", 1),
 ("Perl", 2),
 ("Java", 3),
 ("C++", 4),
 ("C", 5)
]

# Hàm xử lý sự kiện
def ShowChoice():
    """In giá trị (value) của Radio Button được chọn ra console."""
    # Sửa lỗi: Gợi ý của bạn có lỗi ở vòng lặp. Cần dùng language[0] cho text và language[1] cho value.
    # Tuy nhiên, cách dùng enumerate trong gợi ý cũng có vấn đề. Tôi sẽ dùng cách truyền thống hơn.
    print(f"Giá trị lựa chọn: {v.get()}")
    
# Thêm Label tiêu đề
tk.Label(root,
         text="""Chọn ngôn ngữ lập trình yêu thích của bạn:""",
         justify=tk.LEFT,
         padx=20).pack(pady=(10, 0))

# 2. Tạo và đóng gói Radio Buttons
# Duyệt qua danh sách (text, value)
for text, val in languages:
    tk.Radiobutton(root,
                   text=text,             # Nhãn hiển thị (ví dụ: "Python")
                   padx=20,               # Padding bên trong
                   variable=v,            # Liên kết với biến điều khiển v
                   command=ShowChoice,    # Gọi hàm khi được chọn
                   value=val              # Giá trị được gán cho v khi nút này được chọn (ví dụ: 1)
                   ).pack(anchor=tk.W)    # Đặt nút về phía Tây (trái)

root.mainloop()
