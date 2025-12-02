import turtle
import random

# Định nghĩa danh sách màu sắc
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

# Thiết lập đối tượng rùa (painter) và cửa sổ
window = turtle.Screen()
painter = turtle.Turtle()
painter.pensize(3)

# Tắt chế độ vẽ nhanh (cho phép bạn thấy quá trình vẽ)
painter.speed(0)
window.tracer(False)  # Tắt cập nhật màn hình để tăng tốc độ vẽ (optional)

# Vòng lặp chính để vẽ 10 hình tròn
for i in range(10):
    # 1. Chọn màu ngẫu nhiên và đặt màu nét vẽ
    color = random.choice(colors)
    painter.pencolor(color)
    
    # 2. Vẽ hình tròn
    painter.circle(100)
    
    # 3. Các lệnh xoay không ảnh hưởng đến vị trí cuối cùng do lệnh setposition
    # painter.right(30)
    # painter.left(60)
    
    # 4. Quan trọng: Đặt lại vị trí rùa về tâm (0, 0) để các hình tròn đồng tâm
    painter.setposition(0, 0)

window.tracer(True)  # Bật lại cập nhật màn hình
window.mainloop()    # Giữ cửa sổ mở
