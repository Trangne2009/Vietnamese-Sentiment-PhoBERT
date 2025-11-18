import streamlit as st 
import pandas as pd 

from core_nlp import classify_sentiment as bitch, SENTIMENT_PIPELINE
from database import load_history, save_history

# --- A. CẤU HÌNH VÀ TẢI TÀI NGUYÊN ---
@st.cache_resource
def get_pipeline():
    return SENTIMENT_PIPELINE

NLP_PIPELINE = get_pipeline() 

st.set_page_config(page_title="Trợ Lý Phân Loại Cảm Xúc Tiếng Việt", layout="wide")
st.title("Trợ Lý Phân Loại Cảm Xúc Tiếng Việt (Transformer)")
st.caption("Sử dụng mô hình PhoBERT-base-v2 fine-tuned cho Sentiment Analysis.")

if 'history_limit' not in st.session_state:
    st.session_state.history_limit = 50
    
# --- B. HÀM HIỂN THỊ HỖ TRỢ ---
def display_sentiment_result(sentiment, score=None):
    label_map = {
        "POSITIVE": {"icon": "😊", "color": "#28a745", "text": "TÍCH CỰC"},
        "NEGATIVE": {"icon": "😠", "color": "#dc3545", "text": "TIÊU CỰC"},
        "NEUTRAL": {"icon": "😐", "color": "#ffc107", "text": "TRUNG TÍNH"},
        "ERROR": {"icon": "❌", "color": "gray", "text": "LỖI"}
    }
    
    info = label_map.get(sentiment, label_map["ERROR"]) 
    score_display = f" (Độ tin cậy: {score*100:.2f}%)" if score is not None else ""
    
    st.markdown(
        f"<div style='background-color: {info['color']}; padding: 12px; border-radius: 6px; color: white; font-weight: bold; font-size: 18px; '>"
        f"{info['icon']} KẾT QUẢ: {info['text']}{score_display}"
        f"</div>", 
        unsafe_allow_html= True
    )
    
# --- C. KHU VỰC PHÂN LOẠI ---
st.header("I. Phân Loại Cảm Xúc")

input_text = st.text_area("Nhập câu tiếng Việt của bạn: ", height=100)

if st.button("Phân Loại Cảm Xúc"): 
    if NLP_PIPELINE is None:
        st.error("Lỗi: Mô hình NLP chưa được tải thành công. Vui lòng kiểm tra cài đặt.")
    elif not input_text.strip():
        st.error("Vui lòng nhập văn bản.")   
    else: 
        with st.spinner('Đang phân tích cảm xúc...'):
            try: 
                result = bitch(input_text)
                
                final_sentiment = result['sentiment']
                final_score = result.get('score') 
                
                st.info(f"👉 **Chuỗi đã được chuẩn hóa & tách từ (Preprocessed):**")
                st.markdown(
                    f"<p style='color: #007bff; font-style: italic; font-weight: bold;'>{result['processed_text']}</p>",
                    unsafe_allow_html=True
                )
                
                display_sentiment_result(final_sentiment, final_score)
                
                if final_sentiment != "ERROR":
                    save_history(input_text, final_sentiment)
                    
            except ValueError as e:
                st.warning(f"⚠️ **Thông báo pop-up:** Câu nhập không hợp lệ! Lý do: {e}")   
            except Exception as e: 
                st.error(f"❌ **Thông báo pop-up:** Câu không hợp lệ, thử lại! Lỗi Pipeline: {e}")       
                
# --- D. KHU VỰC LỊCH SỬ ---    
st.header("II. Lịch Sử Phân Loại")     

history_df = load_history(st.session_state.history_limit)

if not history_df.empty:
    st.subheader(f"Hiển thị {len(history_df)} bản ghi mới nhất:")
    
    st.dataframe(
        history_df,
        width='stretch',
        column_order=("timestamp", "text", "sentiment")
    )
    
    if len(history_df) == st.session_state.history_limit:
        if st.button("Tải thêm 50 bản ghi cũ hơn"):
            st.session_state.history_limit += 50
            st.rerun() 
else:
    st.info("Chưa có lịch sử phân loại nào được lưu trong cơ sở dữ liệu.")
    
        
