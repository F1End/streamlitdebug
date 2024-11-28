"""Simple application to demonstrate issue
Run main.py to load this file locally."""

import streamlit as st
from datetime import datetime
from time import sleep

sessions = {"show_hint": False}
for state, value in sessions.items():
    if state not in st.session_state.keys():
        st.session_state[state] = value

# Some widget on top, to make this feel more like a real application
st.text_input("Type your answer here:")

# Toggling session_state for "show_hint"
if st.button("Show hint"):
    if st.session_state.show_hint:
        print("Hint hidden!")
        st.session_state.show_hint = False
    else:
        print("Hint revealed!")
        st.session_state.show_hint = True

# draws widget only if session_state is True:
if st.session_state.show_hint:
    st.write("Trust yourself!")

display = st.empty()
print(display)

# workaround: move next row "fake_display" from comment to code
# fake_display = st.empty()
while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    display.metric("Current time", current_time)
    sleep(1)
