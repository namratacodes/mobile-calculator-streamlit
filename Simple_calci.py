import streamlit as st

st.set_page_config(page_title="Mobile Calculator", page_icon="🧮", layout="centered")

if "history" not in st.session_state:
    st.session_state.history = []

theme = st.sidebar.toggle("🌙 Dark Mode", value=True)

if theme:
    bg = "#0f172a"
    card = "#1e293b"
    text = "white"
    button = "#38bdf8"
else:
    bg = "#f8fafc"
    card = "#ffffff"
    text = "black"
    button = "#2563eb"

st.markdown(f"""
    <style>
    .stApp {{
        background-color: {bg};
        color: {text};
    }}
    .main-card {{
        background-color: {card};
        padding: 30px;
        border-radius: 25px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        max-width: 380px;
        margin: auto;
    }}
    .title {{
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: {button};
    }}
    .result {{
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: #22c55e;
        margin-top: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("📌 Calculator Menu")

st.sidebar.subheader("🕘 History")
for item in st.session_state.history[-5:]:
    st.sidebar.write(item)

st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown('<div class="title">🧮 Mobile Calculator</div>', unsafe_allow_html=True)

num1 = st.number_input("Enter First Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)

operation = st.selectbox(
    "Choose Operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

col1, col2 = st.columns(2)

with col1:
    calculate = st.button("Calculate 🚀")

with col2:
    clear = st.button("Clear ❌")

if calculate:
    if operation == "Addition":
        result = num1 + num2
        expression = f"{num1} + {num2} = {result}"
    elif operation == "Subtraction":
        result = num1 - num2
        expression = f"{num1} - {num2} = {result}"
    elif operation == "Multiplication":
        result = num1 * num2
        expression = f"{num1} × {num2} = {result}"
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            expression = f"{num1} ÷ {num2} = {result}"
        else:
            result = "Cannot divide by zero"
            expression = result

    st.session_state.history.append(expression)

    st.markdown(f'<div class="result">Result: {result}</div>', unsafe_allow_html=True)

if clear:
    st.session_state.history = []
    st.success("History Cleared")

st.markdown('</div>', unsafe_allow_html=True)


st.markdown("---")
st.markdown("""
<div style='text-align:center; padding:10px; font-size:15px; color:#94a3b8;'>
✨ Made by : <b>Namrata</b>
</div>
""", unsafe_allow_html=True)