import os
import pandas as pd
import numpy as np

class reading_data:

    def __init__(self, file_name):
        self.file_name=file_name

    def import_file(self):
        df = pd.read_csv(self.file_name)
        return df


class statewide_analysis:

    def seats(self):
        place_holder_for_df = reading_data('LS_20.csv')
        df1 = place_holder_for_df.import_file()
        print(df1.groupby(['STATE','PARTY']).sum())

if __name__ == "__main__":

    p = statewide_analysis()
    p.seats()

