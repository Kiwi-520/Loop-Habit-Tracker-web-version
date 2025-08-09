import streamlit as st

# st.title('Add Habit')
# st.write('Form to add new habit will go here.')

# Initialize habits list in session state

if 'habits' not in st.session_state:
        st.session_state['habits'] = []

st.title('Add Habit')

# Habit form

name = st.text_input('eg. Exercise')
question = st.text_input('eg. Did u exercise today?')
frequency_option = st.selectbox('Frequency',['Daily', 'Weekly', 'Every N days'])
n_days = None

if frequency_option == 'Every N days':
        n_days = st.number_input('Every how many days', min_value = 2 ,max_value = 365, value = 3, step =1)


reminder = st.selectbox('reminder',['on','off'])
reminder_tine = 0

if reminder == 'on':
        reminder_time = st.time_input('Reminder time')


notes = st.text_area('Notes')

if st.button('Add habit'):
        if not name:
                st.error('Habit name required!')
        elif frequency_option == 'Every N days' and not n_days:
                st.error('Please enter a number of days.')
        elif reminder == 'on' and not reminder_time:
                st.error('Please pick a reminder time.')
        else:
                habit={
                        'name':name,
                        'question':question,
                        'frequency':frequency_option,
                        'reminder':reminder,
                        'notes':notes
                }
                st.session_state['habits'].append(habit)
                st.success(f'Habit "{name}" added !')

if st.session_state['habits']:
        st.write("Current Habits:", st.session_state['habits'])
        
        