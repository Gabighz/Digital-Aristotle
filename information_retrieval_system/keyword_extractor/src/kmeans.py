#######################################################
# Perform K-means clustering on features of the words #
# (2 clusters, Keyword & Not-Keyword)                 #
# Author: Gabriel Ghiuzan                             #
#######################################################

import numpy as np
from sklearn.cluster import KMeans


# Creates an array which contains each word and the sum of its features
#
# @param classification_features: A two-dimensional array which contains each word and its features
# @return words_with_sum: A two-dimensional array which contains each word and the sum of its features
def features_summing(classification_features):
    # Contains each word as a string and the sum of its features
    words_with_sum = []

    for word in classification_features:

        # Stores the sum of features of each word
        feature_sum = 0

        for feature in range(1, len(word)):
            feature_sum += word[feature]

        words_with_sum.append([word[0], feature_sum])

    return words_with_sum


# Apply K-means clustering to a two-dimensional array which contains each word and its features
#
# @param classification_features: A two-dimensional array which contains each word and its features
#        k: The number of clusters desired to result out of k-means clustering
# @return results: Contains each word and its Keyword or Non-keyword label
def kmeans_clustering(classification_features, k):

    # An array which contains each word and the sum of its features
    words_with_sum = features_summing(classification_features)

    # Will store only the sum of each word
    features_sum = []

    # Extracts only the sum of each word and appends it to features_sum
    for i in range(len(words_with_sum)):
        features_sum.append(words_with_sum[i][1])

    # Converts array to passable numpy data which can be manipulated by sklearn
    features_sum = np.array(features_sum).reshape(-1, 1)

    # Initializes the KMeans object and assigns the number of clusters
    kmeans = KMeans(n_clusters = k)

    # Computes K-means clustering given the sum of each word as discrete values
    kmeans = kmeans.fit(features_sum)

    # Predicts the closest cluster each item in features_sum belongs to
    labels = kmeans.predict(features_sum)

    # Will contain each word and its label
    # For example, [word, 0] or [word, 1], which means [word, Non-keyword] or [word, Keyword]
    results = []

    # Appends each word and its label to results
    for i in range(len(labels)):
        results.append([words_with_sum[i][0], labels[i]])

    return results
