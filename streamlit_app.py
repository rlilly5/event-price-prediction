import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import math
#import matplotlib.pyplot as plt
#from sklearn import datasets
#from sklearn.ensemble import RandomForestRegressor

events = pd.read_csv("ProcessedTicketData.csv", parse_dates=True)


# Main Title
def main():
    st.write("""
# Concert Ticket Timing Predictor
         
This app predicts the best time to purchase **Event Tickets**!
         """)
    st.write('---')

    # User input
    artist_input = st.selectbox("Select Artist", events['artist'].unique())
    artist_popularity = st.slider("Artist Popularity (1-10)", 1, 10)
    concert_venue = st.selectbox("Select Venue", events['venue'].unique())
    concert_day = st.selectbox("Concert Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    concert_date = st.date_input("Concert Date", value=None)
    concert_time = st.time_input("Concert Time")

    # Make prediction
    if st.button("Predict"):
        preprocessed_input = preprocess_input(artist_popularity, venue_capacity, concert_day, concert_time)
        best_time, worst_time = predict_best_worst_times(preprocessed_input)

        st.write("Best time to buy tickets:", best_time)
        st.write("Worst time to buy tickets:", worst_time)

if __name__ == "__main__":
    main()
