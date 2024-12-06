import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# 앱 제목
st.title("QR 코드 생성기")

# 사용자 입력 받기
url = st.text_input("QR 코드를 생성할 URL을 입력하세요")

# 버튼 클릭 시 실행
if st.button("QR 코드 생성"):
    if url:
        # QR 코드 생성
        qr = qrcode.QRCode(
            version=1, 
            error_correction=qrcode.constants.ERROR_CORRECT_L, 
            box_size=10, 
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # QR 코드 이미지를 생성
        img = qr.make_image(fill='black', back_color='white')

        # 이미지를 스트림으로 변환
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # 이미지 출력
        st.image(buffer, caption="생성된 QR 코드", use_column_width=True)

        # 다운로드 링크 제공
        st.download_button(
            label="QR 코드 다운로드",
            data=buffer,
            file_name="qrcode.png",
            mime="image/png"
        )
    else:
        st.warning("URL을 입력해 주세요.")
