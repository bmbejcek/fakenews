import pandas as pd
from textblob import TextBlob

pd.options.mode.chained_assignment = None  # ignores the SettingWithCopy Warning
df = pd.read_csv('INPUT.csv', encoding = 'utf8')
df['polarity'] = 0.0
df['subjectivity'] = 0.0
for i in range(0, len(df.index)):
    print(i)
    blob = TextBlob(str(df['text'][i]))
    df['subjectivity'][i] = blob.sentiment.subjectivity
    df['polarity'][i] = blob.sentiment.polarity

print(df.head())
df.to_csv('OUTPUT.csv', encoding = 'utf8')
