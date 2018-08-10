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


#test the normalising approach of [word,6,3,0] becomes [word,1,1,0]
def new_norm_approach(classification_features, user_path):

    for word in classification_features:
        for x in range(4):
            if(x > 0):
                if (word[x] > 0):
                    word[x] = 1

    classification_features = remove_rake(classification_features)
    # F1 score from 0 to 1

    print("\n F1 - first new norm approach(without rake): ", calculate_F1(classification_features,user_path))

    #test_individual_features(classification_features,user_path)


#test the normalising approach of [word 5,2,0] becomes [word,1] and [word,0,0,0] becomes [word,o]
def new_norm_approach_2(classification_features, user_path):
    temp_array = []

    for word in classification_features:
        if(word[1] != 0 or word[2] != 0 or word[3] != 0):
            temp_array.append([word[0],1])
        else:
            temp_array.append([word[0],0])

    # prints the f1 score of this approach without the rake
    print("\n F1 - second new norm approach(without rake): ", calculate_F1(temp_array, user_path))

    #test_individual_features(temp_array, user_path)


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
