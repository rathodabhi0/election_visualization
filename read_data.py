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

    def gender(self):
        return df1.groupby(['STATE', 'GENDER']).sum()

class partywide_analysis:
    def __init__(self, df1):
        self.df1=df1

    def party_vote(self):
        return df1.groupby(['PARTY']).sum()

if __name__ == "__main__":
    abhi= 'LS_20.csv'
    place_holder_for_df = reading_data(abhi)
    df1 = place_holder_for_df.import_file()
    statewide_analysis_method = statewide_analysis(df1)
    partywide_analysis_method= partywide_analysis(df1)
    print(statewide_analysis_method.state_party())
    print(statewide_analysis_method.state_constituency())
    print(statewide_analysis_method.gender())
    print(partywide_analysis_method.party_vote())


