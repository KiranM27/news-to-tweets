import os
import pickle
from modules.constants import DATA_FOLDER

class PersistDictData:

    def __init__(self):
        
        # ensure that the /data folder exists
        os.makedirs(DATA_FOLDER, exist_ok=True)
    
    def save(self, filename, data):
        with open(f"{DATA_FOLDER}/{filename}.pkl", "wb") as f:
            pickle.dump(data, f)

    def save_key_value(self, filename, key, value):
        data = self.load(filename)
        data[key] = value
        self.save(filename, data)

    def load(self, filename):

        # if the file does not exist, return an empty dictionary
        if not os.path.exists(f"{DATA_FOLDER}/{filename}.pkl"):
            return {}

        with open(f"{DATA_FOLDER}/{filename}.pkl", "rb") as f:
            return pickle.load(f)