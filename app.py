

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta, time
st.set_page_config(page_title="Loop Habit Tracker", layout="wide")

# --- Comprehensive Color Scheme CSS ---
st.markdown('''
    <style>
    :root {
        /* Global Palette */
        --primary-blue: #3A7BD5;
        --accent-orange: #F3A12F;
        --neutral-dark: #2D373B;
        --neutral-medium: #748F90;
        --neutral-light: #F8F9FA;
        --neutral-white: #FFFFFF;
        --success-green: #28A745;
        --warning-amber: #FFC107;
        --error-red: #DC3545;
        
        /* Component-specific colors */
        --nav-bg: #1E2024;
        --sidebar-bg: #FBEBBD;
        --info-bg: #D7EAFB;
        --border-color: #ACCCC4;
        --hover-blue: #2B63A3;
        --chart-grid: #ECEFF1;
        --slider-track: #FFE7B5;
        
        /* Status message backgrounds */
        --success-bg-light: #D4EDDA;
        --success-text-dark: #155724;
        --warning-bg-light: #FFF3CD;
        --warning-text-dark: #856404;
        --error-bg-light: #F8D7DA;
        --error-text-dark: #721C24;
    }
    
    /* Global App Background */
    html, body, .main, .block-container {
        background-color: var(--neutral-light) !important;
        color: var(--neutral-dark) !important;
    }
    .stApp {
        background-color: var(--neutral-light) !important;
    }
    
    /* Top Navigation Bar (if applicable) */
    .stApp > header {
        background-color: var(--nav-bg) !important;
        border-bottom: 1px solid var(--neutral-medium) !important;
    }
    .stApp > header * {
        color: var(--neutral-white) !important;
    }
    
    /* Sidebar Styling */
    .stSidebar {
        background-color: var(--sidebar-bg) !important;
    }
    .stSidebar .stRadio > label {
        color: var(--neutral-dark) !important;
        font-weight: 600 !important;
    }
    .stSidebar .stRadio > div[data-testid="radio-group"] label[data-baseweb="radio"] {
        background-color: transparent !important;
    }
    .stSidebar .stRadio > div[data-testid="radio-group"] label[data-baseweb="radio"][aria-checked="true"]::before {
        background-color: var(--accent-orange) !important;
    }
    .stSidebar h1 {
        color: var(--neutral-white) !important;
        font-weight: 600 !important;
    }
    
    /* Headings and Section Titles */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
        color: var(--neutral-dark) !important;
        font-weight: 700 !important;
    }
    
    /* Informational Callouts */
    .stInfo {
        background-color: var(--info-bg) !important;
        color: var(--neutral-dark) !important;
        border: 1px solid var(--primary-blue) !important;
        border-radius: 6px !important;
    }
    
    /* Form Inputs */
    .stTextInput > div > input, .stTextArea textarea {
        background-color: var(--neutral-white) !important;
        color: var(--neutral-dark) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 5px !important;
    }
    .stTextInput > div > input::placeholder, .stTextArea textarea::placeholder {
        color: var(--neutral-medium) !important;
    }
    .stTextInput > div > input:focus, .stTextArea textarea:focus {
        border-color: var(--primary-blue) !important;
        box-shadow: 0 0 0 2px rgba(58, 123, 213, 0.2) !important;
    }
    
    /* Select Boxes / Dropdowns */
    .stSelectbox > div > div {
        background-color: var(--neutral-dark) !important;
        color: var(--neutral-white) !important;
        border: none !important;
        border-radius: 5px !important;
    }
    .stSelectbox > div > div:hover {
        background-color: var(--primary-blue) !important;
    }
    
    /* Date and Time Inputs */
    .stDateInput > div > input {
        background-color: var(--neutral-white) !important;
        color: var(--neutral-dark) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 5px !important;
    }
    .stTimeInput > div > input {
        background-color: var(--neutral-dark) !important;
        color: var(--neutral-white) !important;
        border: none !important;
        border-radius: 5px !important;
    }
    .stTimeInput > div > input:hover, .stTimeInput > div > input:focus {
        background-color: var(--primary-blue) !important;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: var(--primary-blue) !important;
        color: var(--neutral-white) !important;
        border: none !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        transition: background-color 0.2s ease !important;
    }
    .stButton > button:hover {
        background-color: var(--hover-blue) !important;
        color: var(--neutral-white) !important;
    }
    .stButton > button:disabled {
        background-color: var(--neutral-medium) !important;
        color: rgba(255, 255, 255, 0.6) !important;
    }
    
    /* Data Tables */
    .stDataFrame, .stTable {
        background-color: var(--neutral-white) !important;
        border-radius: 8px !important;
        border: 1px solid var(--border-color) !important;
        box-shadow: 0 2px 8px rgba(172, 204, 196, 0.3) !important;
    }
    
    /* Charts */
    .stPlotlyChart, .stAltairChart {
        background-color: var(--neutral-white) !important;
        border-radius: 8px !important;
    }
    
    /* Sliders (Settings Page) */
    .stSlider > div > div {
        background-color: var(--slider-track) !important;
    }
    .stSlider > div > div > div {
        background-color: var(--accent-orange) !important;
    }
    .stSlider > div > div > div > div {
        background-color: var(--accent-orange) !important;
        border: 2px solid var(--neutral-white) !important;
    }
    .stSlider .st-bb {
        color: var(--neutral-dark) !important;
    }
    
    /* Toggle Switches */
    .stCheckbox > label {
        color: var(--neutral-dark) !important;
    }
    .stCheckbox > label > div {
        background-color: var(--neutral-white) !important;
        border: 1px solid var(--border-color) !important;
    }
    .stCheckbox > label > div[aria-checked="true"] {
        background-color: var(--primary-blue) !important;
        border-color: var(--primary-blue) !important;
    }
    
    /* Status Messages */
    .stSuccess {
        background-color: var(--success-bg-light) !important;
        color: var(--success-text-dark) !important;
        border: 1px solid var(--success-green) !important;
        border-radius: 6px !important;
    }
    .stWarning {
        background-color: var(--warning-bg-light) !important;
        color: var(--warning-text-dark) !important;
        border: 1px solid var(--warning-amber) !important;
        border-radius: 6px !important;
    }
    .stError {
        background-color: var(--error-bg-light) !important;
        color: var(--error-text-dark) !important;
        border: 1px solid var(--error-red) !important;
        border-radius: 6px !important;
    }
    
    /* Habit Grid Icons Styling */
    .habit-grid-icon {
        font-size: 18px !important;
        font-weight: bold !important;
        text-align: center !important;
    }
    
    /* WCAG AA Contrast Compliance */
    .st-emotion-cache-1v0mbdj {
        color: var(--neutral-dark) !important;
    }
    </style>
''', unsafe_allow_html=True)


