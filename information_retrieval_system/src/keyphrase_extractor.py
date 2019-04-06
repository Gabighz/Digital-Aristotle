##################################################
# Main program which identifies and writes       #
# Keyphrases to a txt file based on XML files    #
# and the output of the keyword_extractor        #
#                                                #
# Author: Gabriel Ghiuzan                        #
##################################################

import numpy as np


# Creates an array of keywords given the output of the Keyword extractor
#
# @param path: The output path of the Keyword extractor
# @return keywords: An array which contains only the keywords
def keyword_output(filename):
    # Concatenates the name of the file to a pre-determined input path
    path = "../../keyword_extractor/output/first-year/CS-150/" + filename

    keyword_extractor_output = np.loadtxt(open(path), delimiter=',', dtype=object)
    print(keyword_extractor_output)
    keywords = keyword_extractor_output[keyword_extractor_output[:, 1] == "1", 0]

    return keywords


# This function requests user input of the name of a file as a string
#
# @return filename: The name of the file which will be processed
def input_path():
    filename = input("Input path: ../../keyword_extractor/output/first-year/CS-150/")

    return filename


def main():

    # Opens a file and applies a .txt reader to it. Can also handle the FileNotFoundError exception.
    while True:
        try:
            keywords = keyword_output(input_path())
            break
        except FileNotFoundError:
            print("File not found! Try again.")

    print(keywords)


main()
