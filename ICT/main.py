import streamlit as st

# 간단한 제목 출력
st.title("Streamlit 간단한 예시")

# 사용자 입력 받기
user_input = st.number_input("숫자를 입력하세요", min_value=0)

# 계산 결과 출력
st.write(f"입력한 숫자의 두 배는: {user_input * 2} 입니다.")
