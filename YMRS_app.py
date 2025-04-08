# pip install streamlit

import streamlit as st

# YMRS 문항 및 선택지 데이터 구조 (11개 문항)
ymrs_mapping = [
    {
        "id": 1,
        "question_ko": "기분 고양",
        "question_en": "Elevated Mood",
        "description_ko": "",
        "description_en": "",
        "choices": [
            {
                "score": 0,
                "text_ko": "없음",
                "text_en": "Absent",
                "response_text_ko": "없음",
                "response_text_en": "Absent"
            },
            {
                "score": 1,
                "text_ko": "질문 시 약간 또는 가능성 있는 기분 고양이 나타남",
                "text_en": "Mildly or possibly increased on questioning",
                "response_text_ko": "질문 시 약간 또는 가능성 있는 기분 고양이 나타남",
                "response_text_en": "Mildly or possibly increased on questioning"
            },
            {
                "score": 2,
                "text_ko": "주관적으로 확실한 기분 상승이 있으며, 낙관적이고 자신감 있으며 명랑함. 내용에 적절함",
                "text_en": "Definite subjective elevation; optimistic, self-confident; cheerful; appropriate to content",
                "response_text_ko": "주관적으로 확실한 기분 상승이 있으며, 낙관적이고 자신감 있으며 명랑함. 내용에 적절함",
                "response_text_en": "Definite subjective elevation; optimistic, self-confident; cheerful; appropriate to content"
            },
            {
                "score": 3,
                "text_ko": "고양된 기분이나 내용에 부적절하며 유머스러움",
                "text_en": "Elevated; inappropriate to content; humorous",
                "response_text_ko": "고양된 기분이나 내용에 부적절하며 유머스러움",
                "response_text_en": "Elevated; inappropriate to content; humorous"
            },
            {
                "score": 4,
                "text_ko": "도취된 상태로, 부적절한 웃음 또는 노래를 함",
                "text_en": "Euphoric; inappropriate laughter; singing",
                "response_text_ko": "도취된 상태로, 부적절한 웃음 또는 노래를 함",
                "response_text_en": "Euphoric; inappropriate laughter; singing"
            }
        ]
    },
    {
        "id": 2,
        "question_ko": "정신운동 활동 및 에너지 증가",
        "question_en": "Increased Motor Activity-Energy",
        "description_ko": "",
        "description_en": "",
        "choices": [
            {
                "score": 0,
                "text_ko": "없음",
                "text_en": "Absent",
                "response_text_ko": "없음",
                "response_text_en": "Absent"
            },
            {
                "score": 1,
                "text_ko": "주관적으로 에너지가 증가했다고 느낌",
                "text_en": "Subjectively increased",
                "response_text_ko": "주관적으로 에너지가 증가했다고 느낌",
                "response_text_en": "Subjectively increased"
            },
            {
                "score": 2,
                "text_ko": "생기 있어 보이며, 몸짓이 증가함",
                "text_en": "Animated; gestures increased",
                "response_text_ko": "생기 있어 보이며, 몸짓이 증가함",
                "response_text_en": "Animated; gestures increased"
            },
            {
                "score": 3,
                "text_ko": "과도한 에너지; 때때로 과잉행동 보이며 안절부절못함 (진정 가능함)",
                "text_en": "Excessive energy; hyperactive at times; restless (can be calmed)",
                "response_text_ko": "과도한 에너지; 때때로 과잉행동 보이며 안절부절못함 (진정 가능함)",
                "response_text_en": "Excessive energy; hyperactive at times; restless (can be calmed)"
            },
            {
                "score": 4,
                "text_ko": "운동성 흥분 상태; 지속적인 과잉행동 (진정 불가능함)",
                "text_en": "Motor excitement; continuous hyperactivity (cannot be calmed)",
                "response_text_ko": "운동성 흥분 상태; 지속적인 과잉행동 (진정 불가능함)",
                "response_text_en": "Motor excitement; continuous hyperactivity (cannot be calmed)"
            }
        ]
    },
    {
        "id": 3,
        "question_ko": "성적 관심",
        "question_en": "Sexual Interest",
        "description_ko": "",
        "description_en": "",
        "choices": [
            {
                "score": 0,
                "text_ko": "정상 수준; 증가 없음",
                "text_en": "Normal; not increased",
                "response_text_ko": "정상 수준; 증가 없음",
                "response_text_en": "Normal; not increased"
            },
            {
                "score": 1,
                "text_ko": "약간 또는 가능성 있는 증가",
                "text_en": "Mildly or possibly increased",
                "response_text_ko": "약간 또는 가능성 있는 증가",
                "response_text_en": "Mildly or possibly increased"
            },
            {
                "score": 2,
                "text_ko": "질문 시 주관적으로 확실한 증가가 있음",
                "text_en": "Definite subjective increase on questioning",
                "response_text_ko": "질문 시 주관적으로 확실한 증가가 있음",
                "response_text_en": "Definite subjective increase on questioning"
            },
            {
                "score": 3,
                "text_ko": "자발적으로 성적인 내용을 이야기하거나, 성적인 문제를 자세히 설명하며, 스스로 과도한 성욕이 있다고 보고함",
                "text_en": "Spontaneous sexual content; elaborates on sexual matters; hypersexual by self-report",
                "response_text_ko": "자발적으로 성적인 내용을 이야기하거나, 성적인 문제를 자세히 설명하며, 스스로 과도한 성욕이 있다고 보고함",
                "response_text_en": "Spontaneous sexual content; elaborates on sexual matters; hypersexual by self-report"
            },
            {
                "score": 4,
                "text_ko": "노골적인 성적 행동을 보임 (다른 환자, 의료진 또는 면담자에게)",
                "text_en": "Overt sexual acts (toward patients, staff, or interviewer)",
                "response_text_ko": "노골적인 성적 행동을 보임 (다른 환자, 의료진 또는 면담자에게)",
                "response_text_en": "Overt sexual acts (toward patients, staff, or interviewer)"
            }
        ]
    },
    {
        "id": 4,
        "question_ko": "수면",
        "question_en": "Sleep",
        "description_ko": "",
        "description_en": "",
        "choices": [
            {
                "score": 0,
                "text_ko": "수면 감소가 없다고 보고함",
                "text_en": "Reports no decrease in sleep",
                "response_text_ko": "수면 감소가 없다고 보고함",
                "response_text_en": "Reports no decrease in sleep"
            },
            {
                "score": 1,
                "text_ko": "평소보다 최대 1시간 정도 적게 잠을 잠",
                "text_en": "Sleeping less than normal amount by up to one hour",
                "response_text_ko": "평소보다 최대 1시간 정도 적게 잠을 잠",
                "response_text_en": "Sleeping less than normal amount by up to one hour"
            },
            {
                "score": 2,
                "text_ko": "평소보다 1시간 이상 적게 잠",
                "text_en": "Sleeping less than normal by more than one hour",
                "response_text_ko": "평소보다 1시간 이상 적게 잠",
                "response_text_en": "Sleeping less than normal by more than one hour"
            },
            {
                "score": 3,
                "text_ko": "수면의 필요가 줄었다고 보고함",
                "text_en": "Reports decreased need for sleep",
                "response_text_ko": "수면의 필요가 줄었다고 보고함",
                "response_text_en": "Reports decreased need for sleep"
            },
            {
                "score": 4,
                "text_ko": "수면이 필요 없다고 부인함",
                "text_en": "Denies need for sleep",
                "response_text_ko": "수면이 필요 없다고 부인함",
                "response_text_en": "Denies need for sleep"
            }
        ]
    },
    {
        "id": 5,
        "question_ko": "과민성",
        "question_en": "Irritability",
        "description_ko": "",
        "description_en": "",
        "choices": [
            {
                "score": 0,
                "text_ko": "없음",
                "text_en": "Absent",
                "response_text_ko": "없음",
                "response_text_en": "Absent"
            },
            {
                "score": 2,
                "text_ko": "주관적으로 과민성이 증가했다고 느낌",
                "text_en": "Subjectively increased",
                "response_text_ko": "주관적으로 과민성이 증가했다고 느낌",
                "response_text_en": "Subjectively increased"
            },
            {
                "score": 4,
                "text_ko": "면담 중 때때로 과민한 모습을 보이며, 병동 내에서 최근 분노 또는 짜증을 보인 에피소드가 있음",
                "text_en": "Irritable at times during interview; recent episodes of anger or annoyance on ward",
                "response_text_ko": "면담 중 때때로 과민한 모습을 보이며, 병동 내에서 최근 분노 또는 짜증을 보인 에피소드가 있음",
                "response_text_en": "Irritable at times during interview; recent episodes of anger or annoyance on ward"
            },
            {
                "score": 6,
                "text_ko": "면담 내내 자주 과민한 모습을 보이며, 짧고 퉁명스러움",
                "text_en": "Frequently irritable during interview; short, curt throughout",
                "response_text_ko": "면담 내내 자주 과민한 모습을 보이며, 짧고 퉁명스러움",
                "response_text_en": "Frequently irritable during interview; short, curt throughout"
            },
            {
                "score": 8,
                "text_ko": "적대적이고 협조하지 않으며, 면담이 불가능함",
                "text_en": "Hostile, uncooperative; interview impossible",
                "response_text_ko": "적대적이고 협조하지 않으며, 면담이 불가능함",
                "response_text_en": "Hostile, uncooperative; interview impossible"
            }
        ]
    },
    {
        "id": 6,
        "question_ko": "언어 (속도 및 양)",
        "question_en": "Speech (Rate and Amount)",
        "description_ko": "",
        "description_en": "",
        "choices": [
            {
                "score": 0,
                "text_ko": "증가 없음",
                "text_en": "No increase",
                "response_text_ko": "증가 없음",
                "response_text_en": "No increase"
            },
            {
                "score": 2,
                "text_ko": "말이 많아졌다고 느낌",
                "text_en": "Feels talkative",
                "response_text_ko": "말이 많아졌다고 느낌",
                "response_text_en": "Feels talkative"
            },
            {
                "score": 4,
                "text_ko": "때때로 말의 속도나 양이 증가함, 장황하게 말함",
                "text_en": "Increased rate or amount at times, verbose at times",
                "response_text_ko": "때때로 말의 속도나 양이 증가함, 장황하게 말함",
                "response_text_en": "Increased rate or amount at times, verbose at times"
            },
            {
                "score": 6,
                "text_ko": "밀어붙이듯 말함; 지속적으로 말의 속도와 양이 증가하며, 중단시키기 어려움",
                "text_en": "Push; consistently increased rate and amount; difficult to interrupt",
                "response_text_ko": "밀어붙이듯 말함; 지속적으로 말의 속도와 양이 증가하며, 중단시키기 어려움",
                "response_text_en": "Push; consistently increased rate and amount; difficult to interrupt"
            },
            {
                "score": 8,
                "text_ko": "압박적으로 말함; 끊임없이 이어지는 말로 중단 불가능함",
                "text_en": "Pressured; uninterruptible, continuous speech",
                "response_text_ko": "압박적으로 말함; 끊임없이 이어지는 말로 중단 불가능함",
                "response_text_en": "Pressured; uninterruptible, continuous speech"
            }
        ]
    },
    {
        "id": 7,
        "question_ko": "언어-사고 장애",
        "question_en": "Language-Thought Disorder",
        "description_ko": "",
        "description_en": "",
        "choices": [
            {
                "score": 0,
                "text_ko": "없음",
                "text_en": "Absent",
                "response_text_ko": "없음",
                "response_text_en": "Absent"
            },
            {
                "score": 1,
                "text_ko": "우회적인 표현, 약한 주의 산만, 생각이 빠름",
                "text_en": "Circumstantial; mild distractibility; quick thoughts",
                "response_text_ko": "우회적인 표현, 약한 주의 산만, 생각이 빠름",
                "response_text_en": "Circumstantial; mild distractibility; quick thoughts"
            },
            {
                "score": 2,
                "text_ko": "주의 산만, 사고의 목표를 잃고 자주 주제를 바꿈; 사고가 경주하듯 흐름",
                "text_en": "Distractible, loses goal of thought; changes topics frequently; racing thoughts",
                "response_text_ko": "주의 산만, 사고의 목표를 잃고 자주 주제를 바꿈; 사고가 경주하듯 흐름",
                "response_text_en": "Distractible, loses goal of thought; changes topics frequently; racing thoughts"
            },
            {
                "score": 3,
                "text_ko": "사고의 비약, 본론에서 벗어남, 따라가기 어려움; 운율 맞추기, 메아리 말하기",
                "text_en": "Flight of ideas; tangentiality; difficult to follow; rhyming, echolalia",
                "response_text_ko": "사고의 비약, 본론에서 벗어남, 따라가기 어려움; 운율 맞추기, 메아리 말하기",
                "response_text_en": "Flight of ideas; tangentiality; difficult to follow; rhyming, echolalia"
            },
            {
                "score": 4,
                "text_ko": "사고가 일관되지 않으며, 의사소통이 불가능함",
                "text_en": "Incoherent; communication impossible",
                "response_text_ko": "사고가 일관되지 않으며, 의사소통이 불가능함",
                "response_text_en": "Incoherent; communication impossible"
            }
        ]
    },
    {
        "id": 8,
        "question_ko": "사고 내용",
        "question_en": "Content",
        "description_ko": "",
        "description_en": "",
        "choices": [
            {
                "score": 0,
                "text_ko": "정상",
                "text_en": "Normal",
                "response_text_ko": "정상",
                "response_text_en": "Normal"
            },
            {
                "score": 2,
                "text_ko": "의심스러운 계획이나 새로운 관심사 있음",
                "text_en": "Questionable plans, new interests",
                "response_text_ko": "의심스러운 계획이나 새로운 관심사 있음",
                "response_text_en": "Questionable plans, new interests"
            },
            {
                "score": 4,
                "text_ko": "특별한 프로젝트 수행 중; 과도하게 종교적임",
                "text_en": "Special project(s); hyper-religious",
                "response_text_ko": "특별한 프로젝트 수행 중; 과도하게 종교적임",
                "response_text_en": "Special project(s); hyper-religious"
            },
            {
                "score": 6,
                "text_ko": "과대망상 또는 편집적 사고; 관계 망상 있음",
                "text_en": "Grandiose or paranoid ideas; ideas of reference",
                "response_text_ko": "과대망상 또는 편집적 사고; 관계 망상 있음",
                "response_text_en": "Grandiose or paranoid ideas; ideas of reference"
            },
            {
                "score": 8,
                "text_ko": "망상 또는 환각을 경험함",
                "text_en": "Delusions; hallucinations",
                "response_text_ko": "망상 또는 환각을 경험함",
                "response_text_en": "Delusions; hallucinations"
            }
        ]
    },
    {
        "id": 9,
        "question_ko": "파괴적-공격적 행동",
        "question_en": "Disruptive-Aggressive Behavior",
        "description_ko": "",
        "description_en": "",
        "choices": [
            {
                "score": 0,
                "text_ko": "없음, 협조적임",
                "text_en": "Absent, cooperative",
                "response_text_ko": "없음, 협조적임",
                "response_text_en": "Absent, cooperative"
            },
            {
                "score": 2,
                "text_ko": "빈정거림; 때때로 목소리가 크고, 방어적임",
                "text_en": "Sarcastic; loud at times, guarded",
                "response_text_ko": "빈정거림; 때때로 목소리가 크고, 방어적임",
                "response_text_en": "Sarcastic; loud at times, guarded"
            },
            {
                "score": 4,
                "text_ko": "요구가 많으며, 병동에서 위협적인 언행을 보임",
                "text_en": "Demanding; threats on ward",
                "response_text_ko": "요구가 많으며, 병동에서 위협적인 언행을 보임",
                "response_text_en": "Demanding; threats on ward"
            },
            {
                "score": 6,
                "text_ko": "면담자를 위협하거나 고함침; 면담이 어려움",
                "text_en": "Threatens interviewer; shouting; interview difficult",
                "response_text_ko": "면담자를 위협하거나 고함침; 면담이 어려움",
                "response_text_en": "Threatens interviewer; shouting; interview difficult"
            },
            {
                "score": 8,
                "text_ko": "폭력적이며, 물건을 파괴하거나 공격적임; 면담이 불가능함",
                "text_en": "Assaultive; destructive; interview impossible",
                "response_text_ko": "폭력적이며, 물건을 파괴하거나 공격적임; 면담이 불가능함",
                "response_text_en": "Assaultive; destructive; interview impossible"
            }
        ]
    },
    {
        "id": 10,
        "question_ko": "외모",
        "question_en": "Appearance",
        "description_ko": "",
        "description_en": "",
        "choices": [
            {
                "score": 0,
                "text_ko": "복장과 단정한 외모가 적절함",
                "text_en": "Appropriate dress and grooming",
                "response_text_ko": "복장과 단정한 외모가 적절함",
                "response_text_en": "Appropriate dress and grooming"
            },
            {
                "score": 1,
                "text_ko": "최소한의 단정치 못함",
                "text_en": "Minimally unkempt",
                "response_text_ko": "최소한의 단정치 못함",
                "response_text_en": "Minimally unkempt"
            },
            {
                "score": 2,
                "text_ko": "위생 상태가 좋지 않으며, 다소 단정하지 않고, 과도하게 차려입음",
                "text_en": "Poorly groomed; moderately disheveled; overdressed",
                "response_text_ko": "위생 상태가 좋지 않으며, 다소 단정하지 않고, 과도하게 차려입음",
                "response_text_en": "Poorly groomed; moderately disheveled; overdressed"
            },
            {
                "score": 3,
                "text_ko": "단정하지 않으며, 일부만 옷을 입었거나, 과장된 화장을 함",
                "text_en": "Disheveled; partly clothed; garish make-up",
                "response_text_ko": "단정하지 않으며, 일부만 옷을 입었거나, 과장된 화장을 함",
                "response_text_en": "Disheveled; partly clothed; garish make-up"
            },
            {
                "score": 4,
                "text_ko": "매우 단정하지 않으며, 장식물이 많고, 기이한 복장을 함",
                "text_en": "Completely unkempt; decorated; bizarre garb",
                "response_text_ko": "매우 단정하지 않으며, 장식물이 많고, 기이한 복장을 함",
                "response_text_en": "Completely unkempt; decorated; bizarre garb"
            }
        ]
    },
    {
        "id": 11,
        "question_ko": "병식",
        "question_en": "Insight",
        "description_ko": "",
        "description_en": "",
        "choices": [
            {
                "score": 0,
                "text_ko": "병이 있다는 것을 인정하며, 치료의 필요성에 동의함",
                "text_en": "Present; admits illness; agrees with need for treatment",
                "response_text_ko": "병이 있다는 것을 인정하며, 치료의 필요성에 동의함",
                "response_text_en": "Present; admits illness; agrees with need for treatment"
            },
            {
                "score": 1,
                "text_ko": "병이 있을 가능성 있음",
                "text_en": "Possibly ill",
                "response_text_ko": "병이 있을 가능성 있음",
                "response_text_en": "Possibly ill"
            },
            {
                "score": 2,
                "text_ko": "행동의 변화를 인정하지만 병이 있다고는 부인함",
                "text_en": "Admits behavior change, but denies illness",
                "response_text_ko": "행동의 변화를 인정하지만 병이 있다고는 부인함",
                "response_text_en": "Admits behavior change, but denies illness"
            },
            {
                "score": 3,
                "text_ko": "행동 변화의 가능성은 인정하지만 병은 아니라고 주장함",
                "text_en": "Admits possible change in behavior, but denies illness",
                "response_text_ko": "행동 변화의 가능성은 인정하지만 병은 아니라고 주장함",
                "response_text_en": "Admits possible change in behavior, but denies illness"
            },
            {
                "score": 4,
                "text_ko": "어떤 행동 변화도 없었다고 주장함",
                "text_en": "Denies any behavior change",
                "response_text_ko": "어떤 행동 변화도 없었다고 주장함",
                "response_text_en": "Denies any behavior change"
            }
        ]
    }
]

