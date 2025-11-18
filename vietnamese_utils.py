from underthesea import word_tokenize 

# --- A. Từ điển Chuẩn hóa ---
TEENCODE_DICT = {
    # Viết tắt phổ biến:
    'ko': 'không', 'k': 'không', 'bt': 'bình thường', 'cx': 'cũng', 
    'nhju': 'nhiều', 'j': 'gì', 'vs': 'với', 'r': 'rồi', 'lun': 'luôn',
    'đc': 'được', 'tk': 'thằng', 'uk': 'ừ', 'nx': 'nhận xét', 'qá': 'quá', 't': 'tôi', 
    # Teencode/Lặp từ (Bổ sung theo yêu cầu đồ án: thay 'rất' -> 'rất/rất')
    'rất rất rất': 'rất rất',
    'vcl': 'vãi cả linh hồn',
    
    # Thiếu dấu/sai chính tả thường gặp
    'thik': 'thích', 'dz': 'dễ thương', 'mng': 'mọi người', 'do': 'dở', 'rat': 'rất', 'hom': 'hôm',
    'ghet': 'ghét', 'pùn': 'buồn', 'nhien': 'nhiên', 'qua': 'quá',
    'mon': 'món', 'an': 'ăn', 'khong': 'không', 'gian': 'gian', 'on': 'ồn', 'ao': 'ào', 'tuy': 'tuy', 
    
    # Thêm các cụm từ thiếu dấu mà bạn đã định nghĩa:
    'mon an': 'món ăn', 
    'khong gian': 'không gian', 
    'on ao': 'ồn ào',
    'tuy nhien': 'tuy nhiên' 
}

def preprocess_text(raw_text: str) -> str: 
    # 1. Kiểm tra lỗi nhập liệu
    # Bắt buộc phải có trong hàm này để raise lỗi ValueError
    if len(raw_text.strip()) < 5: 
        raise ValueError("Câu nhập quá ngắn, vui lòng nhập tối thiểu 5 ký tự.")
    
    # 2. Chuyển chữ thường
    text = raw_text.lower() 
    
    # 3. THÊM KHOẢNG TRẮNG ĐẦU VÀ CUỐI (Tạo ranh giới từ)
    text = " " + text + " "
    
    # Sắp xếp từ điển để xử lý cụm từ dài trước (VD: 'mon an' trước 'mon')
    sorted_teencode = sorted(TEENCODE_DICT.items(), key=lambda item: len(item[0]), reverse=True)
    
    for old, new in sorted_teencode:
        # Sử dụng replace() để thay thế các cụm từ dài
        text = text.replace(" " + old + " ", " " + new + " ")
        
    text = text.strip()  
    
    tokenized_list = word_tokenize(text) 
    
    text = " ".join(tokenized_list)
    
    return text 