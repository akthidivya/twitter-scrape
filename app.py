import pandas as pd
import utility.db as db
import utility.twitter_scrape as twitter_scrape
import streamlit as st




class App:
    """
    Function to scrape, insert it to MongoDB, Display the scraped data using Streamlit
    """
    def process(query):
        # Get the Tweets list
        tweets_list2 = twitter_scrape.scrape_twitter(query)

        # Creating a dataframe from the tweets list above
        data = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Content','url', 'Username' ,'replycount','retweet count','tweet language','tweet source','tweet like count'])

        # Display the DataFrame using Streamlit
        st.write(data)

        # Insert the DataFrame into MongoDB
        response = db.insert_pandas_df_to_mongoDB(data)

        return response




# Call the method with class
App.process("COVID Vaccine since:2021-01-01 until:2021-05-31")