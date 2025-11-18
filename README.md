**🇻🇳 Sentiment Analysis for Vietnamese (PhoBERT-based Transformer)**
Trợ lý phân loại cảm xúc Tiếng Việt được xây dựng dựa trên kiến trúc PhoBERT-base-v2 fine-tuned, triển khai bằng framework Streamlit và đóng gói bằng Docker.

1. Các Công nghệ Chính:
 * Mô hình: aiface/phobert-v2-3class_v1 (PhoBERT-base-v2 fine-tuned)
 * Thư viện: Hugging Face Transformers, PyTorch
 * Deployment: Docker (Đóng gói môi trường)
 * Frontend: Streamlit

2. Hướng dẫn Cài đặt & Chạy Dự án: 
Dự án này được đóng gói hoàn toàn bằng Docker, không yêu cầu cài đặt môi trường Python phức tạp.

## Điều kiện Tiên quyết: 

1.  Cài đặt **Docker** trên hệ thống của bạn.
2.  Tải xuống **TẤT CẢ** các file sau vào thư mục gốc của dự án:
    * `Dockerfile`
    * `requirements.txt`
    * `app.py`
    * `core_nlp.py`
    * `vietnamese_utils.py` 

3. Chạy Ứng dụng (3 Lệnh Cơ bản): 
Chạy các lệnh sau trong Terminal tại thư mục chứa file dự án: 
1. Build Docker Image: Xây dựng Docker Image từ Dockerfile. Lệnh này chỉ cần chạy một lần.
### docker build -t sentiment-assistant:final .
2. Chạy Docker Container: Chạy ứng dụng trong Container, ánh xạ cổng nội bộ (8501) ra cổng ngoại vi của máy bạn.
### docker run -d -p 8501:8501 --name final-app sentiment-assistant:final
Truy cập Local: Sau khi Container chạy, bạn có thể truy cập ứng dụng qua: http://localhost:8501

3. Công khai Ứng dụng qua Ngrok (Tùy chọn):
Sử dụng Ngrok để tạo một đường link công cộng (HTTPS) để chia sẻ dự án.
### ngrok http 8501
**LƯU Ý:** Bạn cần cài đặt Ngrok và đã đăng nhập để sử dụng lệnh này. Đường link công cộng sẽ được hiển thị trong Terminal.

4. Kết quả Đánh giá Hiệu suất:
 * Mô hình được đánh giá trên tập test 20 câu, bao gồm các trường hợp từ đơn giản đến phức tạp như câu kép, câu mỉa mai và ngữ cảnh trung tính.
 * Accuracy trên tập test 20 câu: 75%.
 * Mô hình vẫn gặp khó khăn khi phân loại các câu có cảm xúc **Trung tính phức tạp (Neutral)** hoặc **Phức tạp về mặt cấu trúc** (ví dụ: các câu có sự đối lập hoặc mang tính chất so sánh). Các trường hợp này thường bị dự đoán sai thành **Negative** do sự xuất hiện của các từ tiêu cực đơn lẻ trong câu.