st.sidebar.title("Loop Habit Tracker")
page = st.sidebar.radio("Go to", ["Dashboard", "Add Habit", "Statistics", "Settings"])

# --- Data Model ---
def init_state():
	if "habits" not in st.session_state:
		st.session_state.habits = []
	if "completions" not in st.session_state:
		st.session_state.completions = {}  # {(habit_idx, date): True/False}

def today():
	return datetime.now().date()

def get_last_n_days(n=7):
	return [today() - timedelta(days=i) for i in range(n-1, -1, -1)]

def is_scheduled(habit, day):
	# Daily
	if habit["frequency_type"] == "Daily":
		return day >= habit["start_date"]
	# Every N days
	elif habit["frequency_type"] == "Every N days":
		delta = (day - habit["start_date"]).days
		return delta >= 0 and delta % habit["frequency_value"] == 0
	return False

def get_completion(habit_idx, day):
	return st.session_state.completions.get((habit_idx, day), None)

def set_completion(habit_idx, day, value):
	st.session_state.completions[(habit_idx, day)] = value


def get_streaks(habit_idx, days):
	# Current streak: consecutive ✔️ from today backwards
	current = 0
	for d in reversed(days):
		if is_scheduled(st.session_state.habits[habit_idx], d) and get_completion(habit_idx, d):
			current += 1
		elif is_scheduled(st.session_state.habits[habit_idx], d):
			break
	# Longest streak: max consecutive ✔️
	longest = 0
	streak = 0
	for d in days:
		if is_scheduled(st.session_state.habits[habit_idx], d) and get_completion(habit_idx, d):
			streak += 1
			longest = max(longest, streak)
		elif is_scheduled(st.session_state.habits[habit_idx], d):
			streak = 0
	return current, longest

