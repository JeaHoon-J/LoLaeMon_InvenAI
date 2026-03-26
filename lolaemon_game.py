# 


"""---
- 여기부터 코랩파일불러와서 다시실행

#### 코랩 데이터 파일 불러오기
"""

# colab 이후 재실행

import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma.vectorstores import Chroma

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")


os.listdir("C:/Users/Playdata/Desktop/SK_jaehoon/lolaemon_chroma_db")

import chromadb
client = chromadb.PersistentClient(path="C:/Users/Playdata/Desktop/SK_jaehoon/lolaemon_chroma_db/lolaemon_chroma_db")
print(client.list_collections())

collection = client.get_collection(name="lolaemon")

datas = collection.get(limit=2)
print(datas)

# sentence transformer test 결과
# keyword = '인공지능'
# query_embed = embedding_model.encode(keyword).tolist()
# results = collection.query(query_embeddings=query_embed, n_results=5)

# for result in results['metadatas'][0]:
#     print(result['origin tech text'])

"""#### Store"""

from langchain_chroma.vectorstores import Chroma

vector_store = Chroma(persist_directory="C:/Users/Playdata/Desktop/SK_jaehoon/lolaemon_chroma_db/lolaemon_chroma_db",
    embedding_function=embedding_model, collection_name = 'lolaemon')

retriever = vector_store.as_retriever(search_kwargs={"k": 5})
docs = retriever.invoke("인공지능 기술")
docs

"""### 발명 게임 함수 정의
- new (혁신적 발명), a_little_upgrade (부분 개선), failure (실패)
"""

from datetime import date
state = {
    'coins' : 100,
    'last_reset' : date.today(),
    'current_invetion':None,
    'history' : [], # 이전 발명 저장
    'last_result': ''
}

## 코인 리셋
def reset_daily_coins(state):
    state['coins'] = 100
    state['last_reset'] = date.today()
    state['history'] = []
    return '코인이 초기화되었습니다. 오늘의 코인은 100코인입니다.'

from datetime import date
state = {
    'coins' : 100,
    'last_reset' : date.today(),
    'current_invention':None,
    'history' : [], # 이전 발명 저장
    'last_result': ''
}

## 코인 리셋
def reset_daily_coins(state):
    state['coins'] = 100
    state['last_reset'] = date.today()
    state['history'] = []
    return '코인이 초기화되었습니다. 오늘의 코인은 100코인입니다.'
### 게임 이벤트 별 코인 차감
import random

def apply_game_logic(state, action):
    """
    action: 사용자가 'new' 또는 'upgrade' 요청
    결과: 이벤트별 랜덤 결정 + 코인 차감/보상
    """
    if action == 'new':
        cost = 50 # 혁신적 발명 적용
    elif action == 'upgrade':
        cost = 25
    else:
        cost=0

    if state['coins']<cost:
        return '코인 부족, 오늘은 이만!', state['coins']

    state['coins']-= cost
    event_type = random.choices(["new", "a_little_upgrade", "failure"], weights=[0.4, 0.4, 0.2], k=1)[0]

    return event_type, state['coins']

"""#### 프롬프트 작성 (미래에서 온 로라에몽)"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.9)

prompt = ChatPromptTemplate.from_messages([
    ("system", """
당신은 미래에서 온 발명가 ‘도라에몽’입니다.
당신의 임무는 사용자의 요청을 해결하기 위해, 기술 참고 자료를 기반으로 창의적이고 재미있고 만화스러운 새로운 발명품을 만드는 것입니다.
말투는 항상 진구를 대하듯 "~했어!", "~구!", "~이야!" 등 친근하고 활기찬 말투를 사용하세요.
"""),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", """
[현재 상태]
- 💰 남은 코인: {coins}
- 🎲 이번 결과: {last_result} # 이벤트 타입: new(혁신), a_little_upgrade(부분 개선), failure(실패)
- 🛠️ 직전 모델: {current_invention}
- 📜 히스토리: {history_list}

[사용자 고민]
"{question}"

[미래 기술 참고 자료]
{context}

