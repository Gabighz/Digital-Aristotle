#######################################################
# Tests the performance of individual classification  #
# features with F1 score                              #
# Author: Slade Brooks                                #
#######################################################

from kmeans import kmeans_clustering
from processing import pre_processing, post_processing

# Global for the number of clusters used by k-means clustering.
CLUSTERS = 2


# Computes the F1 score of each classification feature
# @param classification_features: Contains each word and its features, i.e.[word, is_bold, is_larger, is_not_black, RAKE]
# @param user_path: Specifies what lecture notes file will be loaded into the Keyword extractor.
def test_individual_features(classification_features, filename):

    for index in range(len(classification_features[0]) - 1):
        temp_array = []
        for word in classification_features:
            temp_array.append([word[0], word[index + 1]])

        # The return is 2D array which contains each word and its label
        clustered_data = kmeans_clustering(temp_array, CLUSTERS)

        # Post-processing to measure the performance of our classifier
        performance = post_processing(clustered_data, filename)

        # F1 score from 0 to 1
        print(" \n Classification feature: " + str(index + 1) + ", F1 score: ", performance)


# Removes RAKE as a classification features. This is done to measure the performance without it.
# @param classification_features: Contains each word and its features, i.e.[word, is_bold, is_larger, is_not_black, RAKE]
# @return no_rake: Contains each word and its features without RAKE, i.e. [word, is_bold, is_larger, is_not_black]
def remove_rake(classification_features):
    no_rake = []
    for word in classification_features:
        no_rake.append([word[0], word[1], word[2], word[3]])
    return no_rake


# Applies k-means clustering with the feature(s) of the test case. Then, F1 score is computed.
# @param classification_features: Contains each word and its features, i.e.[word, is_bold, is_larger, is_not_black, RAKE]
# @param filename: Specifies what lecture notes file will be loaded into the Keyword extractor.
# @return performance: Outputs the F1 score for a particular test case.
def calculate_f1(classification_features, filename):

    # The return is 2D array which contains each word and its label
    clustered_data = kmeans_clustering(classification_features, CLUSTERS)

    # Post-processing to measure the performance of our classifier
    performance = post_processing(clustered_data, filename)

    return performance
