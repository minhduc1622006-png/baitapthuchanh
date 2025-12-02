import turtle
import math

# --- Cấu hình ---
window = turtle.Screen()
window.bgcolor("white")  # Đặt màu nền trắng
window.title("Hoa văn Hình tròn Lồng nhau")

painter = turtle.Turtle()
painter.pensize(2)  # Độ dày nét vẽ
painter.speed(0)    # Tốc độ vẽ tối đa (fastest)
window.tracer(False) # Tắt cập nhật màn hình để vẽ nhanh hơn

# Định nghĩa các màu cần dùng: Đỏ, Xanh lá cây, Xanh dương
colors = ["red", "green", "blue"]

# --- Thiết lập Tham số Vẽ ---
radius = 100       # Bán kính của mỗi hình tròn/cung tròn
num_circles = 12   # Tổng số hình tròn cần vẽ (12 cung tròn tạo ra 6 cánh)
# Góc xoay giữa mỗi lần vẽ: 360 độ / 12 lần lặp = 30 độ
angle_step = 360 / num_circles

# --- Quá trình Vẽ ---
for i in range(num_circles):
    # 1. Chọn màu sắc theo chu kỳ: 0 -> đỏ, 1 -> xanh lá, 2 -> xanh dương, 3 -> đỏ, ...
    color_index = i % len(colors)
    painter.pencolor(colors[color_index])

    # 2. Xoay rùa để chuẩn bị vẽ hình tròn/cung tròn
    # Xoay theo góc bước đã tính
    painter.setheading(i * angle_step) 

    # 3. Di chuyển rùa đến vị trí bắt đầu vẽ cung tròn mà không để lại nét
    # Rùa di chuyển từ tâm (0,0) ra xa tâm một khoảng bằng bán kính để bắt đầu vẽ cung tròn
    painter.penup()
    painter.forward(radius)
    painter.pendown()

    # 4. Vẽ cung tròn (hoặc hình tròn)
    # Rùa vẽ hình tròn từ vị trí hiện tại. 
    # Vị trí này sẽ tạo ra hình tròn có tâm dịch chuyển ra khỏi gốc (0,0)
    # Bán kính âm làm rùa xoay theo chiều kim đồng hồ, giúp hình vẽ chính xác hơn
    painter.circle(-radius, 360) 

    # 5. Quay về tâm (0, 0) để bắt đầu lần lặp tiếp theo
    painter.penup()
    painter.home()
    
# Cập nhật màn hình và giữ cửa sổ mở
window.tracer(True)
window.mainloop()
