##################################################
# Main program which executes the modules,       #
# and writes Keywords and Non-keywords to a file #
##################################################

# This constant is used in kmeans.py. It determines the number of classifications.
# Currently, we have 2 classifications, namely Keywords and Non-keywords.
CLUSTERS = 2

import os

from XML_parser import parse_file
from feature_selection import feature_assignment
from kmeans import kmeans_clustering
from processing import pre_processing, post_processing


def interface_path():
    path = input("Input path: ../input/first-year/CS-150/")

    return path


def main():
    # Open a file here and apply a function from XML_parser to it
    user_path = interface_path()
    path =  "../input/first-year/CS-150/" + user_path
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

    # F1 score from 0 to 1
    print("\n F1 score: ", performance)

    # Write to file
    output_path = "../output/first-year/CS-150/" + path

    # Enables us to create paths from within the program
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    file = open(output_path, "w")

    for observation in clustered_data:
        file.write(str(observation) + "\n")

    file.close()


main()
