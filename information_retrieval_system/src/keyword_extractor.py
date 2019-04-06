#
# Module which identifies and outputs Keywords
#
# Author: Gabriel Ghiuzan
#

from xml_parser import parse_xml
from feature_selection import feature_assignment
from kmeans import kmeans_clustering
from processing import pre_processing, post_processing

# This constant is used in kmeans.py. It determines the number of classifications.
# Currently, we have 2 classifications: Keywords and Non-keywords.
CLUSTERS = 2


# This function requests user input of the name of a file as a string
#
# @return filename: The name of the file which will be processed
def input_path():
    filename = input("Input path: ../../input/first-year/CS-150/")

    return filename


def keyword_extractor():
    # Opens a file and applies an XML parser to it. Can also handle the FileNotFoundError exception.
    while True:
        try:
            # Gets the name of the file from the user
            filename = input_path()

            # Concatenates the name of the file to a pre-determined input path
            path = "../input/first-year/CS-150/" + filename + ".xml"

            # An array which contains a phrase or a word and its corresponding XML data
            parsed_xml = parse_xml(path)

            break
        except FileNotFoundError:
            print("File not found! Try again.")

    # Prints the raw XML data
    counter = 0
    print("\n Raw XML Data: \n")
    for word_array in parsed_xml:
        print(word_array)
        counter += 1
    print("\n Number of word arrays in raw XML data: ", counter)

    # Pre-processing to filter out unwanted data from parsed_content
    filtered_content = pre_processing(parsed_xml)

    # Prints the filtered data so we can check if the pre-processor is working correctly
    print("\n Filtered data (each word with its own XML features): \n")
    counter = 0
    for word_array in filtered_content:
        print(word_array)
        counter += 1
    print("\n Number of word arrays in filtered data: ", counter)

    # A two-dimensional array which contains each word and its features
    classification_features = feature_assignment(filtered_content)

    # Prints each word and its classification features and the number of all words in classification_features
    counter = 0
    print("\n \n Each word and its classification features: \n")
    for word in classification_features:
        # Format: [word, is_bold, is_larger, is_not_black, RAKE]
        print(word)
        counter += 1

    print("\n Number of words in classification_features: ", counter)

    # Runs the k-means algorithm 10 times, a number chosen arbitrarily.
    # The cost function of this algorithm converges towards local minima, not guaranteed to find
    # the global minimum. Thus, several restarts are needed.
    runs = []
    for n in range(10):
        # A 2D array which contains each word and its label
        # For example, [word, 0] or [word, 1], which means [word, Non-keyword] or [word, Keyword]
        classified_words = kmeans_clustering(classification_features, CLUSTERS)

        # Post-processing to measure the performance of our keyword extractor
        performance = post_processing(classified_words, filename)

        runs.append([classified_words, performance])

    # The highest performing classification is extracted.
    classified_words, max_performance = max(runs, key=lambda array: array[1])

    # F1 score, from 0 to 1
    print("\n F1 score: ", max_performance)
