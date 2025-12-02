import tkinter as tk
from tkinter import messagebox

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Indicator Buttons (Nút Lựa Chọn Hình Chữ Nhật)")

# 1. Khởi tạo biến điều khiển
v = tk.IntVar()
v.set(1) # Giá trị mặc định là 1 (Python)

# Danh sách các lựa chọn
languages = [
 ("Python", 1),
 ("Perl", 2),
 ("Java", 3),
 ("C++", 4),
 ("C", 5)
]

# Hàm xử lý sự kiện
def ShowChoice():
    """In giá trị (value) của Indicator Button được chọn ra console 
       và hiển thị thông báo."""
    lua_chon = v.get()
    print(f"Giá trị lựa chọn hiện tại: {lua_chon}")
    
    # Tìm tên ngôn ngữ tương ứng để hiển thị trong thông báo
    ten_ngon_ngu = ""
    for name, val in languages:
        if val == lua_chon:
            ten_ngon_ngu = name
            break
            
    messagebox.showinfo("Lựa chọn", f"Bạn đã chọn: {ten_ngon_ngu}")

# Thêm Label tiêu đề
tk.Label(root,
         text="""Chọn ngôn ngữ lập trình yêu thích của bạn:""",
         justify=tk.LEFT,
         padx=20).pack(pady=(10, 0))

# 2. Tạo và đóng gói Indicator Buttons
for text, val in languages:
    tk.Radiobutton(root,
                   text=text,
                   variable=v,
                   command=ShowChoice,
                   value=val,
                   
                   # === Các thuộc tính để chuyển thành Indicator Button ===
                   **indicatoron=0**,         # Tắt hình tròn indicator (chuyển sang hình chữ nhật)
                   **width=20**,              # Đặt chiều rộng cố định cho nút
                   # =======================================================
                   
                   padx=20,               # Padding bên trong (căn lề chữ)
                   pady=5,                # Padding dọc để các nút cách nhau
                   relief=tk.RAISED,      # Hiệu ứng nổi
                   bg="lightgray"         # Màu nền
                   ).pack(anchor=tk.W, padx=20, pady=2)

root.mainloop()
