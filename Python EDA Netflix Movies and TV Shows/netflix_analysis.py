import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/laingangiang/Downloads/mymoviedb (1).csv", encoding="latin-1", engine="python", header=0)

# Display the first 10 rows of the DataFrame
print(df.head(10))

# Display the last 10 rows of the DataFrame
print(df.tail(10))

# Remove rows and columns with missing values
df = df.dropna(axis=0)
df = df.dropna(axis=1)

# Display the data set summary about the DataFrame
print(df.info())

# Display the statistical summary of the DataFrame
print(df.describe())

# Display the original data types of each column in the DataFrame
print(df.dtypes)

# Convert data type
df = df.astype({"Vote_Count": "int64"})
df = df.astype({"Vote_Average": "float64"})

# Display the data types of the "Vote_Count" and "Vote_Average" columns after conversion
print(df.dtypes[["Vote_Count", "Vote_Average"]])

# Define the ranges for Popularity
bins1 = np.linspace(df["Popularity"].min(), df["Popularity"].max(), 5)
labels1 = ["Low", "Moderate", "High", "Trending"]

# Define the ranges for Vote_Count
bins2 = np.linspace(df["Vote_Count"].min(), df["Vote_Count"].max(), 5)
labels2 = ["Niche", "Limited", "Popular", "Mainstream"]

# Define the ranges for Vote_Average
bins3 = np.linspace(df["Vote_Average"].min(), df["Vote_Average"].max(), 5)
labels3 = ["Poor", "Average", "Good", "Excellent"]

# Create new categorical columns based on the defined ranges
df["Popularity_Category"] = pd.cut(df["Popularity"], bins=bins1, labels=labels1)
df["Vote_Count_Category"] = pd.cut(df["Vote_Count"], bins=bins2, labels=labels2)
df["Vote_Average_Category"] = pd.cut(df["Vote_Average"], bins=bins3, labels=labels3)

# Convert the values in the Original_Language column to uppercase
df["Original_Language"] = df["Original_Language"].str.upper()

# Display the unique values in the "Original_Language" and "Genre" columns
print(df["Original_Language"].unique())
print(df["Genre"].str.split(", ").explode().unique())

# Create dummy variables for "Original_Language" and "Genre" columns
original_language_dummies = pd.get_dummies(df["Original_Language"])
genre_dummies = pd.get_dummies(df["Genre"].str.split(", ").explode())

# Group the dummy variables by the original index to combine the multiple genres for each movie
grouped_genre_dummies = genre_dummies.groupby(genre_dummies.index).max()
grouped_language_dummies = original_language_dummies.groupby(original_language_dummies.index).max()

# Create pivot tables for genre and language analysis
genre_df = df.assign(Genre=df["Genre"].str.split(", ")).explode("Genre")

# Calculate average popularity by genre and language
average_popularity_by_genre = genre_df.pivot_table(index="Genre", values="Popularity", aggfunc="mean")

print("Average Popularity by Genre")
print(average_popularity_by_genre)

# Calculate average popularity by language
average_popularity_by_language = df.pivot_table(index="Original_Language", values="Popularity", aggfunc="mean")

print("Average Popularity by Language")
print(average_popularity_by_language)

# Calculate movie count by genre and language
movie_count_by_genre = genre_df.pivot_table(index="Genre", values="Title", aggfunc="count").rename(columns={"Title": "Movie_Count"})

print("Movie Count by Genre")
print(movie_count_by_genre)

# Calculate movie count by language
movie_count_by_language = df.pivot_table(index="Original_Language", values="Title", aggfunc="count").rename(columns={"Title": "Movie_Count"})

print("Movie Count by Language")
print(movie_count_by_language)

# Create a bubble chart for Genre vs. Average Popularity sized by movie count
genre_bubble_df = average_popularity_by_genre.join(movie_count_by_genre).reset_index()

