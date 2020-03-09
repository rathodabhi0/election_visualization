import os
import pandas as pd
import numpy as np
# import dash
# import dash_core_components as dcc
# import dash_html_components as html

class reading_data:

    def __init__(self, file_name):
        self.file_name=file_name

    def import_file(self):
        df = pd.read_csv(self.file_name)
        return df

##analysis of every state: Grouped by [(State,party), (State,Constituency)]
class statewide_analysis:
    def __init__(self, df1):
        self.df1=df1

    def state_party(self):
        return df1.groupby(['STATE','PARTY']).sum()

    def state_constituency(self):
        return df1.groupby(['STATE','CONSTITUENCY']).sum()


if __name__ == "__main__":
    abhi= 'LS_20.csv'
    place_holder_for_df = reading_data(abhi)
    df1 = place_holder_for_df.import_file()
    new_method = statewide_analysis(df1)
    print(new_method.state_party())
    print(new_method.state_constituency())


