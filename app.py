import streamlit as st

st.set_page_config(page_title="เครื่องคิดเลข", page_icon="🧮", layout="centered")

st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
.block-container {padding: 1rem 1rem 0 1rem; max-width: 420px;}

div.stButton > button {
    width: 100%;
    height: 80px;
    font-size: 28px;
    font-weight: 400;
    border-radius: 16px;
    border: none;
    background: #333333;
    color: #ffffff;
    margin: 0;
}
div.stButton > button:hover  { background: #444444; border: none; }
div.stButton > button:focus  { border: none; box-shadow: none; }

.op   div.stButton > button { background: #FF9500; color: #ffffff; }
.op   div.stButton > button:hover { background: #FFB143; }

.gray div.stButton > button { background: #A5A5A5; color: #000000; }
.gray div.stButton > button:hover { background: #C0C0C0; }

.zero div.stButton > button { text-align: left; padding-left: 28px; }

div[data-testid="stHorizontalBlock"] { gap: 10px !important; }
.row-gap { margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

if "expr" not in st.session_state:
    st.session_state.expr = ""
if "display" not in st.session_state:
    st.session_state.display = "0"

def press(val):
    if val == "AC":
        st.session_state.expr = ""
        st.session_state.display = "0"
    elif val == "+/-":
        try:
            cur = float(st.session_state.expr)
            st.session_state.expr = str(-cur)
            st.session_state.display = st.session_state.expr
        except:
            pass
    elif val == "%":
        try:
            cur = float(st.session_state.expr)
            st.session_state.expr = str(cur / 100)
            st.session_state.display = st.session_state.expr
        except:
            pass
    elif val == "=":
        try:
            result = eval(st.session_state.expr)
            result = int(result) if isinstance(result, float) and result == int(result) else round(result, 8)
            st.session_state.display = str(result)
            st.session_state.expr = str(result)
        except:
            st.session_state.display = "Error"
            st.session_state.expr = ""
    else:
        if st.session_state.display == "0" and val != ".":
            st.session_state.expr = val
        else:
            st.session_state.expr += val
        st.session_state.display = st.session_state.expr

# display
st.markdown(f"""
<div style="background:#1c1c1c; border-radius:20px; padding:20px 24px 12px;
            text-align:right; margin-bottom:12px; min-height:110px;
            display:flex; flex-direction:column; justify-content:flex-end;">
  <div style="font-size:16px; color:#888; min-height:24px; word-break:break-all;">
    {st.session_state.expr if st.session_state.expr != st.session_state.display else ""}
  </div>
  <div style="font-size:52px; font-weight:300; color:#ffffff; word-break:break-all; line-height:1.1;">
    {st.session_state.display}
  </div>
</div>
""", unsafe_allow_html=True)

def btn_row(buttons):
    cols = st.columns([1] * len(buttons))
    for i, (label, val, style) in enumerate(buttons):
        with cols[i]:
            st.markdown(f'<div class="{style}">', unsafe_allow_html=True)
            if st.button(label, key=f"k_{label}_{val}"):
                press(val)
            st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="row-gap"></div>', unsafe_allow_html=True)

btn_row([("AC","AC","gray"), ("+/-","+/-","gray"), ("%","%","gray"), ("÷","/","op")])
btn_row([("7","7",""),       ("8","8",""),          ("9","9",""),    ("×","*","op")])
btn_row([("4","4",""),       ("5","5",""),          ("6","6",""),    ("−","-","op")])
btn_row([("1","1",""),       ("2","2",""),          ("3","3",""),    ("+","+","op")])

c1, c2, c3 = st.columns([2, 1, 1])
with c1:
    st.markdown('<div class="zero">', unsafe_allow_html=True)
    if st.button("0", key="k_0_zero"):
        press("0")
    st.markdown('</div>', unsafe_allow_html=True)
with c2:
    if st.button(".", key="k_dot"):
        press(".")
with c3:
    st.markdown('<div class="op">', unsafe_allow_html=True)
    if st.button("=", key="k_eq"):
        press("=")
    st.markdown('</div>', unsafe_allow_html=True)
