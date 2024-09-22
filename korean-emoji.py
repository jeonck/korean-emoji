# korean_emoji_chat.py
import streamlit as st

def korean_emoji_chat():
    # 감성 아이콘 딕셔너리
    emoticons = {
        "ㄱ.행복": "😊",
        "ㄱ.슬픔": "😢",
        "ㄱ.화남": "😡",
        "ㄱ.사랑": "❤️",
        "ㄱ.놀람": "😲",
        "ㄱ.웃음": "😂",
        "ㄱ.키스": "😘",
        "ㄱ.울음": "😭",
        "ㄱ.기쁨": "😁",
        "ㄱ.눈물": "😥",
        "ㄱ.두려움": "😱",
        "ㄱ.피곤": "😴",
        "ㄱ.아픔": "🤕",
        "ㄱ.혼란": "😕",
        "ㄱ.굳센": "💪",
        "ㄱ.오케이": "👌",
        "ㄱ.승리": "✌️",
        "ㄱ.박수": "👏",
        "ㄱ.예스": "👍",
        "ㄱ.노": "👎",
        "ㄱ.사고": "💡",
        "ㄱ.강아지": "🐶",
        "ㄱ.고양이": "🐱",
        "ㄱ.해": "☀️",
        "ㄱ.달빛": "🌙",
        "ㄱ.별": "⭐",
        "ㄱ.불": "🔥",
        "ㄱ.물": "💧",
        "ㄱ.나무": "🌳",
        "ㄱ.꽃": "🌸",
        "ㄱ.하트": "💖",
        "ㄱ.ㅎㅂ": "😊",
        "ㄱ.ㅅㅍ": "😢",
        "ㄱ.ㅎㄴ": "😡",
        "ㄱ.ㅅㄹ": "❤️",
        "ㄱ.ㄴㄹ": "😲",
        "ㄱ.ㅇㅅ": "😂",
        "ㄱ.ㅋㅅ": "😘",
        "ㄱ.ㅇㅇ": "😭",
        "ㄱ.ㄱㅂ": "😁",
        "ㄱ.ㄴㅁ": "😥",
        "ㄱ.ㄷㄹㅇ": "😱",
        "ㄱ.ㅍㄱ": "😴",
        "ㄱ.ㅇㅍ": "🤕",
        "ㄱ.ㅎㄹ": "😕",
        "ㄱ.ㄱㅅ": "💪",
        "ㄱ.ㅇㅋ": "👌",
        "ㄱ.ㅅㄹ": "✌️",
        "ㄱ.ㅂㅅ": "👏",
        "ㄱ.ㄴ": "👎",
        "ㄱ.ㅅㄱ": "💡",
        "ㄱ.ㄱㅇㅈ": "🐶",
        "ㄱ.ㄱㅇ": "🐱",
        "ㄱ.ㅎ": "☀️",
        "ㄱ.ㄷㅂ": "🌙",
        "ㄱ.ㅂ": "⭐",
        "ㄱ.ㅂ": "🔥",
        "ㄱ.ㅁ": "💧",
        "ㄱ.ㄴㅁ": "🌳",
        "ㄱ.ㄱ": "🌸",
        "ㄱ.ㅎㅌ": "💖"
    }

    # Streamlit 애플리케이션
    st.title("한글 이모지 채팅앱")

    # 사용자 입력
    user_input = st.text_input(" 'ㄱ.ㅎㅂ' 또는 'ㄱ.행복' 형식으로 메시지를 입력하세요:")

    # 감성 아이콘 변환 함수
    def replace_emoticons(text):
        for key, icon in emoticons.items():
            text = text.replace(key, icon)
        return text

    # 메시지 리스트
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 메시지 저장 및 출력
    if user_input:
        transformed_message = replace_emoticons(user_input)
        st.session_state.messages.append(transformed_message)
        st.write("변환된 메시지:")
        st.write(transformed_message)

    # 저장된 메시지 표시
    st.write("채팅 기록:")
    for message in st.session_state.messages:
        st.write(message)

    # 이모티콘 표 표시
    st.write("이모티콘 표:")
    emoticon_table = [{"초성": key, "이모티콘": emoticons[key]} for key in emoticons]
    st.table(emoticon_table)

# 앱 실행
if __name__ == "__main__":
    korean_emoji_chat()
