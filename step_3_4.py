from pathlib import Path
import streamlit as st
from step_1 import OUT_DIR
from step_3_3 import OUT_3_3, read_text_and_fill_area

st.title("문자 인식 웹 앱")

uploaded = st.file_uploader("인식할 이미지 선택하세요.") #얘가 업로드 위젯임
if uploaded is not None:
    tmp_path = OUT_DIR / f"{Path(__file__).stem}.tmp"
    tmp_path.write_bytes(uploaded.getvalue())

    col_left, col_right = st.columns(2)
    with col_left:
        st.subheader("원본 이미지")
        st.image(tmp_path.as_posix()) #원본이미지 출력
    with col_right:
        st.subheader("문자 인식 결과")
        with st.spinner(text="문자를 인식하는 중입니다..."):
            read_text_and_fill_area(tmp_path)
        st.image(OUT_3_3.as_posix())