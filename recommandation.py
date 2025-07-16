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

# Convert features to numbers
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df['features'])

# Compute similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Recommendation function
def recommend_laptops(name, cosine_sim=cosine_sim):
    idx = df[df['name'] == name].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:3]
    laptop_indices = [i[0] for i in sim_scores]
    return df['name'].iloc[laptop_indices]

# Test example
print("Recommended laptops for 'HP Pavilion Gaming':")
print(recommend_laptops('HP Pavilion Gaming'))
 