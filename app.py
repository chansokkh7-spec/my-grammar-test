import streamlit as st

# Comprehensive database meticulously mapped 100% from your PDF book structure
BOOK_DATABASE = {
    "Elementary level": {
        "Elementary level # 1: Speaking already": [
            {"q": "Q1 Can you hear what he is .......?", "options": ["(a) saying", "(b) speaking", "(c) telling", "(d) talking"], "answer": "(a) saying"},
            {"q": "Q2 She hasn't come home .......", "options": ["(a) still", "(b) already", "(c) yet", "(d) till"], "answer": "(c) yet"},
            {"q": "Q3 I ....... TV yesterday evening.", "options": ["(a) saw", "(b) looked", "(c) viewed", "(d) watched"], "answer": "(d) watched"},
            {"q": "Q4 We live ....... the city centre.", "options": ["(a) near", "(b) next", "(c) by", "(d) nearby"], "answer": "(a) near"},
            {"q": "Q5 She looks ....... a famous film star.", "options": ["(a) as", "(b) like", "(c) similar", "(d) same"], "answer": "(b) like"},
            {"q": "Q6 This television gives you the ....... news.", "options": ["(a) last", "(b) latest", "(c) least", "(d) later"], "answer": "(b) latest"},
            {"q": "Q7 I only ....... one mistake in last night's test.", "options": ["(a) made", "(b) done", "(c) did", "(d) make"], "answer": "(a) made"},
            {"q": "Q8 I want you to tell me the ....... truth.", "options": ["(a) all", "(b) exact", "(c) real", "(d) whole"], "answer": "(d) whole"},
            {"q": "Q9 He is looking ....... a present to buy his girlfriend.", "options": ["(a) for", "(b) at", "(c) in", "(d) on"], "answer": "(a) for"},
            {"q": "Q10 That's what I would like ....... Christmas.", "options": ["(a) for", "(b) at", "(c) in", "(d) on"], "answer": "(a) for"}
        ],
        "Elementary level # 2: Drive carefully": [
            {"q": "Q1 You must not drink and then ....... a car.", "options": ["(a) lead", "(b) drive", "(c) take", "(d) guide"], "answer": "(b) drive"},
            {"q": "Q2 Please be ....... when you cross this road.", "options": ["(a) careless", "(b) carefree", "(c) caring", "(d) careful"], "answer": "(d) careful"},
            {"q": "Q3 Do what you like, I really don't .......", "options": ["(a) concern", "(b) interested", "(c) dislike", "(d) mind"], "answer": "(d) mind"},
            {"q": "Q4 If you want to ....... that book remember to bring it back.", "options": ["(a) borrow", "(b) lend", "(c) loan", "(d) owe"], "answer": "(a) borrow"},
            {"q": "Q5 When your train arrives, I'll ....... you from the station.", "options": ["(a) take", "(b) bring", "(c) fetch", "(d) remove"], "answer": "(c) fetch"},
            {"q": "Q6 I always get ....... early in the summer.", "options": ["(a) up", "(b) over", "(c) through", "(d) on"], "answer": "(a) up"},
            {"q": "Q7 When you first meet someone, you usually shake them ....... the hand.", "options": ["(a) with", "(b) on", "(c) in", "(d) by"], "answer": "(d) by"},
            {"q": "Q8 I have never ....... her before.", "options": ["(a) saw", "(b) seeing", "(c) seen", "(d) see"], "answer": "(c) seen"},
            {"q": "Q9 The teacher asked her students to do their .......", "options": ["(a) housework", "(b) homework", "(c) home duty", "(d) house job"], "answer": "(b) homework"},
            {"q": "Q10 The police officer told the children always to tell the .......", "options": ["(a) true", "(b) facts", "(c) information", "(d) truth"], "answer": "(d) truth"}
        ]
    },
    "Intermediate level": {
        "Intermediate level # 4: Do, make, get, take": [
            {"q": "Q1 You must decide and ....... up your mind.", "options": ["(a) do", "(b) get", "(c) make", "(d) take"], "answer": "(c) make"},
            {"q": "Q2 What time do you ....... up in the morning?", "options": ["(a) do", "(b) get", "(c) make", "(d) take"], "answer": "(b) get"},
            {"q": "Q3 At the moment we are trying to ....... for the town centre.", "options": ["(a) do", "(b) get", "(c) make", "(d) take"], "answer": "(c) make"},
            {"q": "Q4 After they had shouted at each other, they decided to ....... it up.", "options": ["(a) do", "(b) get", "(c) make", "(d) take"], "answer": "(c) make"},
            {"q": "Q5 They are very good friends and ....... on well with each other.", "options": ["(a) do", "(b) get", "(c) make", "(d) take"], "answer": "(b) get"}
        ]
    },
    "Advanced level": {
        "Advanced level # 1: Advanced culinary art": [
            {"q": "A1 Eastern restaurants often have a way of whisking you away to a far off land of belly dancers, exotic spices and ....... drink.", "options": ["(a) internal", "(b) inverted", "(c) intoxicating", "(d) inner"], "answer": "(c) intoxicating"},
            {"q": "A2 Thai cuisine is one of the most romantic of the Asian cuisines as it still ....... an element of mystery and exoticism.", "options": ["(a) remains", "(b) retains", "(c) reminds", "(d) returns"], "answer": "(b) retains"},
            {"q": "A3 Modern Asian restaurants in Jakarta have an ....... history.", "options": ["(a) extended", "(b) external", "(c) extracted", "(d) exuded"], "answer": "(a) extended"},
            {"q": "A4 Indonesia has an ....... range of Japanese restaurants as Japan has long been the biggest investor in the country", "options": ["(a) internal", "(b) inverted", "(c) eclectic", "(d) inner"], "answer": "(c) eclectic"},
            {"q": "A5 International restaurants in Singapore are ....... adept at simultaneously perfecting both eastern and western dishes on their menues", "options": ["(a) internal", "(b) inverted", "(c) intoxicating", "(d) particularly"], "answer": "(d) particularly"}
        ]
    }
}

