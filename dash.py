import streamlit as st
from database import Database

# Initialize database
db = Database()

# Streamlit UI
st.set_page_config(page_title="AI Skill Selector", layout="wide")

st.title("🤖 AI-Powered Dynamic Skill Selector")
st.markdown("**Monitor and enhance AI skill performance using real-time analytics.**")

# Sidebar navigation
menu = st.sidebar.radio("Navigation", ["🏆 Leaderboard", "📊 Skill Performance", "➕ Add Skill Data"])

# Leaderboard View
if menu == "🏆 Leaderboard":
    st.subheader("🏆 Top Performing Skills")
    leaderboard = db.get_leaderboard()

    if leaderboard:
        st.table(leaderboard)
    else:
        st.info("No skill data available yet. Add some!")

# Skill Performance View
elif menu == "📊 Skill Performance":
    st.subheader("📊 Skill Performance Metrics")
    skills = db.get_all_skills()

    if skills:
        st.table(skills)
    else:
        st.warning("No data found. Add performance metrics!")

# Add Skill Data View
elif menu == "➕ Add Skill Data":
    st.subheader("➕ Update Skill Performance")

    skill_name = st.text_input("Skill Name", placeholder="Enter skill name (e.g., NLP_Model_1)")
    accuracy = st.number_input("Accuracy Score (0-1)", min_value=0.0, max_value=1.0, step=0.01)

    if st.button("Submit"):
        if skill_name and (0.0 <= accuracy <= 1.0):
            db.update_performance(skill_name, accuracy)
            st.success(f"Updated {skill_name} with accuracy {accuracy}")
        else:
            st.error("Invalid input. Please enter valid values.")

# Close database connection when Streamlit stops
st.sidebar.button("🔄 Refresh Data", on_click=lambda: st.experimental_rerun())
