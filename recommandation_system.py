import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

data = {
    "User": ["Prathmesh", "Aditya", "Anupam", "Omkar", "Aftab", "Sham"],
    "Item": ["Movie1", "Movie1", "Movie1", "Movie2", "Movie3", "Movie3"],
    "Rating": [5, 4, 5, 4, 5, 4]
}

df = pd.DataFrame(data)

user_item_matrix = df.pivot_table(index="User", columns="Item", values="Rating").fillna(0)

user_similarity = cosine_similarity(user_item_matrix)


def recommend_items(user, user_item_matrix, user_similarity):
    user_index = user_item_matrix.index.get_loc(user)
    similar_users = user_similarity[user_index]
    
 
    weighted_ratings = user_item_matrix.T.dot(similar_users)
    recommendations = pd.Series(weighted_ratings, index=user_item_matrix.columns)

    rated_items = user_item_matrix.loc[user]
    recommendations = recommendations[rated_items == 0]
    
    return recommendations.sort_values(ascending=False).head(3)

print("Recommendations for Prathmesh:")
print(recommend_items("Prathmesh", user_item_matrix, user_similarity))
