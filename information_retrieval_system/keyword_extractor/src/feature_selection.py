###############################################################################################################
# Selects desired features of words from XML data and represents each word as an array.                       #
# This array contains the word itself as a string and its features as numerical values.                       #
#                                                                                                             #
# Each word is stored in a 2D array as the following: [word, is_bold, is_larger, is_not_black, RAKE]          #
#                                                                                                             #
# word: A String which represents the word                                                                    #
# is_bold: A Boolean value to see if it is bold                                                               #
# is_larger: A Boolean value to see if it is a larger font                                                    #
# is_not_black: A Boolean value to see if it is not black                                                     #
# RAKE: The RAKE ranking                                                                                      #
#                                                                                                             #
# Author: Gabriel Ghiuzan, Avi Varma & Slade Brooks                                                           #
###############################################################################################################

import numpy as np
from rake_nltk import Rake
from sklearn.feature_selection import VarianceThreshold

# The position of the word in the raw XML array
WORD_INDEX = 0

# The position of the bold value in the raw XML array
BOLD_INDEX = 1

# The position of the font size in the raw XML array
FONT_SIZE_INDEX = 2

# The position of the font size in the raw XML array
COLOUR_INDEX = 3


# Constructs the word list using the raw data which has been normalised, then set is filtered down to the values
# within the variance threshold.
#
# @param raw_data: Files that have been pre-processed and outputted into an XML format.
# @return classification_features: Outputs the filtered array.
def feature_assignment(raw_data):
    classification_features = generate_classification_features(raw_data)

    normalise_features(classification_features)
    variance_threshold(classification_features)

    return classification_features


# Removes all zero-variance features, i.e. features that have the same value in all samples
#
# @param classification_features: A two-dimensional array which contains each word and its features
def variance_threshold(classification_features):

    # Makes a copy of the array which contains each word and its classification features
    features = classification_features

    # Array which will only contain each word
    word_array = []

    # Removes the string of each array, e.g. ["word", 0, 1, 1, 1] becomes [0, 1, 1, 1]
    # since this features selection algorithm does not work with arrays that contain strings
    for array in features:
        word_array.append(array[0])
        del array[0]

    selection_algorithm = VarianceThreshold()

    selection_algorithm.fit_transform(features)

    # Puts the corresponding word of each array back in
    index = 0
    for array in features:
        array.insert(0, word_array[index])
        index += 1


# Instead of summing up the instances in which a feature appears, a boolean value is used.
# For example, [word, 4, 3, 0, 1] becomes [word, 1, 1, 0, 1]
#
# @param classification_features: A two-dimensional array which contains each word and its features
def normalise_features(classification_features):

    for word in classification_features:
        # Range stops at the length of the array minus one as not to include RAKE in the below computation
        for index in range(len(word) - 1):
            if index > WORD_INDEX and word[index] > 0:
                word[index] = 1


# Assigns classification features for each word in the data and adds it to an array
#
# @param raw_data: A two-dimensional array which contains each word and its XML data
# @return classification_features: A two-dimensional array which contains each word and its classification features
def generate_classification_features(raw_data):

    # Will contain each word and its classification features
    classification_features = []

    # Finds the biggest font size in the XML array
    biggest_font_size = int(max([font_size for (array_index, font_size_index), font_size in np.ndenumerate(raw_data)
                            if font_size_index == FONT_SIZE_INDEX]))

    # Finds the smallest font size in the XML array
    smallest_font_size = int(min([font_size for (array_index, font_size_index), font_size in np.ndenumerate(raw_data)
                             if font_size_index == FONT_SIZE_INDEX]))

    # Contains each word and its XML attributes
    words = split_sentences_into_words(raw_data)

    for array in words:
        classification_features.append([array[WORD_INDEX], array[BOLD_INDEX],
                                       is_larger(array[FONT_SIZE_INDEX], biggest_font_size, smallest_font_size),
                                       is_not_black(array[COLOUR_INDEX])])

    # Contains only the words
    just_words = [word for (array_index, word_index), word in np.ndenumerate(words) if word_index == WORD_INDEX]

    # A two-dimensional array which contains each word and its RAKE ranking
    words_with_ranking = calculate_rake_ranking(just_words)

    # Appends the RAKE ranking
    for word_array in classification_features:

        found = False
        for ranked_array in words_with_ranking:

            if word_array[WORD_INDEX] == ranked_array[WORD_INDEX] and not found:
                word_array.append(ranked_array[1])
                found = True

    return classification_features


