from pymongo import MongoClient


"""
Create a connection to MongoDB
"""
def connect_mongoDB():
    # Try exception block to handle the exceptions
    try:
        # MongoDB connection string
        client = MongoClient("mongodb://localhost:27017")

        # MongoDB DB name
        db = client["zen"]

        # MongoDB collection name
        collection = db["twitter"]

        return collection
    
    except Exception as e:
        print(e)
        return False



def insert_pandas_df_to_mongoDB(data):
    # Try exception block to handle the exceptions
    try:
        # Reset the index of a DataFrame
        data.reset_index(inplace=True)

        # Convert data to dict
        data_dict = data.to_dict("records")

        # Get the collection name from the connection function
        collection = connect_mongoDB()

        # Insert into collections
        records = collection.insert_many(data_dict)

        # Return the response
        return records
    
    except Exception as e:
        print(e)
        return False