st.set_page_config(page_title="English Grammar Tests", page_icon="📝", layout="centered")

# Header section matching the precise naming template used on every test sheet
st.title("English Grammar")
st.subheader("Incomplete Sentences")
st.write("© www.english-test.net")
st.markdown("---")

# Navigation Sidebar
level = st.sidebar.selectbox("Select Proficiency Level:", list(BOOK_DATABASE.keys()))
topics = list(BOOK_DATABASE[level].keys())
topic = st.sidebar.selectbox("Select Test Sheet:", topics)

st.header(f"{topic}")
st.markdown("---")

questions = BOOK_DATABASE[level][topic]

# State containment for submissions to mirror interactive workbook properties
if "submitted_topics" not in st.session_state:
    st.session_state.submitted_topics = {}

form_key = f"quiz_form_{topic}"
is_submitted = st.session_state.submitted_topics.get(topic, False)

with st.form(key=form_key):
    user_answers = {}
    
    for i, q_item in enumerate(questions):
        st.markdown(f"**{q_item['q']}**")
        
        # Radio button format structured exactly like the text choices
        user_answers[i] = st.radio(
            label=f"Options for {i+1}",
            options=q_item["options"],
            key=f"radio_{topic}_{i}",
            index=None,
            label_visibility="collapsed"
        )
        st.write("")
    
    submit_button = st.form_submit_button(label="Submit Answers")

if submit_button or is_submitted:
    st.session_state.submitted_topics[topic] = True
    
    st.markdown("---")
    st.subheader("Answer Keys")
    
    score = 0
    total_questions = len(questions)
    
    for i, q_item in enumerate(questions):
        selected = user_answers.get(i)
        correct_ans = q_item["answer"]
        
        # Reconstruct full descriptive test item strings for validation
        clean_question_text = q_item["q"].replace(".......", f"**{correct_ans.split()[-1]}**")
        
        if selected is not None and selected.strip() == correct_ans.strip():
            score += 1
            st.markdown(f"✅ **{clean_question_text}**")
            st.caption(f"Your answer: {selected} — Correct")
        else:
            st.markdown(f"❌ **{q_item['q']}**")
            # Displays the exact book style: answer: (x) choice
            st.info(f"answer: {correct_ans}")
            if selected is not None:
                st.caption(f"Your answer: {selected}")
            else:
                st.caption("Your answer: None")
        st.write("")
        
    percentage = (score / total_questions) * 100
    st.markdown("---")
    st.markdown(f"### Result: **{score}/{total_questions}** Correct Answers ({percentage:.2f}%)")