# 앱 UI 및 결과 처리를 위한 함수 정의

def render_form():
    st.header("YMRS 평가 (Young Mania Rating Scale)")
    st.write("아래의 각 문항에 대해 해당하는 선택지를 드롭다운에서 선택해 주세요.")
    
    # 각 질문마다 드롭다운 생성 (UI는 한국어, 선택지에는 한국어 텍스트 출력)
    for question in ymrs_mapping:
        key_name = f"question_{question['id']}"
        st.selectbox(
            label=question["question_ko"],
            options=question["choices"],
            format_func=lambda option: option["text_ko"],
            key=key_name
        )

    # 제출 버튼 클릭 시 st.session_state 값 변경
    if st.button("제출"):
        st.session_state.submitted = True

def show_result():
    st.header("YMRS Results")
    total_score = 0
    result_lines = []
    
    # 각 문항의 결과 산출 (영문 문항 제목, 선택한 드롭다운의 영어 응답 및 선택지 점수)
    for question in ymrs_mapping:
        key_name = f"question_{question['id']}"
        selected_option = st.session_state.get(key_name, None)
        if selected_option is None:
            continue
        score = selected_option["score"]
        total_score += score
        line = f"{question['id']}. {question['question_en']}\n   ({score}) {selected_option['text_en']}"
        result_lines.append(line)
        
    # 임상적 해석 (참고: Young et al., 1978)
    if total_score < 12:
        interpretation = "No significant manic symptoms."
    elif total_score < 20:
        interpretation = "Mild manic symptoms."
    elif total_score < 30:
        interpretation = "Moderate manic symptoms."
    else:
        interpretation = "Severe manic symptoms."
        
    result_text = ("[Young Mania Rating Scale] Results\n\n" + "\n\n".join(result_lines) + 
                   f"\n\nTotal Score: {total_score}\nClinical Interpretation: {interpretation}\n" +
                   "\nReference: Young RC, Biggs JT, Ziegler VE, Meyer DA. A Rating Scale for Mania: Reliability, Validity and Sensitivity. "
                   "Br J Psychiatry. 1978;133:429-435. (https://doi.org/10.1192/bjp.133.5.429)")
    
    st.code(result_text, language="text")
    
    # 돌아가기 버튼 클릭 시 제출 상태 초기화하여 결과 화면에서 입력 화면으로 전환
    if st.button("돌아가기"):
        st.session_state.submitted = False

def main():
    # st.session_state 초기화: 'submitted' 키가 없으면 생성
    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    # 제출 여부에 따라 form 또는 결과 화면 출력
    if st.session_state.submitted:
        show_result()
    else:
        render_form()

    # (개발 시 검증용) 콘솔에 ymrs_mapping 출력
    print(ymrs_mapping)

if __name__ == "__main__":
    main()
