import tkinter as tk
from tkinter import messagebox

# Định nghĩa một lớp (class) cho ứng dụng GUI
class UngDungGUI:
    # 1. Phương thức khởi tạo (Constructor)
    def __init__(self, master):
        # Thiết lập cửa sổ chính
        self.master = master
        master.title("Ứng dụng Tkinter OOP")
        master.geometry("350x150")

        # 2. Tạo và cấu hình Widget (Button)
        # c) Liên kết phương thức xử lý sự kiện
        self.nut_chuc_nang = tk.Button(
            master,
            text="Nhấn tôi!",
            fg="white",  # Màu chữ
            bg="blue",   # Màu nền
            font=('Arial', 12, 'bold'), # Đặt font
            command=self.xu_ly_su_kien # Gán phương thức của lớp
        )

        # Sử dụng Grid Layout Manager để căn giữa
        self.nut_chuc_nang.grid(row=0, column=0, padx=100, pady=50)

    # 3. Phương thức xử lý sự kiện phím bấm
    def xu_ly_su_kien(self):
        """
        Phương thức được gọi khi nut_chuc_nang được nhấn.
        """
        thong_bao = "Chào mừng đến với lập trình hướng đối tượng GUI!"
        print(f"Sự kiện nút bấm: {thong_bao}")
        messagebox.showwarning("Cảnh báo Nhấn nút", thong_bao)

# Phần chạy chính của chương trình
if __name__ == '__main__':
    # a) Xây dựng cửa sổ đồ họa window form (root window)
    cua_so_goc = tk.Tk()
    
    # Khởi tạo ứng dụng, truyền cửa sổ gốc vào lớp
    ung_dung = UngDungGUI(cua_so_goc)
    
    # Bắt đầu vòng lặp sự kiện chính
    cua_so_goc.mainloop()
