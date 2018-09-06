from kmeans import kmeans_clustering
from processing import pre_processing, post_processing

def test_individual_features(classification_features, user_path):
    CLUSTERS = 2

    for x in range(len(classification_features[0])-1):
        temp_array = []
        for word in classification_features:
            temp_array.append([word[0],word[x+1]])

        # The return is 2D array which contains each word and its label
        clustered_data = kmeans_clustering(temp_array, CLUSTERS)

        # Post-processing to measure the performance of our classifier
        performance = post_processing(clustered_data, user_path)

            # F1 score from 0 to 1
        print("\n          feature "+ str(x+1) + " F1 score: ", performance)

    #test_individual_features(classification_features,user_path)


def remove_rake(classification_features):
    temp_array = []
    for word in classification_features:
        temp_array.append([word[0],word[1],word[2],word[3],])

    return temp_array

def calculate_F1(word_array, user_path):
    CLUSTERS = 2

    # The return is 2D array which contains each word and its label
    clustered_data = kmeans_clustering(word_array, CLUSTERS)

    # Post-processing to measure the performance of our classifier
    performance = post_processing(clustered_data, user_path)

    return performance
