# LoLaeMon 🐱‍💻🔧

**LoLaeMon**은 LLM 기반 발명 시뮬레이션 게임입니다.  
현대 세계(2020년대)의 문제를 해결하기 위해, 존재하지 않는 '미래의 비밀 도구'를 발명하고 텍스트로 시뮬레이션합니다.

![도라에몽](https://upload.wikimedia.org/wikipedia/en/8/8d/Doraemon_character.png)

---

## 모델 & 기술

- **LLM**: GPT-4o-mini
- **임베딩 모델**: HuggingFace `paraphrase-multilingual-MiniLM-L12-v2`
- **Vector Store**: Chroma DB
- **데이터**: 한국어-영어 기술 번역 말뭉치 (AIHub)

---

## 게임 설명

1. **발명 게임**
   - 새로운 발명품 생성 (`new`)  
   - 기존 발명 업그레이드 (`upgrade`)  
   - 실패 가능성도 존재 (`failure`)

2. **코인 시스템**
   - 하루 100코인 지급
   - 발명품 생성, 업그레이드 시 코인 소모

3. **게임 상태 관리**
   - 현재 발명, 지난 발명 히스토리, 코인 상태 유지

4. **발명 규칙**
   - 기술 참고 자료 기반
   - 최소 2개 이상의 기술 결합
   - 창의적 발명품 이름 + 과학적 설명
   - 업그레이드 시 성능 개선 명확히 표시

---
