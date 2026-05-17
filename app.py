import streamlit as st

st.set_page_config(page_title="เครื่องคิดเลข", page_icon="🧮", layout="centered")

st.markdown("""
<style>
div.stButton > button {
    width: 100%;
    height: 70px;
    font-size: 24px;
    border-radius: 12px;
    border: 1px solid #ddd;
    background: #ffffff;
    color: #1a1a1a;
}
div.stButton > button:hover { background: #f0f0f0; }
</style>
""", unsafe_allow_html=True)

if "expr" not in st.session_state:
    st.session_state.expr = ""
if "display" not in st.session_state:
    st.session_state.display = "0"

def press(val):
    if val == "C":
        st.session_state.expr = ""
        st.session_state.display = "0"
    elif val == "=":
        try:
            result = eval(st.session_state.expr)
            result = int(result) if result == int(result) else round(result, 10)
            st.session_state.display = str(result)
            st.session_state.expr = str(result)
        except:
            st.session_state.display = "Error"
            st.session_state.expr = ""
    else:
        st.session_state.expr += str(val)
        st.session_state.display = st.session_state.expr

# display
st.markdown(f"""
<div style="background:#f5f5f0;border-radius:12px;padding:16px 20px;
            text-align:right;margin-bottom:16px;border:1px solid #ddd">
  <div style="font-size:36px;font-weight:500;color:#1a1a1a;
              word-break:break-all">{st.session_state.display}</div>
</div>
""", unsafe_allow_html=True)

# buttons
rows = [
    ["C", "%", "//", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "", "="],
]

labels = {"*": "×", "/": "÷", "//": "÷÷", "-": "−", "+": "+", "=": "=",
          "C": "C", "%": "%", ".": ".", "0": "0", "": ""}

for row in rows:
    cols = st.columns(4)
    for i, val in enumerate(row):
        with cols[i]:
            if val == "":
                st.empty()
            else:
                if st.button(labels.get(val, val), key=f"btn_{val}_{row}"):
                    press(val)
