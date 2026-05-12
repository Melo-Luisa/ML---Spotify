import pandas as pd


df = pd.read_csv('dataset.csv')
#show the first 5 rows of the dataset
# print(df.head())
#show the summary of the dataset
# print(df.info())
#show the number of missing values in each column
# print(df.isnull().sum())
#show the statistical summary of the dataset
# print(df.describe())
# show the number of rows in the dataset
# print(len(df))

#explore the dataset by showing the unique values in each column
# print(df["artists"].value_counts().head(10))
# print(df[df["popularity"] > 80].head(10))
#group by artists and popularity and show the mean popularity for each artist
# media_artista = df.groupby("artists")["popularity"].mean()
# media_artista = media_artista.sort_values(ascending=False)

# print(media_artista.head(10))
print(df.corr(numeric_only=True))

