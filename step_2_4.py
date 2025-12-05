# step_2_4.py - streamlit 이용해서 문자 인식해주는 웹 앱 제작
from pathlib import Path
import streamlit as st
from step_1 import OUT_DIR
from step_2_3 import read_text_and_draw_line

st.set_page_config(page_title="OCR 웹 앱", layout="centered")
st.title("이미지에서 문자 인식하기")
st.caption("by JimProKing")

uploaded = st.file_uploader("인식할 이미지 업로드하세요", type=["png", "jpg", "jpeg"])

if uploaded is not None:
    # 임시 저장
    tmp_path = OUT_DIR / f"temp_uploaded_{uploaded.name}"
    tmp_path.write_bytes(uploaded.getvalue())

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("원본 이미지")
        st.image(tmp_path.as_posix(), use_column_width=True)

    with col2:
        st.subheader("문자 인식 + 박스 결과")
        with st.spinner("문자를 인식하고 있습니다... 잠시만 기다려주세요!"):
            # 여기서 실제 OCR + 박스 그리기 실행
            read_text_and_draw_line(tmp_path)
        
        # 결과 이미지 표시
        result_image_path = OUT_DIR / "step_2_3.jpg"  # step_2_3에서 저장한 이름
        if result_image_path.exists():
            st.image(result_image_path.as_posix(), use_column_width=True)
            st.success("인식 완료!")
        else:
            st.error("결과 이미지를 찾을 수 없습니다.")