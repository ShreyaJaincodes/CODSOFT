import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample laptop data
data = {
    'name': [
        'Dell Inspiron 15',
        'HP Pavilion Gaming',
        'Lenovo ThinkPad X1',
        'Asus ROG Strix',
        'Apple MacBook Air'
    ],
    'features': [
        'Dell Intel i5 8GB Office',
        'HP Ryzen 5 16GB Gaming',
        'Lenovo Intel i7 16GB Business',
        'Asus Ryzen 7 16GB Gaming',
        'Apple M1 8GB Student'
    ]
}

df = pd.DataFrame(data)

# TF-IDF vectorizer on features
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df['features'])

# Function to recommend laptops based on user query (e.g., "Graphic designing")
def recommend_laptops_by_feature(query, tfidf_matrix=tfidf_matrix):
    query_vec = tfidf.transform([query])
    cosine_sim = linear_kernel(query_vec, tfidf_matrix).flatten()
    top_indices = cosine_sim.argsort()[-3:][::-1]  # Top 3 results
    return df.iloc[top_indices][['name', 'features']]

# Example usage
print("Recommended laptops for 'Graphic designing':")
print(recommend_laptops_by_feature('Graphic designing'))
