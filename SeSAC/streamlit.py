# 스트림 릿 라이브러리
import streamlit as st 
import pandas as pd

# 타이틀과 헤더
st.title("이것은 스트림릿 헤더입니다.")
st.header("이것은 스트림릿 헤더입니다222.")

# 텍스트 입력
# Text / Write
st.text("Hello World! (text)")
st.write("Hello World! (write)")

# write
# '변수' -> 문자열, 숫자, 리스트, 딕셔너리, 데이터프레임
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
       Discover tips, trends, and personalized recommendations for your beauty journey.</p>
</div>
"""

# Google Fonts 적용
st.markdown(
    '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap" rel="stylesheet">',
    unsafe_allow_html=True
)
st.markdown(html_page, unsafe_allow_html=True)

# --------------------
st.success('success!')
st.warning('warning!')
st.error('err!')

# --------------------
# 이미지, 오디오, 비디오
from PIL import Image
image = Image.open('./img/beauty.jpg')
st.image(image, width = 300, caption = '~~ 이미지에요.')

# open('경로', 'wr') as f:
#   f.read()
# audio_file = open('경로', 'rb')
# audio_by = audio_file.read()
# st.audio(audio_by)

# 유튜브 영상 넣기
# 로컬 영상 -> 리드 후 넣기
# 외부 영상 -> 링크 입력
st.video("https://www.youtube.com/watch?v=grzhzh5PHX0")

# --------------------
# 상호작용

if st.button('눌러주세요'):
    st.text('버튼이 눌림')
    
# checkbox
if st.checkbox('check'):
    st.write('체크함')
    
# radiobutton
radio_button = st.radio('select', ['집에가기', '공부하기'])
if radio_button == '집에가기':
    st.text('저도요..')
    
else: 
    st.text('힘들지만 좋은 선택...')
    
# selectbox
city = st.selectbox('Your city', ['Seoul', 'Busan', 'etc'])
if city == 'Seoul':
    st.text('서울사람이구나')
    
# multi select
job = st.multiselect('your future job', ['programmer', 'data scientist', 'it consultant'])

# --------------------
# 정보를 input
name = st.text_input('이름을 기입하세요.', "예) 홍길동...")

# 숫자 입력
number = st.number_input('숫자를 입력하세요')

# text area
message = st.text_area('문자를 적어주세요', 'Write something')

# 슬라이더
select = st.slider('select a value', 1, 10)

if st.button('눌러보세요'):
    st.balloons()
    
# ----------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv('경로')

st.area_chart(df[['열1', '열2']])
st.bar_chart(df[['열1', '열2']])
st.line_chart(df[['열1', '열2']])

fig, ax = plt.subplots()
corr_plot = sns.heatmap(df[['열1', '열2']].corr(), annot=True)
st.pyplot(fig)

# st.header("Dataframes and Tables")

# import pandas as pd
# df = pd.read_csv("auto.csv")
# st.dataframe(df.head(10))

# st.table(df.head(10))


#PLOTTINGS
st.area_chart(df[["mpg","cylinders"]])
st.bar_chart(df[["mpg",	"cylinders"]].head(20))
st.line_chart(df[["mpg","cylinders"]].head(20))

#SEABORN
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()
corr_plot = sns.heatmap(df[["mpg","cylinders", "displacement"]].corr(), annot = True)
st.pyplot(fig)

# Date and Time
st.header("Date & Time")

import datetime

today = st.date_input("Today is", datetime.datetime.now())


import time 

hour = st.time_input("The time is", datetime.time(12,30))


# DISPLAY JSON CODE
data = {"name":"John","surname":"Wick"}
st.json(data)

#Displaying CODE
st.code("import pandas as pd")

julia_code = """
function doit(num::int)
	println(num)
end
"""

st.code(julia_code, language='julia')


st.header("Progress Bar and Spinner")

#Progress Bar
import time

my_bar = st.progress(0)
for value in range(100):
	time.sleep(1)
	my_bar.progress(value+1)

# #SPINNER
import time

with st.spinner("Please wait..."):
	time.sleep(10)
st.success("Done!")