##################################################
# Main program which identifies and writes       #
# Keywords and Non-keywords to a txt file        #
#                                                #
# Author: Gabriel Ghiuzan                        #
##################################################
import os

from xml_parser import parse_file
from feature_selection import feature_assignment
from kmeans import kmeans_clustering
from processing import pre_processing, post_processing

# This constant is used in kmeans.py. It determines the number of classifications.
# Currently, we have 2 classifications: Keywords and Non-keywords.
CLUSTERS = 2


# This function requests user input of the name of a file as a string
#
# @return filename: The name of the file which will be processed
def interface_path():
    filename = input("Input path: ../../Input files/first-year/CS-150/")

    return filename


def main():
    # Opens a file and applies an XML parser to it. Can also handle the FileNotFoundError exception.
    while True:
        try:
            # Gets the name of the file from the user
            filename = interface_path()

            # Concatenates the name of the file to a pre-determined input path
            path = "../../Input files/first-year/CS-150/" + filename

            # The number of files to be processed (currently, we process only one file at a time)
            file_number = 0

            # An array which contains a phrase or a word and its corresponding XML data
            parsed_content = parse_file(path, file_number)

            break
        except FileNotFoundError:
            print("File not found! Try again.")

    # Pre-processing to filter out unwanted data from parsed_content
    filtered_content = pre_processing(parsed_content)

    # A two-dimensional array which contains each word and its features
    classification_features = feature_assignment(filtered_content)

    # Prints each word and its classification features and the number of all words in classification_features
    counter = 0
    print("\n \n Each word and its classification features: \n")
    for word in sorted(classification_features):
        # Format: [word, is_bold, is_larger, is_not_black, RAKE]
        print(word)
        counter += 1

    print("\n Number of words in classification_features: ", counter)

    # A 2D array which contains each word and its label
    # For example, [word, 0] or [word, 1], which means [word, Non-keyword] or [word, Keyword]
    classified_words = kmeans_clustering(classification_features, CLUSTERS)

    # Post-processing to measure the performance of our keyword extractor
    performance = post_processing(classified_words, filename)

    # F1 score, from 0 to 1
    print("\n F1 score: ", performance)

    # Creates and array in which the first index is the name of the file
    # and the second index is the extension of the file (typically 'xml')
    filename_and_extension = filename.split('.')

    # Takes only the name of the file and adds the .txt extension
    output_filename = filename_and_extension[0] + '.txt'

    # Stores the path of the file which will contain the classified words
    output_path = "../output/first-year/CS-150/" + output_filename

    # Enables us to create directories from within the program
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    output_file = open(output_path, "w")

    for word_with_label in classified_words:
        output_file.write(str(word_with_label) + "\n")

    output_file.close()


main()
