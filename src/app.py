import streamlit as st
from src.monty_hall import simulate_games
import time

st.title(':zap: Monty Hall Simulation')
st.image('./src/image/1200px-Monty_open_door.svg.png')

num_games = st.number_input('Please enter number of games to simulate:',
                            min_value=1,
                            max_value=100000,
                            value=100)

# Create two lists to hold win percentages for both cases
wins_no_switch = 0
wins_switch = 0

col1, col2 = st.columns(2)
col1.subheader('Win Percentage Without Switching')
chart1 = col1.line_chart(x=None, y=None, height=400)
col2.subheader('Win Percentage With Switching')
chart2 = col2.line_chart(x=None, y=None, height=400)

for i in range(num_games):
    # Simulate one game at a time
    num_win_without_switching, num_win_with_switching = simulate_games(1)

    # Calculate win percentages for both cases and add to lists
    wins_no_switch += num_win_without_switching
    wins_switch += num_win_with_switching

    # Display the current percentages after each game
    chart1.add_rows([wins_no_switch/(i+1)])
    chart2.add_rows([wins_switch/(i+1)])

    # Add a delay to create a slow loop effect
    time.sleep(0.01)

