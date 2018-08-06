##################################################
# Main program which executes the modules,       #
# and writes Keywords and Non-keywords to a file #
##################################################

# This constant is used in kmeans.py. It determines the number of classifications.
# Currently, we have 2 classifications, namely Keywords and Non-keywords.

import os

from XML_parser import parse_file
from feature_selection import feature_assignment
from kmeans import kmeans_clustering
from processing import pre_processing, post_processing
from f1_score_testing import f1_tests, test_individual_features

CLUSTERS = 2


def interface_path():
    path = input("Input path: ../input/first-year/CS-150/")

    return path


def main():
    # Open a file here and apply a function from XML_parser to it
    user_path = interface_path()
    path = "../input/first-year/CS-150/" + user_path
    file_number = 0
    parsed_content = parse_file(path, file_number)

    # Pre-processing to filter out stopwords from parsed_files
    filtered_content = pre_processing(parsed_content)

    # Return a two-dimensional array which contains each word and its features
    classification_features = feature_assignment(filtered_content)

    # The return is 2D array which contains each word and its label
    clustered_data = kmeans_clustering(classification_features, CLUSTERS)

    # Prints each word and its classification features
    print("\n \n Each word and its classification features: \n")
    for word in sorted(classification_features):
        # Format and content: [word, isBold, isBig, isAbnormalColour, RAKE]
        print(word)

    # Post-processing to measure the performance of our classifier
    performance = post_processing(clustered_data, user_path)

    # Tests the F1 score of each individual feature
    test_individual_features(classification_features, user_path)

    # Performs analysis of F1 scores using a new normalising method
    f1_tests(classification_features, user_path)

    # Extracts the name of the file and its extension from the path provided by the user
    file_name, file_extension = user_path.split('.')

    # Write to file
    output_path = "../output/first-year/CS-150/" + file_name + ".txt"

    # Enables us to create paths from within the program
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    file = open(output_path, "w")

    for observation in clustered_data:
        file.write(str(observation) + "\n")

    file.close()

    # F1 score from 0 to 1
    print("\n F1 score: ", performance)


main()
