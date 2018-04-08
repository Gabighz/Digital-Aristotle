########################################################
# Perform K-means clustering on features of the words #
# (2 clusters, Keyword & Not-Keyword)                 #
#######################################################

# In the second version, might manually code weighted k-means clustering

import pylab
import numpy as np
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

    # Stores only the sum of each word
    # to be changed to something that can reference each sum to its corresponding word
    features_sum = []

    for i in range(len(dataset)):
        features_sum.append(dataset[i][1])

    # Convert array to passable numpy data which can be manipulated by sklearn
    features_sum = np.array(features_sum).reshape(-1, 1)

    # Initializes KMeans and assigns the number of clusters
    kmeans = KMeans(n_clusters = k)

    # Compute K-means clustering
    kmeans = kmeans.fit(features_sum)

    # Predict the closest cluster each observation in features_sum belongs to
    labels = kmeans.predict(features_sum)

    # Contains each observation and its label
    results = []

    index = 0 # used for iterating through dataset

    for label in labels:

        if label == 0:
            label = 'Not-Keyword'
        else:
            label = 'Keyword'

        results.append([dataset[index][0], label])

        index += 1

    # Coordinates of cluster centers (centroids)
    print("\nCoordinates of centroids: \n", kmeans.cluster_centers_)

    return results
