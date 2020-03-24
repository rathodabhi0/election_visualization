import os
import pandas as pd
import numpy as np
import redis
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

    def state_wise_party_vote_share(self):
        df2 = df1[['STATE','PARTY','TOTAL VOTES', 'TOTAL ELECTORS']]
        df2['Vote share']= ((df2['TOTAL VOTES']/df2['TOTAL ELECTORS'])*100)
        return df2[['STATE', 'PARTY', 'Vote share']].groupby(['STATE', 'PARTY']).sum()

    def state_constituency(self):
        return df1.groupby(['STATE','CONSTITUENCY', 'TOTAL ELECTORS']).sum()

    def gender(self):
        return df1.groupby(['STATE', 'GENDER', 'TOTAL ELECTORS']).sum()

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
    print(statewide_analysis_method.state_wise_party_vote_share())
    print(statewide_analysis_method.state_constituency())
    print(statewide_analysis_method.gender())
    print(partywide_analysis_method.party_vote())