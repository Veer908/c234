import pandas as pd
data = pd.read_csv('sports_dataset.csv')

data.loc[data['Goal'] < 75, 'student_promoted'] = 'Not_Promoted'
data.loc[data['Goal']  > 75, 'student_promoted'] = 'Promoted'

print(data)