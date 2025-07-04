import streamlit as st

st.set_page_config(page_title="Maryam Attiq's Calculator", layout="centered")
st.title("Maryam Attiq's Calculator")

if "expression" not in st.session_state:
    st.session_state.expression = ""

def press(val):
    # Convert words to symbols
    if val == "Add":
        val = "+"
    elif val == "Subtract":
        val = "-"
    elif val == "Multiply":
        val = "*"
    elif val == "Divide":
        val = "/"
    st.session_state.expression += val

def clear():
    st.session_state.expression = ""

def evaluate():
    try:
        st.session_state.expression = str(eval(st.session_state.expression))
    except:
        st.session_state.expression = "Error"

# Show input
st.text_input("Expression", value=st.session_state.expression, disabled=True)

# Button layout using words
buttons = [
    ["7", "8", "9", "Divide"],
    ["4", "5", "6", "Multiply"],
    ["1", "2", "3", "Subtract"],
    ["0", ".", "=", "Add"]
]

for row in buttons:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        if btn == "=":
            cols[i].button("=", on_click=evaluate)
        else:
            cols[i].button(btn, on_click=press, args=(btn,))

st.button("Clear", on_click=clear)

