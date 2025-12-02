def read_entire_file(file_path):
    """
    Đọc toàn bộ nội dung của một tệp văn bản và in ra màn hình.
    :param file_path: Đường dẫn đến tệp cần đọc.
    """
    try:
        # Sử dụng 'with open' để mở tệp. 'r' là chế độ chỉ đọc.
        with open(file_path, 'r', encoding='utf-8') as file:
            # Phương thức .read() sẽ đọc toàn bộ nội dung của tệp vào một chuỗi (string) duy nhất.
            file_content = file.read()
            
            # In nội dung tệp ra màn hình
            print("--- Nội dung toàn bộ tệp ---")
            print(file_content)
            print("----------------------------")
            
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy tệp tại đường dẫn: {file_path}")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi đọc tệp: {e}")

# --- Ví dụ sử dụng ---

# Thay đổi 'your_file_name.txt' bằng đường dẫn thực tế của tệp bạn muốn đọc.
# Ví dụ: 'D:/Documents/my_text.txt' hoặc 'a.txt' (nếu tệp nằm cùng thư mục với chương trình).
file_to_read = 'a.txt' 

read_entire_file(file_to_read)

# Lưu ý: Thêm tham số `encoding='utf-8'` là quan trọng để đảm bảo 
# các ký tự tiếng Việt (hoặc các ký tự đặc biệt khác) được đọc chính xác.
