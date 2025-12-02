# Bước 1: Khởi tạo window form
root = tk.Tk()
root.title("tk")
root.geometry("400x300") # Thiết lập kích thước cửa sổ

# Tạo thanh Menu Bar
menu = tk.Menu(root)
root.config(menu=menu) # Gán Menu Bar vào cửa sổ

# Xây dựng Menu "File"
filemenu = tk.Menu(menu, tearoff=0) # tearoff=0 loại bỏ gạch ngang ở đầu menu
menu.add_cascade(label="File", menu=filemenu) # Thêm File vào Menu Bar

# Các lệnh trong Menu "File" theo hình mẫu (New, Open, Exit)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator() # Dòng phân cách
filemenu.add_command(label="Exit", command=lambda: ExitApp(root)) # Truyền root vào hàm Exit

# Xây dựng Menu "Insert"
insertmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu) # Thêm Insert vào Menu Bar

# Các lệnh trong Menu "Insert" theo hình mẫu (Text, Picture)
insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)

# Xây dựng Menu "Help"
helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu) # Thêm Help vào Menu Bar

# Các lệnh trong Menu "Help" (About)
helpmenu.add_command(label="About", command=About)

# Bắt đầu vòng lặp sự kiện chính
root.mainloop()
