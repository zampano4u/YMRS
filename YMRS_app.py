import streamlit as st

questions = [
    {
        "id": 1,
        "ko_title": "고양된 기분",
        "en_title": "Elevated Mood",
        "options": [
            ("없음", 0),
            ("질문 시 약간 상승된 기분", 1),
            ("주관적 고양감, 낙관적, 자신감 있음, 명랑함", 2),
            ("부적절하게 들뜸, 유머", 3),
            ("도취감, 부적절한 웃음, 노래 부름", 4)
        ]
    },
    {
        "id": 2,
        "ko_title": "운동 활동 증가 – 에너지",
        "en_title": "Increased Motor Activity – Energy",
        "options": [
            ("없음", 0),
            ("주관적으로 증가됨", 1),
            ("동작 활발, 제스처 증가", 2),
            ("과도한 에너지, 진정 가능", 3),
            ("지속적 과잉활동, 진정 불가", 4)
        ]
    },
    {
        "id": 3,
        "ko_title": "성적 관심",
        "en_title": "Sexual Interest",
        "options": [
            ("정상, 증가 없음", 0),
            ("약간 증가된 듯함", 1),
            ("질문 시 증가 확인", 2),
            ("자발적 성적 표현, 성적 묘사", 3),
            ("공공연한 성적 행동", 4)
        ]
    },
    {
        "id": 4,
        "ko_title": "수면",
        "en_title": "Sleep",
        "options": [
            ("수면 감소 없음", 0),
            ("평소보다 1시간 이내 감소", 1),
            ("1시간 이상 감소", 2),
            ("수면욕구 감소", 3),
            ("수면이 필요 없다고 함", 4)
        ]
    },
    {
        "id": 5,
        "ko_title": "과민성",
        "en_title": "Irritability",
        "options": [
            ("없음", 0),
            ("주관적으로 과민함", 2),
            ("면담 중 가끔 과민, 최근 분노", 4),
            ("지속적 과민, 퉁명스러움", 6),
            ("적대적, 비협조적, 면담 불가", 8)
        ]
    },
    {
        "id": 6,
        "ko_title": "언어 (속도와 양)",
        "en_title": "Speech (Rate and Amount)",
        "options": [
            ("증가 없음", 0),
            ("말이 많다고 느낌", 2),
            ("때때로 말 많고 빠름", 4),
            ("지속적 과도한 말, 끼어들기 어려움", 6),
            ("압박된 말, 끊을 수 없음", 8)
        ]
    },
    {
        "id": 7,
        "ko_title": "사고장애",
        "en_title": "Language – Thought Disorder",
        "options": [
            ("없음", 0),
            ("우회적, 산만, 생각 빠름", 1),
            ("산만, 주제 이탈, 사고 분산", 2),
            ("사고비약, 연상, 빗나감", 3),
            ("의사소통 불가", 4)
        ]
    },
    {
        "id": 8,
        "ko_title": "사고 내용",
        "en_title": "Content",
        "options": [
            ("정상", 0),
            ("의심스러운 계획, 새로운 관심", 2),
            ("특별 프로젝트, 과도한 종교심", 4),
            ("과대망상, 관계망상", 6),
            ("망상, 환각", 8)
        ]
    },
    {
        "id": 9,
        "ko_title": "파괴적 / 공격적 행동",
        "en_title": "Disruptive–Aggressive Behavior",
        "options": [
            ("없음, 협조적", 0),
            ("비꼬는 말투, 큰소리", 2),
            ("위협, 요구 많음", 4),
            ("면담자 위협, 고함", 6),
            ("공격적, 파괴적", 8)
        ]
    },
    {
        "id": 10,
        "ko_title": "외모",
        "en_title": "Appearance",
        "options": [
            ("적절한 복장, 단정함", 0),
            ("약간 흐트러짐", 1),
            ("단정하지 않음, 과도하게 꾸밈", 2),
            ("난잡, 과도한 화장", 3),
            ("완전히 흐트러짐, 기이한 복장", 4)
        ]
    },
    {
        "id": 11,
        "ko_title": "병식",
        "en_title": "Insight",
        "options": [
            ("있음, 병 인정, 치료 동의", 0),
            ("병일 수 있음", 1),
            ("행동 변화 인정, 병 부정", 2),
            ("변화 인정하나 병 부정", 3),
            ("어떤 변화도 부정", 4)
        ]
    }
]

st.title("Young Mania Rating Scale (YMRS)")

user_selections = {}
all_answered = True

for q in questions:
    st.markdown(f"**{q['id']}. {q['ko_title']}**")
    labels = [f"{text} ({score})" for text, score in q["options"]]
    choice = st.selectbox("선택하세요", labels, key=q["id"])
    user_selections[q["id"]] = choice
    if not choice:
        all_answered = False

if st.button("Show Result"):
    if all_answered:
        scores = []
        responses = []

        for q in questions:
            choice = user_selections[q["id"]]
            score = int(choice.split("(")[-1].strip(")"))
            scores.append(score)
            responses.append(f"{q['id']}. {q['en_title']} - {choice}")

        total_score = sum(scores)

        if total_score <= 12:
            interpretation = "No or minimal manic symptoms"
        elif 13 <= total_score <= 19:
            interpretation = "Mild mania"
        elif 20 <= total_score <= 25:
            interpretation = "Moderate mania"
        else:
            interpretation = "Severe mania"

        output_lines = ["**Young Mania Rating Scale (YMRS)**", ""]
        output_lines.extend(responses)
        output_lines.append("")
        output_lines.append(f"Total Score: {total_score}")
        output_lines.append(f"Clinical Interpretation: {interpretation}")

        final_output = "\n".join(output_lines)

        # ✅ 출력만 표시, 복사 버튼 없음
        st.code(final_output, language="markdown")
    else:
        st.warning("모든 문항에 응답한 후 결과를 확인할 수 있습니다.")
