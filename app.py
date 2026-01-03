import streamlit as st
from firebase_config import db

st.title("Bible Reading Tracker")

# --- Login / Signup ---
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login / Sign Up"):
    user_ref = db.collection("users").document(email)
    if not user_ref.get().exists:
        # Sign up new user
        user_ref.set({
            "badges": [],
            "streak": 0,
            "progress": {}
        })
    st.session_state["email"] = email
    st.success(f"Logged in as {email}")
