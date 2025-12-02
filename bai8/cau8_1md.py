import turtle

# Thiết lập cửa sổ
window = turtle.Screen()
window.bgcolor("lightgreen")

# Thiết lập đối tượng rùa (painter)
painter = turtle.Turtle()
painter.color('blue')        # Đặt màu nét vẽ và màu tô là xanh dương (Blue)
painter.pensize(3)           # Độ dày nét vẽ là 3

# Tắt chế độ vẽ nhanh (cho phép bạn thấy quá trình vẽ)
painter.speed(0) 
window.tracer(False)         # Tắt cập nhật màn hình để tăng tốc độ vẽ

# Hàm vẽ hình vuông
def drawsq(t, s):
    """Vẽ một hình vuông với rùa t, độ dài cạnh s."""
    for i in range(4):
        t.forward(s)
        t.left(90)

# Vòng lặp chính để vẽ hình phức tạp
# Vòng lặp này sẽ chạy 179 lần (từ 1 đến 179)
for i in range(1, 180):
    painter.left(18)         # Xoay rùa 18 độ
    drawsq(painter, 200)     # Vẽ hình vuông có cạnh 200

window.tracer(True)          # Bật lại cập nhật màn hình
window.mainloop()            # Giữ cửa sổ mở cho đến khi người dùng đóng
