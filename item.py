items = {
    "Item": ["Movie1", "Movie2", "Movie3", "Movie4"],
    "Genre": ["Action Adventure", "Action Thriller", "Romance Drama", "Adventure Comedy"]
}

item_df = pd.DataFrame(items)

vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(item_df["Genre"])

item_similarity = cosine_similarity(genre_matrix)

def recommend_similar_items(liked_item, item_df, item_similarity):
    item_index = item_df[item_df["Item"] == liked_item].index[0]
    similar_items = item_similarity[item_index]
    
    similar_indices = similar_items.argsort()[::-1][1:4]
    return item_df.iloc[similar_indices]["Item"]

print("Items similar to Movie1:")
print(recommend_similar_items("Movie1", item_df, item_similarity))