def get_last_missed(habit_idx, days):
	for d in reversed(days):
		if is_scheduled(st.session_state.habits[habit_idx], d) and get_completion(habit_idx, d) is False:
			return d
	return None

def get_stats(habit_idx, days):
	scheduled = [d for d in days if is_scheduled(st.session_state.habits[habit_idx], d)]
	completed = [d for d in scheduled if get_completion(habit_idx, d)]
	missed = [d for d in scheduled if get_completion(habit_idx, d) is False]
	if scheduled:
		rate = len(completed) / len(scheduled)
	else:
		rate = 0
	return len(completed), len(missed), rate, len(scheduled)

# --- UI Pages ---

def dashboard():
    st.title("Habit Dashboard")
    days = get_last_n_days(7)
    day_labels = [d.strftime("%a %d") for d in days]
    if not st.session_state.habits:
        st.info("No habits yet. Add one!")
        return
    
    # Create a styled table header
    st.markdown("### 📊 Your Habit Progress")
    
    # Table header
    cols = st.columns([3] + [1]*7)
    cols[0].markdown("**Habit**")
    for i, label in enumerate(day_labels):
        cols[i+1].markdown(f"**{label}**")
    
    st.markdown("---")
    
    # Table rows
    for idx, habit in enumerate(st.session_state.habits):
        cols = st.columns([3] + [1]*7)
        
        # Habit name with color and prompt
        habit_info = f"""
        <div style='padding: 8px; border-left: 4px solid {habit['color']}; background: white; border-radius: 4px; margin: 2px 0;'>
            <span style='color: {habit['color']}; font-weight: bold; font-size: 14px;'>{habit['name']}</span>
        """
        if habit.get('prompt'):
            habit_info += f"<br><span style='font-size: 12px; color: #748F90; font-style: italic;'>{habit['prompt']}</span>"
        habit_info += "</div>"
        
        cols[0].markdown(habit_info, unsafe_allow_html=True)
        
        # Daily status icons
        for j, day in enumerate(days):
            if is_scheduled(habit, day):
                val = get_completion(idx, day)
                if day == today():
                    if val is None:
                        if cols[j+1].button("⭕", key=f"mark_{idx}_{day}", help="Click to mark as done"):
                            set_completion(idx, day, True)
                            st.rerun()
                    elif val:
                        cols[j+1].markdown('<div class="habit-grid-icon" style="color: #28A745;">✔️</div>', unsafe_allow_html=True)
                    else:
                        cols[j+1].markdown('<div class="habit-grid-icon" style="color: #DC3545;">✖️</div>', unsafe_allow_html=True)
                else:
                    if val is None:
                        if day < today():
                            cols[j+1].markdown('<div class="habit-grid-icon" style="color: #DC3545;">✖️</div>', unsafe_allow_html=True)
                        else:
                            cols[j+1].markdown('<div class="habit-grid-icon" style="color: #3A7BD5;">⭕</div>', unsafe_allow_html=True)
                    elif val:
                        cols[j+1].markdown('<div class="habit-grid-icon" style="color: #28A745;">✔️</div>', unsafe_allow_html=True)
                    else:
                        cols[j+1].markdown('<div class="habit-grid-icon" style="color: #DC3545;">✖️</div>', unsafe_allow_html=True)
            else:
                cols[j+1].markdown('<div class="habit-grid-icon" style="color: #748F90;">❓</div>', unsafe_allow_html=True)
        
        # Add some spacing between habit rows
        if idx < len(st.session_state.habits) - 1:
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

