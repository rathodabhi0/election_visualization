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
        print("Party vote share in state")
        df2 = df1[['STATE','PARTY','TOTAL VOTES', 'TOTAL ELECTORS']]
        df2['Vote share']= ((df2['TOTAL VOTES']/df2['TOTAL ELECTORS'])*100)
        return df2[['STATE', 'PARTY', 'Vote share']].groupby(['STATE', 'PARTY']).sum()

    def state_constituency_party_winner(self):
        print("Constituency winner by Party")
        df2 = df1.loc[df1.WINNER == 1]
        return df2[['STATE', 'CONSTITUENCY', 'PARTY', 'WINNER']]

    def gender(self):
        print("This is gender table")
        df2 = df1[['STATE', 'GENDER']]
        return df2.groupby(['STATE', 'GENDER']).sum()

class partywide_analysis:
    def __init__(self, df1):
        self.df1=df1

    def party_vote(self):
        print("Party vote share in Nationally")
        df2 = df1[['PARTY','TOTAL VOTES']].groupby(['PARTY']).sum()
        df3 = df1[['TOTAL VOTES'][0]].sum()
        df2['Vote share'] = ((df2['TOTAL VOTES']/df3)*100)
        return df2.sort_values(by=['Vote share'], ascending=False)

    def total_candidates_by_party(self):
        print("Total number of candidates for each party")
        df2 = df1[df1.PARTY != 'NOTA']
        df2 = df2['PARTY'].value_counts()
        return

if __name__ == "__main__":
    abhi= 'LS_20.csv'
    place_holder_for_df = reading_data(abhi)
    df1 = place_holder_for_df.import_file()
    statewide_analysis_method = statewide_analysis(df1)
    partywide_analysis_method= partywide_analysis(df1)
    print(statewide_analysis_method.state_wise_party_vote_share())
    print(statewide_analysis_method.state_constituency_party_winner())
    print(statewide_analysis_method.gender())
    print(partywide_analysis_method.party_vote())
    print(partywide_analysis_method.total_candidates_by_party())