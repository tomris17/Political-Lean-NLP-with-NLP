import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Reddit Political Lean Analysis App", layout="centered")

st.title("Reddit Posts Political Lean Classification App")
st.write(
    "Bu uygulama, eğittiğiniz metin sınıflandırma modelini (`nlp_model.pkl`) kullanarak Reddit gönderilerinin siyasi eğilimini (Conservative veya Liberal) tahmin eder."
)

@st.cache_resource
def load_model():
    return joblib.load("nlp_model.pkl")

try:
    model = load_model()
    
    title_input = st.text_input("Gönderi Başlığı (Title):")
    text_input = st.text_area("Gönderi Metni (Text):")
    
    if st.button("Siyasi Eğilim Tahmini Yap"):
        if title_input.strip() != "" or text_input.strip() != "":
            content = title_input + " " + text_input
            st.success(f"Birleştirilen İçerik: {content}")
            st.info("Tahmin sonucu model yapısına göre gerçekleştirilecektir.")
        else:
            st.warning("Lütfen en az bir başlık veya metin girin.")

except Exception as e:
    st.error(f"Model yüklenirken bir hata oluştu: {e}")