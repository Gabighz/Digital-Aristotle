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
from processing import *

def interface_path():
    path = input("Type the relative path of your input file: ")

    return path

def interface_output(raw_data, filtered_data, classification_features, performance):
    print("\n What would you like to print? : \n")
    print("1. The raw XML data for the file processed")
    print("2. The filtered data in the pre-processor")
    print("3. Each word and its classification features")
    print("4. F1 score")

    option = int(input("\n Option: "))

    if option == 1:
        # Prints the raw XML data so we can check if the pre-processor is working correctly
        print("\n Raw XML Data: \n")
        counter = 0
        for word_array in sorted(raw_data):
            print(word_array)
            counter += 1
        print("\n Number of word arrays in raw XML data: ", counter)

    elif option == 2:
        # Prints the filtered data so we can check if the pre-processor is working correctly
        print("\n Filtered data (each word with its own XML features): \n")
        counter = 0
        for word_array in sorted(filtered_data):
            print(word_array)
            counter += 1
        print("\n Number of word arrays in filtered data: ", counter)

    elif option == 3:
        # Prints each word and its classification features
        print("\n \n Each word and its classification features: \n")
        for word in sorted(classification_features):
            # Format and content: [word, isBold, isBig, isAbnormalColour, RAKE]
            print(word)

    elif option == 4:
        # F1 score from 0 to 1
        print("\n F1 score: ", performance)

def main():
    # Open a file here and apply a function from XML_parser to it
    path = interface_path()
    file_number = 0
    parsed_content = parse_file(path, file_number)

    # Pre-processing to filter out stopwords from parsed_files
    filtered_content = pre_processing(parsed_content)

    # Return a two-dimensional array which contains each word and its features
    classification_features = feature_assignment(filtered_content)

    # The return is 2D array which contains each word and its label
    clustered_data = kmeans_clustering(classification_features, CLUSTERS)

    # Post-processing to measure the performance of our classifier
    performance = post_processing(clustered_data)

    # Write to file
    path = "../output/foundation-year/CSC079/SlidesWeek2.txt"

    # Enables us to create paths from within the program
    os.makedirs(os.path.dirname(path), exist_ok=True)

    file = open(path, "w")

    for observation in clustered_data:
        file.write(str(observation) + "\n")

    file.close()

    while(True):
        interface_output(parsed_content, filtered_content,
                        classification_features, performance)

main()
