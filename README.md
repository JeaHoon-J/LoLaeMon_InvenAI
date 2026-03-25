# LoLaeMon_InvenAI 🐱‍💻🔧

**미래 발명 시뮬레이션 + 신기술 개발 AI 프로젝트**  

**LoLaeMon_InvenAI**(도라에몽 + LLM,로라에몽)는 **사용자의 요청을 바탕으로 창의적인 발명품과 신기술을 만들어내는 AI 실험실**입니다.  
단순 게임이 아니라, **LLM + 다양한 기술 정보 RAG 구조 기반의 실제 AI 개발 경험**을 제공하며, Embedding, Vector DB, 프롬프트 설계, 실시간 인터랙션까지 모두 포함합니다.

---

## 🔹 핵심 목표

1. **창의적 발명 생성**  
   - 사용자의 고민이나 요청을 바탕으로, 미래 발명가 ‘도라에몽 + LLM = LoLaeMon (로라에몽)’이 미래 발명을 설계  
   - 최소 2개 이상의 기술을 결합하여 **신기술 발명**  

2. **신기술 개발 실습**  
   - AIHub 기술 문서를 기반으로 실제 기술 데이터 활용  
   - RAG(Retrieval-Augmented Generation) 구조 적용 → 현실적인 발명 구현  

3. **AI 개발 학습 포인트**  
   - LLM 프롬프트 설계와 컨텍스트 활용  
   - HuggingFace Embedding + Chroma Vector Store 기반 검색  
   - 실시간 발명, 업그레이드, 코인 기반 게임 인터랙션 구현  

---


## 🔹 구현 프로세스

1. LLM을 활용한 **창의적 발명 시뮬레이션** 구현  
2. 한국어-영어 기술 문서 데이터셋(AIHub)을 기반으로 **RAG(Retrieval-Augmented Generation)** 구조 실습  
3. HuggingFace 임베딩 모델과 **Chroma DB**를 활용한 **Vector Store** 구축 및 Lag 형성  
4. 체계적인 **프롬프트 설계**를 통한 LLM 제어 및 게임적 인터랙션 구현  
5. Streamlit UI를 통해 실시간 발명과 코인, 히스토리 관리 기능 제공  

---

## 🔹 기술 스택

| 영역 | 사용 기술 / 라이브러리 |
|------|--------------------|
| LLM | OpenAI GPT-4o-mini (`langchain_openai`) |
| Embedding | HuggingFace `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` |
| Vector DB | Chroma (Persistent Vector Store) |
| Retrieval | LangChain `retriever` 기반 RAG 구조 |
| UI | Streamlit |
| Data | 한국어-영어 기술 번역 말뭉치 (AIHub) |
| 환경 | Python 3.10+, dotenv, pandas, tqdm |

---

## 🔹 구조 및 개발 과정

1. **데이터 전처리**
   - AIHub 기술 문서셋에서 **도메인 + 서브도메인 + 기술 설명**을 결합하여 document 생성
   - 결측치 처리 및 샘플링 후, LLM 검색용 corpus 구축

2. **Vector Store 구축**
   - HuggingFace 임베딩 모델을 통해 각 기술 문서를 벡터화
   - Chroma DB에 저장하여 RAG 구조에서 빠른 유사도 검색 가능
   - 검색 결과는 LLM 입력으로 제공되어, **참고 기술 기반 발명 생성**에 활용

3. **LLM + 프롬프트 설계**
   - 미래 발명가 ‘도라에몽’ 역할을 하는 시스템 프롬프트
   - 핵심 규칙:
     - 최소 2개 이상의 기술 결합
     - 기술 자료에 없는 내용 사용 금지
     - 업그레이드 시 성능/기능 개선 반영
   - 사용자 입력 + 검색된 기술 컨텍스트를 결합하여 LLM 호출

4. **게임 로직 & 상태 관리**
   - 코인 기반 발명/업그레이드 시스템
   - 실패 확률, 부분 개선 이벤트 반영
   - 직전 발명, 발명 히스토리, 남은 코인 상태 유지

5. **Streamlit UI**
   - 배경 이미지 고정, 도라에몽 캐릭터 표시
   - 사용자 발명 요청 입력, 업그레이드, 코인 초기화 버튼
   - 실시간 발명 결과 출력 및 사이드바 상태 관리

---

