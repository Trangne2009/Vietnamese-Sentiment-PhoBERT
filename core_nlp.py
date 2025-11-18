from transformers import pipeline 
from vietnamese_utils import preprocess_text

MODEL_NAME = "aiface/phobert-v2-3class_v1"

def load_nlp_pipeline(): 
    try: 
        sentiment_pipeline = pipeline("sentiment-analysis", model=MODEL_NAME, tokenizer=MODEL_NAME, tokenizer_kwargs={'max_length': 128, 'truncation': True})
        print(f"Đã tải thành công PhoBERT Pipeline: {MODEL_NAME}")
        return sentiment_pipeline
    except Exception as e: 
        print(f"Lỗi tải model {MODEL_NAME}: {e}. Chuyển sang DistilBERT dự phòng.")
        return pipeline("sentiment-analysis", model="distilbert-base-multilingual-cased", tokenizer_kwargs={'max_length': 128, 'truncation': True})
    
SENTIMENT_PIPELINE = load_nlp_pipeline() 

LABEL_MAPPING = {
    # ÁNH XẠ CHÍNH XÁC TỪ CONFIG.JSON
    'LABEL_0': 'NEGATIVE',
    'LABEL_1': 'NEUTRAL', 
    'LABEL_2': 'POSITIVE', 
    
    # Giữ các nhãn chữ
    'POSITIVE': 'POSITIVE', 
    'NEGATIVE': 'NEGATIVE',
    'NEUTRAL': 'NEUTRAL'
}

def classify_sentiment(raw_text: str) -> dict:
    if SENTIMENT_PIPELINE is None:
        raise Exception("Lỗi pipeline, không thể phân loại.") 
    
    text_processed = preprocess_text(raw_text)
            
    try: 
        results = SENTIMENT_PIPELINE(text_processed)[0]
        score = results['score']
        raw_label = results['label'].upper() 
        
        # BƯỚC GỠ LỖI TẠM THỜI: In nhãn thô ra terminal
        print(f"DEBUG: Nhãn thô (Raw Label) cho câu '{raw_text}': {raw_label}")
        # BƯỚC GỠ LỖI TẠM THỜI: In điểm số ra terminal
        print(f"DEBUG: Điểm số (Score) cho câu '{raw_text}': {score}")
        
        if score < 0.5:
            final_sentiment = "NEUTRAL"
        else: 
            final_sentiment = LABEL_MAPPING.get(raw_label, "NEUTRAL")
            
        return {
            "text": raw_text,
            "sentiment": final_sentiment,
            "score": score,
            "processed_text": text_processed
        }   
    except Exception as e: 
        raise Exception(f"Lỗi trong quá trình gọi pipeline: {e}") 