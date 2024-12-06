import streamlit as st
import pyshorteners

# 앱 제목
st.title("URL 줄이기 앱")

# 사용자 입력 받기
url = st.text_input("URL을 입력하세요")

# 버튼 클릭 시 실행
if st.button("URL 줄이기"):
    if url:
        try:
            # URL을 줄이는 로직
            s = pyshorteners.Shortener()
            short_url = s.tinyurl.short(url)
            
            # 결과 출력
            st.success(f"줄여진 URL: {short_url}")
            st.write(f"[{short_url}]({short_url})")
        except Exception as e:
            st.error("유효한 URL을 입력하세요.")
    else:
        st.warning("URL을 입력해 주세요.")
