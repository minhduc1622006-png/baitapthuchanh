import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog # Cần cho chức năng Open

# Bước 3: Thêm các phương thức xử lý sự kiện (Open, Exit, InsText, InsPic)
def NewFile():
    """Xử lý sự kiện khi nhấn 'New' hoặc 'New File!'"""
    print("New File!")
    # Sử dụng messagebox để hiển thị thông báo
    messagebox.showinfo("Thông báo", "Lựa chọn: New File!")

def OpenFile():
    """Xử lý sự kiện khi nhấn 'Open'. Mở hộp thoại chọn file."""
    # Mở hộp thoại file, trả về đường dẫn file đã chọn
    file_path = filedialog.askopenfilename(
        title="Chọn một tập tin",
        filetypes=(("Tất cả các tập tin", "*.*"), ("Tập tin văn bản", "*.txt"))
    )
    if file_path:
        print(f"File đã chọn: {file_path}")
        messagebox.showinfo("Thông báo", f"Lựa chọn: Open. File đã chọn: {file_path}")
    else:
        messagebox.showinfo("Thông báo", "Không có file nào được chọn.")

def ExitApp(root):
    """Xử lý sự kiện khi nhấn 'Exit'. Thoát ứng dụng."""
    print("Thoát ứng dụng...")
    root.quit() # Lệnh thoát vòng lặp chính của Tkinter

def About():
    """Xử lý sự kiện khi nhấn 'About'."""
    print("This is a simple example of a menu")
    messagebox.showinfo("Về chương trình", "Chương trình mẫu sử dụng Tkinter để tạo Menu Bar.")

def InsText():
    """Xử lý sự kiện khi nhấn 'Text'."""
    print("Insert Text!")
    messagebox.showinfo("Thông báo", "Lựa chọn: Insert Text.")

def InsPic():
    """Xử lý sự kiện khi nhấn 'Picture'."""
    print("Insert Picture!")
    messagebox.showinfo("Thông báo", "Lựa chọn: Insert Picture.")
