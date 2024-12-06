# 스트림 릿 라이브러리
import streamlit as st 
import pandas as pd
from PIL import Image

# 페이지 설정
st.set_page_config(
    page_title="Beauty Hub",
    page_icon="💄",
    layout="centered"
)

# Google Fonts 적용
st.markdown(
    '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Roboto:wght@300;400&display=swap" rel="stylesheet">',
    unsafe_allow_html=True
)

# 타이틀과 헤더
st.markdown(
    """
    <h1 style="
        text-align: center; 
        color: #FF8BA0; 
        font-family: 'Playfair Display', serif; 
        font-weight: bold;">
        이것은 스트림릿 헤더입니다.
    </h1>
    <h2 style="
        text-align: center; 
        color: #B085A1; 
        font-family: 'Roboto', sans-serif;">
        이것은 스트림릿 헤더입니다222.
    </h2>
    """,
    unsafe_allow_html=True
)

# 텍스트 입력
st.markdown(
    """
    <div style="
        text-align: center; 
        color: #666; 
        font-family: 'Roboto', sans-serif;">
        <p>Hello World! (text)</p>
        <p><strong>Hello World! (write)</strong></p>
    </div>
    """,
    unsafe_allow_html=True
)

# DataFrame 출력
st.write(pd.DataFrame({'first': [1, 2, 3, 4], 
                       'second': [4, 5, 6, 7]}))

# markdown
html_page = """
<div style="
    background: linear-gradient(to bottom right, #FFDEE9, #B5FFFC);
    padding: 50px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    text-align: center;
    font-family: 'Playfair Display', serif;">
   <p style="
       color: #FF8BA0;
       font-size: 28px;
       font-weight: bold;
       margin: 0;">Welcome to Your Beauty Hub!</p>
   <p style="
       color: #FF8BA0;
       font-size: 18px;
       margin-top: 10px;">
       Discover tips, trends, and personalized recommendations for your beauty journey.
   </p>
</div>
"""
st.markdown(html_page, unsafe_allow_html=True)

# --------------------
# Alert 메시지 스타일링
st.success('🎉 Success: This is a success message!')
st.warning('⚠️ Warning: Be careful of potential issues.')
st.error('❌ Error: Something went wrong!')

# --------------------
# 이미지
image = Image.open('./img/beauty.jpg')
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{st.image(image, width=300, caption='~~ 이미지에요.')}" alt="Beauty Image" style="border-radius: 10px;"/>
    </div>
    """,
    unsafe_allow_html=True
)

# 비디오
st.markdown(
    """
    <div style="text-align: center;">
        <iframe width="560" height="315" 
                src="https://www.youtube.com/embed/grzhzh5PHX0" 
                title="YouTube video player" 
                frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen>
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------
# 상호작용
if st.button('✨ 눌러주세요'):
    st.text('버튼이 눌림')
