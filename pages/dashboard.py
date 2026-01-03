import streamlit as st
from firebase_config import db
from utils import get_today_reading, calculate_streak, assign_badges
from datetime import date

st.header("Today's Reading")

user_email = st.session_state.get("email")
if not user_email:
    st.warning("Please log in from the main page.")
    st.stop()

# Example reading plan (replace with your 2-year plan)
reading_plan = {str(date.today()): [("Genesis", 1), ("Genesis", 2)]}
today_chapters = get_today_reading(reading_plan)

# Get user progress
user_ref = db.collection("users").document(user_email)
user_data = user_ref.get().to_dict()
progress = user_data.get("progress", {})

# Display checkboxes
for book, chapter in today_chapters:
    key = f"{book}_{chapter}"
    completed = progress.get(key, False)
    checked = st.checkbox(f"{book} {chapter}", value=completed)
    if checked != completed:
        progress[key] = checked
        user_ref.update({"progress": progress})

# Show streak & badges
st.write("Current streak:", calculate_streak(progress))
st.write("Badges:", assign_badges(progress))
