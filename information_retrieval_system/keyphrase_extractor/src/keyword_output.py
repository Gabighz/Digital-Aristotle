##################################################
# Module which contains a function that stores   #
# keywords into an array, given the output of the#
# Keyword Extractor.                             #
#                                                #
# It is used as part of the input for the        #
# Keyphrase Extractor.                           #
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
