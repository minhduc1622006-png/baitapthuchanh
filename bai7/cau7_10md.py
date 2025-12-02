def longest_words(text):
    words = text.split()
    max_len = max(len(word) for word in words)
    return [word for word in words if len(word) == max_len]

# Ví dụ sử dụng
text = "Python là một ngôn ngữ lập trình tuyệt vời và mạnh mẽ"
print("Các từ dài nhất:", longest_words(text))