# Some arrays contain sentences instead of individual words. These are split and appended in their own separate array
# while maintaining their XML attributes.
#
# @param raw_data: A two-dimensional array which contains each word and its XML data
# @return words: A two-dimensional array which contains each word and its XML attributes
def split_sentences_into_words(raw_data):
    # Will contain individual words and their corresponding XML attributes
    words = []

    # Will be used to check if the string is a sentence or a word
    is_sentence = False
    for array in raw_data:

        # If the string contains a space, it is treated as a sentence
        for character in array[WORD_INDEX]:
            if character == " ":
                is_sentence = True

        # If the array contains a string which is a sentence, the string is split into words.
        # Then, each word is appended to the words array.
        # Else, it is directly appended.
        if is_sentence:
            sentence = array[WORD_INDEX].split(" ")

            for element in sentence:
                words.append([element, array[BOLD_INDEX], array[FONT_SIZE_INDEX], array[COLOUR_INDEX]])

        else:
            words.append([array[WORD_INDEX], array[BOLD_INDEX], array[FONT_SIZE_INDEX], array[COLOUR_INDEX]])

    return words


# This function checks if a colour is unusual or not, returns 1 if true else 0.
# At the moment this function only counts anything that is not black as usual.
def is_not_black(color):
    if color != "#000000":
        return 1
    else:
        return 0


# Determines whether the word is larger than the average font size
#
# @param current_font_size: The font size of the word being currently considered
# @param biggest_font_size: The biggest size of the fonts recorded in the xml file
# @param smallest_font_size: The smallest size of the fonts recorded in the xml file
# @return: A boolean value of 1 or 0
def is_larger(current_font_size, biggest_font_size, smallest_font_size):

    # Maximum difference in value before font is considered larger than average.
    font_size_fence = 0.5

    # Checks whether the word is larger than the average font size
    if ((current_font_size - smallest_font_size) / (biggest_font_size - smallest_font_size)) > font_size_fence:
        return 1
    else:
        return 0


# Assigns RAKE ranking to each word and appends the ranking to the end of
# each word's array, using degree(word)/frequency(word) as the metric
#
# @param just_words: An array which contains just words
# @return words_with_rake: A two-dimensional array which contains each word and its RAKE ranking
def calculate_rake_ranking(just_words):
    # Meant to contain each word and its features, but with RAKE ranking not normalized
    rake_not_normalized = []

    # Will be the value returned by this function, containing each word and its features, with RAKE normalized
    words_with_rake = []

    # Initializes the Rake object
    r = Rake()

    # Meant to contain each word in a string
    words_string = ''

    # Extracts only the word itself as a string
    for word_array in just_words:
        words_string += word_array[0] + " "

    # The Rake object ranks all the words in the string
    r.extract_keywords_from_text(words_string)

    # The return type of both functions called below is Dictionary (key -> value)
    frequency_distribution = r.get_word_frequency_distribution()  # word -> frequency (number of times it occurs)
    word_degrees = r.get_word_degrees()  # word -> degree (linguistic co-occurrence)

    # Appends the ranking to each word's array
    for word_array in just_words:

        word_frequency = 1
        word_degree = 1

        # Linear search to match a word to its frequency
        for word, value in frequency_distribution.items():

            if word_array[0] == word:
                word_frequency = value

        # Linear search to match a word to its degree
        for word, value in word_degrees.items():

            if word_array[0] == word:
                word_degree = value

        # Formula in accordance with the chosen metric
        ranking = word_degree / word_frequency

        # Contains the array of a word and its features and the word's RAKE ranking
        array_item = [word_array, ranking]

        rake_not_normalized.append(array_item)

    # Gets the maximum ranking out of all the words
    maximum_ranking = 0
    for word_array in rake_not_normalized:

        if word_array[1] > maximum_ranking:
            # If there is a score higher than the one previously found, maximum_ranking is replaced with it
            maximum_ranking = word_array[1]

    # Normalizes the value of the ranking to [0, 2]
    for i in range(len(rake_not_normalized)):
        ranking = rake_not_normalized[i][1]

        # Normalizes to [0, 1]
        unscaled_ranking = ranking / maximum_ranking

        # Scales to [0, 2]
        rake_not_normalized[i][1] = round(unscaled_ranking * 2, 5)

        # Appends the array of each word and its features, with RAKE normalized to between 0 and 2 inclusive
        words_with_rake.append(rake_not_normalized[i])

    return words_with_rake
