import pandas as pd
from pandas import DataFrame


class DatabaseService:
    def __init__(self):
        self.data = pd.read_csv(r'../data/data.csv', sep=";")

    def get_data(self) -> DataFrame:
        return self.data
