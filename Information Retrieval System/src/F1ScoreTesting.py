from kmeans import kmeans_clustering
from processing import pre_processing, post_processing

def F1Tests(classification_features, user_path):
    CLUSTERS = 2

    for word in classification_features:
        for x in range(4):
            if(x > 0):
                if (word[x] > 0):
                    word[x] = 1

    # The return is 2D array which contains each word and its label
    clustered_data = kmeans_clustering(classification_features, CLUSTERS)

    # Post-processing to measure the performance of our classifier
    performance = post_processing(clustered_data, user_path)

    # F1 score from 0 to 1
    print("\n new F1 score: ", performance)
