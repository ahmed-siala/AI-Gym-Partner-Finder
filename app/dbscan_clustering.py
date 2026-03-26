import pandas as pd
from sklearn.cluster import DBSCAN
import numpy as np

# Sample data for gym users (user name, city)
users = [
    {"name": "Ahmed", "city": "Tunis"},
    {"name": "Mariem", "city": "Sousse"},
    {"name": "Yassine", "city": "Sfax"},
    {"name": "Fatma", "city": "Bizerte"},
    {"name": "Anis", "city": "Nabeul"},
    {"name": "Rania", "city": "Monastir"},
    {"name": "Ramy", "city": "Sfax"},
    {"name": "Emna", "city": "Kairouan"},
    {"name": "Mohaimen", "city": "Sfax"},
    {"name": "Kmar", "city": "Sfax"}
]

# Convert list of dictionaries into a DataFrame
df = pd.DataFrame(users)

# Map cities to numeric values (for DBSCAN to work)
city_mapping = {city: idx for idx, city in enumerate(df["city"].unique())}
df['city_code'] = df["city"].map(city_mapping)

# Prepare data for DBSCAN
X = df[['city_code']].values

# Apply DBSCAN with eps=0.5 (distance between points to consider part of a cluster) and min_samples=2 (minimum points to form a cluster)
db = DBSCAN(eps=0.5, min_samples=2).fit(X)

# Add DBSCAN cluster labels to the DataFrame
df['cluster'] = db.labels_

# Display the clustered users
grouped_users = df.groupby('cluster')

# Print out the clusters
for cluster_id, group in grouped_users:
    print(f"Cluster {cluster_id}:")
    for index, row in group.iterrows():
        print(f"  {row['name']} - {row['city']}")
    print("\n")