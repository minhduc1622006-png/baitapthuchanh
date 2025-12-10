print("tran minh duc")
import tkinter as tk
from tkinter import messagebox

# ==================== FORM A: THÔNG TIN CÁ NHÂN (Phần a) ====================
def create_personal_info_form():

    pass 

# ==================== FORM B: RADIO BUTTON (Phần b) ====================
def create_radio_form():
    radio_window = tk.Toplevel()
    radio_window.title("Chọn Lựa Chọn")
    radio_window.geometry("300x150")
    
    radio_value = tk.IntVar()
    radio_value.set(1) 
    
    def show_selection():
        selected_value = radio_value.get()
        messagebox.showinfo(
            "Kết quả lựa chọn",
            f"Bạn đã chọn giá trị: {selected_value}"
        )
        

    radio_frame = tk.LabelFrame(radio_window, text="Lựa Chọn Radio Button")
    radio_frame.pack(padx=10, pady=10, fill="x")
    
    tk.Radiobutton(
        radio_frame,
        text="Lựa chọn 1",
        variable=radio_value, 
        value=1              
    ).pack(anchor="w", padx=5)
    
    tk.Radiobutton(
        radio_frame,
        text="Lựa chọn 2",
        variable=radio_value,
        value=2
    ).pack(anchor="w", padx=5)
    
    tk.Radiobutton(
        radio_frame,
        text="Lựa chọn 3",
        variable=radio_value,
        value=3
    ).pack(anchor="w", padx=5)
    
    button_click = tk.Button(
        radio_window,
        text="Click Me",
        command=show_selection 
    )
    button_click.pack(pady=10)

    radio_window.grab_set() 
    radio_window.focus_set()
    radio_window.wait_window()

# ==================== CHẠY CHƯƠNG TRÌNH ====================

root = tk.Tk()
root.withdraw() 

create_radio_form()

root.mainloop()
