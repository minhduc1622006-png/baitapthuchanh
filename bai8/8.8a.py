print("tran minh duc")
import tkinter as tk
from tkinter import messagebox

# ==================== FORM A: THÔNG TIN CÁ NHÂN ====================
def create_personal_info_form():
    info_window = tk.Toplevel()
    info_window.title("Thông tin cá nhân")
    info_window.geometry("400x250") 
    
    def show_info():
        ho_ten = entry_name.get()
        ngay_sinh = entry_dob.get()
        mssv = entry_id.get()
        nganh_hoc = entry_major.get()
        
        messagebox.showinfo(
            "Thông tin đã nhập",
            f"Họ tên: {ho_ten}\nNgày sinh: {ngay_sinh}\nMSSV: {mssv}\nNgành học: {nganh_hoc}"
        )
        
    
    tk.Label(info_window, text="Họ tên:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_name = tk.Entry(info_window, width=40)
    entry_name.grid(row=0, column=1, padx=10, pady=5)
    entry_name.insert(0, "tran minh duc")

    tk.Label(info_window, text="Ngày sinh (dd/mm/yyyy):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_dob = tk.Entry(info_window, width=40)
    entry_dob.grid(row=1, column=1, padx=10, pady=5)
    entry_dob.insert(0, "16/02/2006")

    tk.Label(info_window, text="MSSV:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_id = tk.Entry(info_window, width=40)
    entry_id.grid(row=2, column=1, padx=10, pady=5)
    entry_id.insert(0, "245752021610014")
    
    tk.Label(info_window, text="Ngành học:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    entry_major = tk.Entry(info_window, width=40)
    entry_major.grid(row=3, column=1, padx=10, pady=5)
    entry_major.insert(0, "KY THUAT TU DONG HOA")
    
    button_show = tk.Button(
        info_window,
        text="Hiển thị thông tin",
        command=show_info  
    )
    button_show.grid(row=4, column=0, columnspan=2, pady=10)

    info_window.grab_set() 
    info_window.focus_set()
    info_window.wait_window()

# ==================== CHẠY CHƯƠNG TRÌNH ====================

root = tk.Tk()
root.withdraw() 

create_personal_info_form()

root.mainloop()
