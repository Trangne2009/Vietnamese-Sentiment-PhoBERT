# 🇻🇳 Sentiment Analysis for Vietnamese (PhoBERT-based Transformer)

Trợ lý phân loại cảm xúc Tiếng Việt được xây dựng trên kiến trúc **Transformer (PhoBERT-base-v2 Fine-tuned)**, triển khai bằng framework Streamlit, và đóng gói hoàn toàn bằng công nghệ **MLOps (Docker)** để đảm bảo tính tái lập và khả năng triển khai.

---

## 1. Công Nghệ & Kiến Trúc

| Hạng mục | Công nghệ Chính | Chi tiết |
| :--- | :--- | :--- |
| **Mô hình Cơ sở** | aiface/phobert-v2-3class\_v1 | Kiến trúc **PhoBERT-base-v2** đã được fine-tuned, chuyên biệt cho Tiếng Việt. |
| **Thư viện Nền** | Hugging Face Transformers, PyTorch | Đảm bảo hiệu suất tính toán và xử lý ngữ cảnh sâu của mô hình Transformer. |
| **Giao diện (Frontend)** | **Streamlit** | Cung cấp giao diện tương tác trực quan (Web-based UI) cho người dùng cuối. |
| **Triển khai (Deployment)** | **Docker** | Đóng gói môi trường hoàn chỉnh theo tiêu chuẩn MLOps. |

---

## 2. Hướng Dẫn Cài Đặt & Chạy Dự Án

Dự án đã được **Dockerization hoàn toàn**, cho phép khởi chạy nhanh chóng mà không cần cài đặt môi trường Python phức tạp.

### 2.1. Điều kiện Tiên quyết

1.  Cài đặt **Docker Desktop** trên hệ thống của bạn.
2.  Đảm bảo **TẤT CẢ** các file cấu hình và mã nguồn (`Dockerfile`, `requirements.txt`, `app.py`, `core_nlp.py`, `vietnamese_utils.py`) được đặt trong cùng thư mục gốc của dự án.

### 2.2. Quy trình Khởi chạy (3 Lệnh Cơ bản)

Thực hiện các lệnh sau trong Terminal (Command Line) tại thư mục gốc của dự án:

| Lệnh | Mục đích |
| :--- | :--- |
| **1. Xây dựng Docker Image** | **Tạo Image** chứa môi trường, thư viện và mô hình. Lệnh này chỉ cần chạy **một lần duy nhất**. |
| `docker build -t sentiment-assistant:final .` | |
| **2. Chạy Docker Container** | **Khởi chạy ứng dụng** dưới dạng Container nền, ánh xạ cổng nội bộ (`8501`) ra cổng ngoại vi. |
| `docker run -d -p 8501:8501 --name final-app sentiment-assistant:final` | |
| **3. Truy cập Local Demo** | Mở trình duyệt web để tương tác với ứng dụng. |
| **`http://localhost:8501`** | |

---

## 3. Kết Quả Đánh Giá Hiệu Suất

### 3.1. Chỉ số Tổng quan

* Mô hình được đánh giá trên tập test **20 câu**, bao gồm các trường hợp từ đơn giản đến phức tạp như câu kép, câu mỉa mai và ngữ cảnh trung tính.
* **Accuracy trên tập test:** **75%**.

### 3.2. Phân tích Lỗi (Critical Thinking)

* Mô hình vẫn gặp khó khăn khi phân loại các câu có cảm xúc **Trung tính phức tạp (Neutral)** hoặc **Phức tạp về mặt cấu trúc** (ví dụ: các câu có sự đối lập hoặc mang tính chất so sánh).
* Các trường hợp này thường bị dự đoán sai thành **Negative** do sự xuất hiện của các từ tiêu cực đơn lẻ trong câu.

---

## 4. Trạng Thái Triển khai (Deployment Status)

| Trạng thái | Chi tiết | Tóm tắt |
| :--- | :--- | :--- |
| **Đóng gói MLOps** | Ứng dụng đã được đóng gói hoàn chỉnh bằng **Docker Container**. | **Thành công** |
| **Live Demo Công khai** | Dịch vụ Live Demo công khai không được triển khai, do mô hình PhoBERT lớn vượt quá giới hạn tài nguyên RAM và thời gian khởi động (Startup Timeout) của các gói Cloud miễn phí (Render Free Tier, Heroku Free). | **Bị giới hạn bởi tài nguyên/chi phí** |

**Kết luận Kỹ thuật:**

* Đã thành công với **Dockerization**, đảm bảo khả năng tái lập và triển khai cục bộ.
* Đã hiểu rõ về các ràng buộc về **chi phí/tài nguyên** trong môi trường thực tế (Cloud Production).

**💡 Khả năng chạy:** Vui lòng xem **[Video Demo](https://drive.google.com/file/d/1kZgmtBuqZiGNVFikUnt4J6GcAhuWNfak/view?usp=drive_link)** hoặc chạy dự án cục bộ bằng Docker.