import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense
from sklearn.preprocessing import MinMaxScaler

# this file will be revisited after other core features are built first

# we can try to collect the data from kaggle under stock market data
#Format: Date, Low, Open, Volume,  High,  Close, Adjusted Close

# there will be 3 functions dicated in this file
# building the model from raw data and saving it
# loading the model
# adding additional data points to previous model and refitting it

class t_model:
    def __init__(self):
        self.current_model = ""
        self.data_read = ""

    def build_model(self, file_name_path, model_name):
        df = pd.read_csv(file_name_path)
        df["Date"] = pd.to_datetime(df.Date, format="%Y-%m-%d")

        df.index =df['Date']
        # sorting the data based on the date that it was entered
        data = df.sort_index(ascending=True, axis=0)
        # creating a new dataframe based on the length of the original dataframe
        new_ds = pd.DataFrame(0, len(df), columns=["Date, Close"])

        # collecting the subset of information that is required for the new model
        for i in range(0, len(data)):
            new_ds["Date"][i] = data["Date"][i]
            new_ds["Close"][i] = data["Close"][i]

        




    def load_model(self, model_name):
        return 0



    def rebuild_model(self, data, model):
        return 0




