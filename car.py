import streamlit as st
import random
import time

# Initialize Streamlit app
st.title("Car Racing Game 🏎️")
st.markdown("Press the **Race** button to start the race!")

# Set up initial car positions
car_positions = [0, 0, 0]
car_names = ["Car A", "Car B", "Car C"]
finish_line = 50

# Display the race track
def display_race():
    for i, pos in enumerate(car_positions):
        st.write(f"{car_names[i]}: " + "🚗" * pos)

# Button to start the race
if st.button("Race!"):
    st.write("The race has begun!")
    while max(car_positions) < finish_line:
        # Randomly update positions
        for i in range(len(car_positions)):
            car_positions[i] += random.randint(1, 3)
        st.empty()  # Clear previous output
        display_race()
        time.sleep(0.5)  # Pause for a better racing animation

    # Determine the winner
    winner = car_names[car_positions.index(max(car_positions))]
    st.success(f"🏆 {winner} wins the race!")
