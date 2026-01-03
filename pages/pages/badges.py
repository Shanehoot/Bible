import streamlit as st
from firebase_config import db

st.header("Your Badges")

user_email = st.session_state.get("email")
if not user_email:
    st.warning("Please log in first.")
    st.stop()

user_doc = db.collection("users").document(user_email).get()
badges = user_doc.to_dict().get("badges", [])

if badges:
    for badge in badges:
        st.write(f"🏆 {badge}")
else:
    st.write("No badges earned yet. Keep reading!")
