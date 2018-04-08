########################################################
# Perform K-means clustering on features of the words #
# (2 clusters, Keyword & Not-Keyword)                 #
#######################################################

# In the second version, might manually code weighted k-means clustering

import pylab
from sklearn.cluster import KMeans

# Create a dataset from the list of words
def construct_dataset(word_list):

    # Contains each word as a string and the sum of its features
    dataset = []

    for word in word_list:
        
        # Stores the sum of features of each word
        feature_sum = 0

        for feature in range(1, len(word)):
            feature_sum += word[feature]

        dataset.append([word[0], feature_sum])

    return dataset

# Apply K-means clustering to dataset
def kmeans_clustering(word_list, k):

    dataset = construct_dataset(word_list)

    # to be changed to something that can reference each sum to its corresponding word
    # after ensuring that the program is working properly
    features_sum = [sum for sum in dataset[enumerate(dataset)][1]]

    # Number of clusters
    kmeans = KMeans(n_clusters = k)

    # Compute K-means clustering
    kmeans = kmeans.fit(features_sum)

    # Predict the closest cluster each observation in features_sum belongs to
    labels = kmeans.predict(features_sum)

    # Coordinates of cluster centers (centroids)
    print(kmeans.cluster_centers_)

    pylab.show() # to be removed after ensuring that the program is working properly

    # Labels of each point
    return kmeans.labels_
