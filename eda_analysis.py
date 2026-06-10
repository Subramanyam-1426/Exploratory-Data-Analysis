import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("data/netflix_titles.csv")

# Basic Information
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")

# -----------------------------------
# Movies vs TV Shows
# -----------------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="type", data=df)
plt.title("Movies vs TV Shows")
plt.show()

# -----------------------------------
# Content Added Per Year
# -----------------------------------
plt.figure(figsize=(12,5))
df["release_year"].value_counts().sort_index().plot()
plt.title("Content Released Over Years")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

# -----------------------------------
# Top 10 Countries
# -----------------------------------
top_countries = df["country"].value_counts().head(10)

plt.figure(figsize=(10,5))
top_countries.plot(kind="bar")
plt.title("Top 10 Countries Producing Netflix Content")
plt.ylabel("Count")
plt.show()

# -----------------------------------
# Ratings Distribution
# -----------------------------------
plt.figure(figsize=(10,5))
sns.countplot(y="rating",
              data=df,
              order=df["rating"].value_counts().index)
plt.title("Content Ratings")
plt.show()

# -----------------------------------
# Top Genres
# -----------------------------------
genres = df["listed_in"].str.split(", ").explode()

plt.figure(figsize=(10,6))
genres.value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Genres on Netflix")
plt.ylabel("Count")
plt.show()

print("\nTop Genres:")
print(genres.value_counts().head(10))