[핵심 규칙 (반드시 지켜줘!)]
1. 반드시 "미래 기술 참고 자료"에 포함된 정보만 사용하세요. 자료에 없는 개념은 임의로 만들지 마세요.
2. 최소 2개 이상의 기술을 조합하여 새로운 발명품을 만드세요.
3. 단순 요약이나 재작성 금지! 반드시 새로운 이름을 가진 '발명품'이어야 합니다.
4. 과학적으로 말이 되도록 설명하세요 (완전한 판타지 금지).
5. 설명이 부족하면 추론으로 보완하되, 반드시 "(추론)"이라고 표시하세요.
6. '업그레이드' 요청을 했을 때 성공한다면, 기존 모델보다 성능이나 기능이 개선된 점을 명확히 보여줘야 해

---

[출력 형식] (이 구조를 절대 바꾸지 마!)

1. 발명품 이름
(창의적이고 기억에 남는 이름)

2. 한 줄 설명
(이 발명품이 무엇인지 한 문장으로 설명)

3. 작동 원리
- 사용된 기술: (기술 참고 자료에서 가져온 핵심 개념들, 꼭 참고된 {context}의 위치와 origin text의 요약도 알려줘)
- 결합 방식: (기술들이 어떻게 연결되는지 설명)
- 동작 과정: (전체 시스템이 어떻게 작동하는지 단계적으로 설명)

4. 사용 시나리오
(사용자가 실제로 사용하는 상황을 구체적으로 설명)

5. 왜 유용한지
(어떤 문제를 해결하는지 명확히 설명)

6. 이전 발명 요약
(new나 a_little_upgrade 결과일 경우에만 작성)

[중요]
- 기술 참고 자료에 없는 내용은 절대 사용하지 마세요.
- 창의적이고 재밌는 발상을 가득 넣어줘!
""")
])

"""### Chain 설정"""

chain = prompt | llm | StrOutputParser()
message_store = {}

def get_session_history(session_id: str):
    if session_id not in message_store:
        message_store[session_id] = ChatMessageHistory()
    return message_store[session_id]

lolaemon_chain = RunnableWithMessageHistory(chain, get_session_history, input_messages_key = 'question', history_messages_key = 'chat_history')

"""### 게임 함수 적용"""

def play_lolaemon(session_id: str, user_input: str):
    docs = retriever.invoke(user_input)
    context_text = '\n'.join([d.page_content for d in docs]) if docs else '참고할 기술 데이터가 없습니다.'

    is_upgrade = any(word in user_input for word in ['업그레이드', '개선', '더 좋게'])
    action = 'upgrade' if (is_upgrade and state['current_invention']) else 'new'

    event_type, current_coins = apply_game_logic(state, action)
    state['last_result'] = event_type

    if event_type == '코인 부족':
        return '💰 진구야! 코인이 부족해서 주머니를 열 수 없어. 내일 다시 오자!'
    if event_type == 'failure':
        return f"❌ (콰광!) 에구구... 발명에 실패했어. {current_coins}코인만 남았네."

    history_list = ", ".join(state['history'][-3:]) if state['history'] else "없음"

    # D. 실행
    response = lolaemon_chain.invoke(
        {
            "question": user_input,
            "context": context_text,
            "coins": current_coins,
            "last_result": event_type,
            "current_invention": state['current_invention'] or "없음",
            "history_list": history_list
        },
        config={"configurable": {"session_id": session_id}}
    )

    # E. 상태 업데이트
    if state['current_invention']:
        state['history'].append(state['current_invention'][:20] + "...") # 요약해서 저장
    state['current_invention'] = response

    return response

"""### LLM + Agent + Memory"""

print(play_lolaemon("user_01", "오늘은 시험을 보는날이야, 공부를 하나도 못했어 도와줘~"))

# 업그레이드
print(play_lolaemon("user_01", "방금 만들 것을 업그레이드 해줘!"))

print(f"💰 남은 코인: {state['coins']}")
print(f"🛠️ 최근 발명: {state['current_invention'][:30] if state['current_invention'] else '없음'}...")
print(f"📜 전체 기록 개수: {len(state['history'])}개")

print(f"💰 남은 코인: {state['coins']}")
print(f"🛠️ 최근 발명: {state['current_invention'][:30] if state['current_invention'] else '없음'}...")
print(f"📜 전체 기록 개수: {len(state['history'])}개")

msg = reset_daily_coins(state)
print(msg)

# 2. 초기화가 잘 되었는지 확인해볼까요?
print(f"현재 코인: {state['coins']}")
print(f"현재 발명: {state['current_invention']}")

