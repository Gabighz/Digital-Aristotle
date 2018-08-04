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

    test_individual_features(classification_features,user_path)
