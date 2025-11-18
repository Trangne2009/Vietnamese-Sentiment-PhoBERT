# SỬ DỤNG HÌNH ẢNH CƠ SỞ (BASE IMAGE)
# Sử dụng Python 3.11 Slim (nhẹ hơn)

FROM python:3.11-slim

# ĐẶT BIẾN MÔI TRƯỜNG
# Thiết lập UTF-8 cho môi trường Tiếng Việt
ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1 

# CÀI ĐẶT THƯ MỤC LÀM VIỆC TRONG CONTAINER
WORKDIR /app

# SAO CHÉP CÁC FILE CẦN THIẾT
# Sao chép file requirements.txt và cài đặt thư viện
COPY requirements.txt .
RUN pip install --no-cache-dir --timeout 3600 -r requirements.txt

# SAO CHÉP MÃ NGUỒN CỦA ỨNG DỤNG
# Sao chép toàn bộ mã nguồn vào thư mục /app trong container
# Đảm bảo app.py, core_nlp.py, vietnamese_utils.py được copy
COPY . . 

# MỞ CỔNG MẶC ĐỊNH CỦA STREAMLIT
EXPOSE 8501

# LỆNH KHỞI CHẠY ỨNG DỤNG
# Khi container khởi động, nó sẽ chạy lệnh này
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.enableCORS", "false"]

