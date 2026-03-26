import streamlit as st
from lolaemon_game import play_lolaemon, reset_daily_coins, state
from PIL import Image

# ---------------- 페이지 설정 ----------------
st.set_page_config(page_title="LoLaeMon 🐱‍💻", page_icon="🐱‍💻", layout="wide")

# ---------------- 배경 이미지 ----------------
# 안정적인 이미지 URL로 교체
bg_url = "https://images.unsplash.com/photo-1616627988316-7f7b486fa5a1?auto=format&fit=crop&w=1350&q=80"

st.markdown(
    f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("{bg_url}");
        background-size: cover;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- 도라에몽 헤더 ----------------
img_path = "C:/skn24/수업자료/08_large_language_model/04_rag/로라에몽 이미지.jpg"

# 이미지 열기
img = Image.open(img_path)

# Streamlit에 표시
st.image(img, width=500)
st.markdown("<h1 style='text-align:center'>LoLaeMon 🐱‍💻🔧</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center'>미래에서 온 로라에몽이 당신을 위해 발명을 만들어줘요!</p>", unsafe_allow_html=True)

# ---------------- 코인 & 상태 사이드바 ----------------
st.sidebar.header("💰 코인 & 발명 상태")
st.sidebar.write(f"남은 코인: {state['coins']}")
st.sidebar.write(f"최근 발명: {state['current_invention'][:100] if state['current_invention'] else '없음'}")
st.sidebar.write(f"히스토리 개수: {len(state['history'])}")

# ---------------- 사용자 입력 ----------------
user_input = st.text_input("발명 요청하기 (예: 시험 공부 도와줘!)")

# ---------------- 발명 버튼 ----------------
if st.button("🐱‍💻 발명하기"):
    if user_input.strip() != "":
        result = play_lolaemon("user_01", user_input)
        st.success("✅ 발명 결과")
        st.text_area("발명품 설명", result, height=300)
    else:
        st.warning("먼저 발명 요청 내용을 입력하세요!")

# ---------------- 업그레이드 버튼 ----------------
if st.button("🔧 방금 발명 업그레이드"):
    if state['current_invention']:
        result = play_lolaemon("user_01", "방금 만들 것을 업그레이드 해줘!")
        st.success("🔧 업그레이드 결과")
        st.text_area("업그레이드 발명품 설명", result, height=300)
    else:
        st.warning("먼저 발명을 진행해야 업그레이드할 수 있어요!")

# ---------------- 코인 초기화 ----------------
if st.button("💸 코인 초기화"):
    msg = reset_daily_coins(state)
    st.info(msg)