########################################################################################
# Perform K-means clustering (2 clusters, Keyword & Not-Keyword) (Gabriel Ghiuzan)     #
########################################################################################

MAX_ITERATIONS = 100

# Import data and store in dataset
def construct_dataset(word_list):

    # Contains each word as a string and the sum of its features
    dataset = []

    for word in word_list:
        for feature in range(1, len(word)):
            feature_sum += word[feature]

        dataset.append([word[0], feature_sum])

# Euclidean Distance calculator in a one-dimensional space
def euclidean_distance(p, q):
    return math.abs(q - p)

# Initialize centroids to the first elements in the dataset
def initialize_centroids(k):

    for i in range(k):
        centroids[i] = dataset[i]

    return centroids

# Apply K-means clustering to dataset
def kmeans_clustering(dataset, k):

    centroids = initialize_centroids(k)
    clusters = []

    for i in range(MAX_ITERATIONS):

        for observation in dataset:
