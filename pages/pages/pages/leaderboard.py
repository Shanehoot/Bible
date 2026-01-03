import streamlit as st
from firebase_config import db

st.header("Leaderboard")

users = db.collection("users").stream()
leaderboard = []

for user in users:
    data = user.to_dict()
    streak = data.get("streak", 0)
    leaderboard.append((user.id, streak))

# Sort by streak descending
leaderboard.sort(key=lambda x: x[1], reverse=True)

for i, (user, streak) in enumerate(leaderboard, 1):
    st.write(f"{i}. {user} — {streak} days streak")
