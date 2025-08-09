import streamlit as st

import datetime

date = 0

def is_scheduled_for_day(habit, date, completions):
        freq = habit.get("frequency", "Daily")
        if freq == "Daily":
                return True
        
        elif freq.startswith("Every"):
                # Extract N from the "Every N days"
                words = freq.split()
                try:
                    n = int(words[1])
                except:
                        return False
                
                # Get the habit's "start_date"
                start_date = habit.get("start_date")
                if not start_date:
                        return False
                
                start_date = datetime.date.fromisoformat(start_date)
                days_since = (date - start_date).days
                if days_since < 0:
                        return False
                return days_since % n == 0
        return False

if "completions" not in st.session_state:
        st.session_state["completions"] = {}
        
today = datetime.date.today()
date = [today - datetime.timedelta(days=i) for i in range(6, -1, -1)]
labels = [d.strftime('a% %d') for d in dates ]


st.title("Habit Tracker Dashbaord")

if 'habits' not in st.session_state or not st.session_state['habits']:
        st.info('No habits yet! Add some in the "Add Habit" tab.')
else:
        # Table header
        st.markdown("|Habit|"+"|".join(labels)+"|")
        st.markdown("|--"*(len(labels)+1)+"|")
        
        for habit in st.session_state['habits']:
                row=[]
                habit_name = habit['name']
                # Make sure the habit has a start_date (set when added)
                if not habit.get("start_date"):
                        habit['start_date'] = today.isoformat()
                for date in dates:
                        date_str = date.isoformat()
                        # Only scheduled days are actionable
                        if is_scheduled_for_day(habit, date, st.session_state['completions']):
                                # Look up completions
                                completed_today = date_str in st.session_state['completions'] and habit_name in st.session_state['completions'][date_str]
                                if date == today:
                                        # Today: show interactive button if not ocmpleted