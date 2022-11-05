import pandas as pd

# read in data
df = pd.read_csv('csv_files/full_output copy.csv', index_col=0, low_memory=False)

# drop columns


df = df.drop(columns=['City', 'Stage Final', 'SR Final', 'Award', 'Date', 'Stage Average', 'cj1', 'cj2', 'cj3', 'srj1', 'srj2', 'srj3', 'Region'])

df['School'] = df['School'].astype(str)
df['Directors'] = df['Directors'].astype(str)
df['Conference'] = df['Conference'].astype(str)
df['Classification'] = df['Classification'].astype(str)
df['Year'] = df['Year'].astype(int)

# find columns with mixed data types
weird_cols = []
def weird_finder():
    for col in df.columns:
        weird = (df[[col]].applymap(type) != df[[col]].iloc[0].apply(type)).any(axis=1)
        if len(df[weird]) > 0:
            weird_cols.append(col)

weird_finder()

# convert all columns in weird_cols to string
for col in weird_cols:
    df[col] = df[col].astype(str)