def add_habit():
    st.title("➕ Add New Habit")
    st.markdown("Create a new habit to track your daily progress.")
    
    with st.form("add_habit_form"):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            name = st.text_input("Habit name", max_chars=40, placeholder="e.g., Exercise, Read, Meditate")
            prompt = st.text_input("Prompt/question (optional)", placeholder="e.g., Did you exercise today?")
            notes = st.text_area("Notes (optional)", placeholder="Any additional notes about this habit...")
        
        with col2:
            color = st.color_picker("Choose habit color", "#3A7BD5")
            st.markdown("**Frequency**")
            freq_type = st.selectbox("", ["Daily", "Every N days"], label_visibility="collapsed")
            
            freq_val = 1
            n_days = None
            if freq_type == "Every N days":
                n_days = st.number_input("Every how many days?", min_value=2, max_value=30, value=2, step=1)
                freq_val = n_days
        
        st.markdown("---")
        
        col3, col4 = st.columns(2)
        with col3:
            reminder = st.time_input("⏰ Reminder time", value=time(8,0), step=60)
        with col4:
            start_date = st.date_input("📅 Start date", value=today())
        
        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("🎯 Add Habit", use_container_width=True)
        
        if submitted and name:
            st.session_state.habits.append({
                "name": name,
                "prompt": prompt,
                "notes": notes,
                "color": color,
                "frequency_type": freq_type,
                "frequency_value": freq_val,
                "reminder": reminder,
                "start_date": start_date,
            })
            st.success(f"🎉 Successfully added habit: **{name}**")
            st.balloons()
        elif submitted and not name:
            st.error("❌ Please enter a habit name.")


def statistics():
    st.title("📊 Statistics & Visualizations")
    st.markdown("Analyze your habit tracking progress and trends.")
    
    if not st.session_state.habits:
        st.info("🚀 No habits yet. Add one to see beautiful statistics!")
        return
    
    days = get_last_n_days(30)
    
    # Summary table with enhanced styling
    st.markdown("### 📈 Habit Summary (Last 30 Days)")
    data = []
    for idx, habit in enumerate(st.session_state.habits):
        current, longest = get_streaks(idx, days)
        completed, missed, rate, scheduled = get_stats(idx, days)
        last_missed = get_last_missed(idx, days)
        last_missed_str = last_missed.strftime('%Y-%m-%d') if last_missed else '—'
        data.append({
            "🎯 Habit": habit["name"],
            "🔥 Current Streak": current,
            "🏆 Longest Streak": longest,
            "✅ Success Rate": f"{int(rate*100)}%",
            "❌ Missed Days": missed,
            "📅 Scheduled Days": scheduled,
            "🎉 Completions": completed,
            "⏰ Last Missed": last_missed_str
        })
    
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Charts section
    st.markdown("---")
    
    # Daily completion trend
    st.markdown("### 📉 Daily Completions Trend")
    all_completions = []
    for d in days:
        count = 0
        for idx, habit in enumerate(st.session_state.habits):
            if is_scheduled(habit, d) and get_completion(idx, d):
                count += 1
        all_completions.append(count)
    
    chart_df = pd.DataFrame({
        "Date": days, 
        "Completions": all_completions
    })
    st.line_chart(chart_df.set_index("Date"), use_container_width=True)
    
    # Per-habit completions
    st.markdown("### 📊 Completions by Habit")
    bar_data = {}
    for idx, habit in enumerate(st.session_state.habits):
        completed_count = get_stats(idx, days)[0]
        bar_data[habit["name"]] = completed_count
    
    bar_df = pd.DataFrame.from_dict(bar_data, orient='index', columns=["Completions"])
    st.bar_chart(bar_df, use_container_width=True)
    
    # Calendar heatmap
    st.markdown("### 🗓️ Activity Heatmap")
    st.markdown("*Visual representation of your daily habit completion activity*")
    
    import numpy as np
    import altair as alt
    
    heatmap_data = []
    for d in days:
        count = 0
        for idx, habit in enumerate(st.session_state.habits):
            if is_scheduled(habit, d) and get_completion(idx, d):
                count += 1
        heatmap_data.append({
            "date": d, 
            "count": count, 
            "dow": d.weekday(), 
            "week": (d - days[0]).days // 7
        })
    
    heatmap_df = pd.DataFrame(heatmap_data)
    
    chart = alt.Chart(heatmap_df).mark_rect().encode(
        x=alt.X('dow:O', 
                title='Day of Week', 
                axis=alt.Axis(labels=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])),
        y=alt.Y('week:O', title='Week'),
        color=alt.Color('count:Q', 
                       scale=alt.Scale(scheme='blues', range=['#F8F9FA', '#3A7BD5']), 
                       legend=alt.Legend(title="Completions")),
        tooltip=[
            alt.Tooltip('date:T', title='Date'),
            alt.Tooltip('count:Q', title='Completions')
        ]
    ).properties(
        width=400, 
        height=150,
        title="Habit Completion Heatmap"
    )
    
    st.altair_chart(chart, use_container_width=True)
    
    # Key insights
    st.markdown("---")
    st.markdown("### 💡 Key Insights")
    
    if data:
        best_habit = max(data, key=lambda x: float(x["✅ Success Rate"].strip('%')))
        total_completions = sum([d["🎉 Completions"] for d in data])
        avg_success_rate = sum([float(d["✅ Success Rate"].strip('%')) for d in data]) / len(data)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("🏆 Best Performing Habit", 
                     best_habit["🎯 Habit"], 
                     f"{best_habit['✅ Success Rate']} success rate")
        
        with col2:
            st.metric("🎯 Total Completions", 
                     total_completions,
                     "in the last 30 days")
        
        with col3:
            st.metric("📊 Average Success Rate", 
                     f"{avg_success_rate:.1f}%",
                     "across all habits")