plt.figure(figsize=(14, 8))
sns.scatterplot(
    data=genre_bubble_df,
    x="Genre",
    y="Popularity",
    size="Movie_Count",
    sizes=(100, 2000),
    legend=False,
    alpha=0.7,
    color="#1f77b4"
)
plt.title("Genre vs. Average Popularity Sized by Movie Count")
plt.xlabel("Genre")
plt.ylabel("Average Popularity")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Calculate average vote count by genre and language
average_vote_count_by_genre = genre_df.pivot_table(index="Genre", values="Vote_Count", aggfunc="mean")

print("Average Vote count by Genre")
print(average_vote_count_by_genre)

# Calculate average vote count by language
average_vote_count_by_language = df.pivot_table(index="Original_Language", values="Vote_Count", aggfunc="mean")

print("Average Vote count by Language")
print(average_vote_count_by_language)

# Plot horizontal bar chart (sorted) for average popularity by genre
average_popularity_by_genre.sort_values("Popularity", ascending=False).head(10).plot(kind="bar", legend=False)

plt.title("Average Popularity by Genre (Top 10)")
plt.xlabel("Genre")
plt.ylabel("Average Popularity")
plt.tight_layout()
plt.show()

# Plot horizontal bar chart (sorted) for movie count by genre
movie_count_by_genre.sort_values("Movie_Count", ascending=False).head(10).plot(kind="bar", legend=False)

plt.title("Movie Count by Genre (Top 10)")
plt.xlabel("Genre")
plt.ylabel("Movie Count")
plt.tight_layout()
plt.show()

# Plot horizontal bar chart (sorted) for average vote count by genre
average_vote_count_by_genre.sort_values("Vote_Count", ascending=False).head(10).plot(kind="bar", legend=False)

plt.title("Average Vote Count by Genre (Top 10)")
plt.xlabel("Genre")
plt.ylabel("Average Vote Count")
plt.tight_layout()
plt.show()

# Plot horizontal bar chart (sorted) for average popularity by language
average_popularity_by_language.sort_values("Popularity", ascending=False).head(10).plot(kind="bar", legend=False)

plt.title("Average Popularity by Language (Top 10)")
plt.xlabel("Original Language")
plt.ylabel("Average Popularity")
plt.tight_layout()
plt.show()

# Plot horizontal bar chart (sorted) for movie count by language
movie_count_by_language.sort_values("Movie_Count", ascending=False).head(10).plot(kind="bar", legend=False)

plt.title("Movie Count by Language (Top 10)")
plt.xlabel("Original Language")
plt.ylabel("Movie Count")
plt.tight_layout()
plt.show()

# Plot horizontal bar chart (sorted) for average vote count by language
avg_vote_lang_df = average_vote_count_by_language.reset_index().sort_values(by="Vote_Count", ascending=False).head(10)
plt.figure(figsize=(20, 12))
sns.barplot(x="Original_Language", y="Vote_Count", data=avg_vote_lang_df, color="#1f77b4")
plt.title("Average Vote Count by Language (Top 10)")
plt.xlabel("Original Language")
plt.ylabel("Average Vote Count")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Vote_Average distribution by top genres
top_genres = genre_df["Genre"].value_counts().head(6).index
filtered = genre_df[genre_df["Genre"].isin(top_genres)]

plt.figure(figsize=(12, 6))
sns.boxplot(x="Genre", y="Vote_Average", data=filtered)
plt.title("Vote Average Distribution by Genre (Top 6)")
plt.xlabel("Genre")
plt.ylabel("Vote Average")
plt.tight_layout()
plt.show()

# Correlation between popularity, vote count, and vote average
corr_cols = ["Popularity", "Vote_Count", "Vote_Average"]
df[corr_cols] = df[corr_cols].apply(pd.to_numeric, errors='coerce')

sns.heatmap(df[corr_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation between popularity, vote count, and vote average")
plt.tight_layout()
plt.show()
