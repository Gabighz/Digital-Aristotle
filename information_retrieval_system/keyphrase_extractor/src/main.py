##################################################
# Main program which identifies and writes       #
# Keyphrases to a txt file based on XML files    #
# and the output of the keyword_extractor        #
#                                                #
# Author: Gabriel Ghiuzan                        #
##################################################

from keyword_output import keyword_output
from input_path import input_path


def main():

    while True:
        try:
            keywords = keyword_output(input_path())
            break
        except FileNotFoundError:
            print("File not found! Try again.")

    print(keywords)


main()
