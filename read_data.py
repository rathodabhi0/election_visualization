import os
import pandas as pd
import numpy as np

class reading_data:

    def __init__(self, file_name):
        self.file_name=file_name

    def import_file(self):
        df = pd.read_csv(self.file_name)

        print(df.head())


p = reading_data('LS_20.csv')

p.import_file()
