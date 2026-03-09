import pandas as pd
import numpy as np

# Sample Raw Data
raw_data = {
    'auth_id': [101, 102, 101, 104, 105],
    'candidate_name': ['  jOHN dOE  ', 'Jane Smith', 'John Doe', 'ALICE WONG', '  bob brown'],
    'score_raw': ['85', '92', '85', 'N/A', '78%'],
    'date_captured': ['2026-01-15', '15/01/26', '2026-01-15', '2026-02-01', '02-01-2026']
}
df = pd.DataFrame(raw_data)

#Cleaning Names and then catching duplicate data
df['candidate_name'] = df['candidate_name'].str.strip().str.title()
df = df.drop_duplicates()

#cleaning the raw score data and filling the null values with avg score
df['score_raw'] = df['score_raw'].str.replace('%', '', regex=False)
df['score_raw'] = pd.to_numeric(df['score_raw'], errors='coerce')
df['score_raw'] = df['score_raw'].fillna(df['score_raw'].mean()).round(0).astype(int)

#Formatitng date
df['date_captured'] = pd.to_datetime(df['date_captured'], format='mixed').dt.strftime('%Y-%m-%d')

# Business Logic
def categorize_candidate(score):
    if score >= 90:
        return 'Top Tier'
    elif score >= 75:
        return 'Qualified'
    else:
        return 'Pipeline'

df['hiring_status'] = df['score_raw'].apply(categorize_candidate)

#Creating a csv file of cleaned data
df.to_csv('TalentLogic_Final_Project.csv', index=False)

print("--- PROJECT TalentLogic_ETL: SUCCESS ---")
print(df)