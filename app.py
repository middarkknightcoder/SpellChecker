from main import SpellCheckerApp
import streamlit as st


# Heading Part
st.header("👀 Spell Checker 🔍" ,divider="rainbow")
st.header("")

# Input Part
text = st.text_area("Paste or Type Your Text Which You Want to Correct...." ,placeholder="Paste or Type Text Here .....")


# Processing and Result Part
if st.button("Correction"):
    correct = SpellCheckerApp().SpellCorrection(text)
    st.header("")
    st.subheader("Correct Spell",divider="blue")
    st.write(correct.capitalize())
    

    
    