def settings():
    st.title("⚙️ Settings")
    st.markdown("Customize your Loop Habit Tracker experience.")
    
    st.markdown("### Interface")
    
    # Create styled toggle sections
    with st.container():
        st.toggle("Toggle with short press", 
                 help="Put checkmarks with a single tap instead of press-and-hold. More convenient, but might cause accidental toggles.")
        
        st.toggle("Extend day a few hours past midnight", 
                 help="Wait until 3:00 AM to show a new day. Useful if you typically go to sleep after midnight. Requires app restart.")
        
        st.toggle("Enable skip days", 
                 help="Toggle twice to add a skip instead of a checkmark. Skips keep your score unchanged and don't break your streak.")
        
        st.toggle("Show question marks for missing data", 
                 help="Differentiate days without data from actual lapses. To enter a lapse, toggle twice.")
        
        st.toggle("Reverse order of days", 
                 help="Show days in reverse order on the main screen.")
        
        st.toggle("Use pure black in dark theme", 
                 help="Replaces gray backgrounds with pure black in dark theme. Reduces battery usage in phones with AMOLED display.")
    
    st.markdown("---")
    
    st.markdown("### Widget Appearance")
    opacity = st.slider("Widget opacity", 
                       min_value=0, max_value=100, value=100, 
                       help="Makes widgets more transparent or more opaque in your home screen.")
    
    st.markdown(f"**Current opacity: {opacity}%**")
    
    # Data management section
    st.markdown("---")
    st.markdown("### Data Management")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📤 Export Data", use_container_width=True):
            st.info("Export functionality coming soon!")
    
    with col2:
        if st.button("📥 Import Data", use_container_width=True):
            st.info("Import functionality coming soon!")
    
    # About section
    st.markdown("---")
    st.markdown("### About")
    st.markdown("""
    **Loop Habit Tracker Web Version**  
    Built with ❤️ using Streamlit  
    
    Features:
    - ✅ Daily habit tracking
    - 📊 Progress visualization  
    - 🎯 Custom scheduling (daily/every N days)
    - 📈 Statistics and insights
    - 🎨 Beautiful, accessible design
    """)
    
    if st.button("🌟 Give Feedback"):
        st.success("Thank you for using Loop Habit Tracker!")# --- Main ---
init_state()
if page == "Dashboard":
	dashboard()
elif page == "Add Habit":
	add_habit()
elif page == "Statistics":
	statistics()
elif page == "Settings":
	settings()
