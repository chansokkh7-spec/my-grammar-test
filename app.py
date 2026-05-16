import streamlit as st

# ទិន្នន័យសំណួរពិតប្រាកដស្រង់ចេញពីសៀវភៅ PDF របស់អ្នក
BOOK_DATABASE = {
    "Elementary level (កម្រិតដំបូង)": {
        "Elementary #1: Speaking already": [
            {"q": "Q1: Can you hear what he is .......?", "options": ["(a) saying", "(b) speaking", "(c) telling", "(d) talking"], "answer": "(a) saying"},
            {"q": "Q2: She hasn't come home .......", "options": ["(a) still", "(b) already", "(c) yet", "(d) till"], "answer": "(c) yet"},
            {"q": "Q3: I ....... TV yesterday evening.", "options": ["(a) saw", "(b) looked", "(c) viewed", "(d) watched"], "answer": "(d) watched"},
            {"q": "Q4: We live ....... the city centre.", "options": ["(a) near", "(b) next", "(c) by", "(d) nearby"], "answer": "(a) near"},
            {"q": "Q5: She looks ....... a famous film star.", "options": ["(a) as", "(b) like", "(c) similar", "(d) same"], "answer": "(b) like"},
            {"q": "Q6: This television gives you the ....... news.", "options": ["(a) last", "(b) latest", "(c) least", "(d) later"], "answer": "(b) latest"},
            {"q": "Q7: I only ....... one mistake in last night's test.", "options": ["(a) made", "(b) done", "(c) did", "(d) make"], "answer": "(a) made"},
            {"q": "Q8: I want you to tell me the ....... truth.", "options": ["(a) all", "(b) exact", "(c) real", "(d) whole"], "answer": "(d) whole"}
        ]
    },
    "Intermediate level (កម្រិតមធ្យម)": {
        "Intermediate #4: Do, make, get, take": [
            {"q": "Q1: You must decide and ....... up your mind.", "options": ["(a) do", "(b) get", "(c) make", "(d) take"], "answer": "(c) make"},
            {"q": "Q2: What time do you ....... up in the morning?", "options": ["(a) do", "(b) get", "(c) make", "(d) take"], "answer": "(b) get"}
        ]
    },
    "Advanced level (កម្រិតខ្ពស់)": {
        "Advanced #1: Advanced culinary art": [
            {"q": "A1: Eastern restaurants often have a way of whisking you away to a far off land of belly dancers, exotic spices and ....... drink.", "options": ["(a) internal", "(b) inverted", "(c) intoxicating", "(d) inner"], "answer": "(c) intoxicating"},
            {"q": "A2: Thai cuisine is one of the most romantic of the Asian cuisines as it still ....... an element of mystery and exoticism.", "options": ["(a) remains", "(b) retains", "(c) reminds", "(d) returns"], "answer": "(b) retains"},
            {"q": "A3: Modern Asian restaurants in Jakarta have an ....... history.", "options": ["(a) extended", "(b) external", "(c) extracted", "(d) exuded"], "answer": "(a) extended"}
        ]
    }
}

st.set_page_config(page_title="English Grammar Test System", page_icon="📚", layout="centered")

st.title("📝 ប្រព័ន្ធធ្វើតេស្តវេយ្យាករណ៍អង់គ្លេសស្វ័យប្រវត្ត")
st.write("📖 វិញ្ញាសាទាំងអស់ត្រូវបានដកស្រង់ចេញពីសៀវភៅ **English Grammar (Tests)**")

level = st.sidebar.selectbox("📂 ជ្រើសរើសកម្រិតសិក្សា (Select Level):", list(BOOK_DATABASE.keys()))
topics = list(BOOK_DATABASE[level].keys())
topic = st.sidebar.selectbox("📖 ជ្រើសរើសមេរៀន (Select Topic):", topics)

st.subheader(f"🎯 វិញ្ញាសា: {topic}")
st.divider()

questions = BOOK_DATABASE[level][topic]

with st.form(key="quiz_form"):
    user_answers = {}
    for i, q_item in enumerate(questions):
        st.markdown(f"**{q_item['q']}**")
        user_answers[i] = st.radio(
            f"ចម្លើយទី {i+1}:", 
            q_item["options"], 
            key=f"q_{i}",
            index=None,
            label_visibility="collapsed"
        )
        st.write("")

    submit_button = st.form_submit_button(label="📤 ផ្ញើចម្លើយ និងពិនិត្យលទ្ធផល (Submit)")

if submit_button:
    score = 0
    total_questions = len(questions)
    
    st.divider()
    st.subheader("📊 លទ្ធផលនៃការធ្វើតេស្ត (Test Result)")
    
    for i, q_item in enumerate(questions):
        selected = user_answers[i]
        correct_ans = q_item["answer"]
        
        if selected is not None:
            if selected.strip() == correct_ans.strip():
                score += 1
                st.success(f"✅ សំណួរទី {i+1}: ត្រឹមត្រូវ! អ្នកបានជ្រើសរើស {selected}")
            else:
                st.error(f"❌ សំណួរទី {i+1}: ខុសហើយ! ចម្លើយត្រឹមត្រូវគឺ៖ {correct_ans}")
        else:
            st.warning(f"⚠️ សំណួរទី {i+1}: អ្នកមិនបានឆ្លើយទេ។ ចម្លើយត្រឹមត្រូវគឺ៖ {correct_ans}")
            
    percentage = (score / total_questions) * 100
    st.markdown(f"### 🏆 ពិន្ទុរបស់អ្នកសរុបគឺ: **{score}/{total_questions}** ({percentage:.2f}%)")
    
    if percentage >= 80:
        st.balloons()
        st.success("🎉 អស្ចារ្យណាស់! អ្នកធ្វើបានល្អខ្លាំងណាស់។")
