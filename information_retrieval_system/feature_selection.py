#
# Selects desired features of words from XML data and represents each word as an array.
# This array contains the word itself as a string and its features as numerical values.
#
# Each word is stored in a 2D array as the following: [word, is_bold, is_larger, is_not_black, RAKE]
#
# word: A String which represents the word
# is_bold: A Boolean value to see if it is bold
# is_larger: A Boolean value to see if it is a larger font
# is_not_black: A Boolean value to see if it is not black
# RAKE: The RAKE ranking
#
# Author: Gabriel Ghiuzan & Avi Varma
#

import numpy as np
from rake_nltk import Rake
from sklearn.preprocessing import MinMaxScaler

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

    return classification_features


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
    # Converts raw_data to a numpy array
    raw_data = np.array(raw_data, dtype=object)

    # Will contain each word and its classification features
    classification_features = []

    # Finds the biggest font size in the XML array
    biggest_font_size = int(max(raw_data[:, FONT_SIZE_INDEX]))

    # Finds the smallest font size in the XML array
    smallest_font_size = int(min(raw_data[:, FONT_SIZE_INDEX]))

    # Contains each word and its XML attributes
    words = split_sentences_into_words(raw_data)

    for array in words:
        classification_features.append([array[WORD_INDEX], array[BOLD_INDEX],
                                       is_larger(array[FONT_SIZE_INDEX], biggest_font_size, smallest_font_size),
                                       is_not_black(array[COLOUR_INDEX])])

    # Converts words to a numpy array
    words = np.array(words, dtype=object)

    # Contains only the words
    just_words = words[:, WORD_INDEX]

    # A list which contains each RAKE ranking
    rankings = calculate_rake_ranking(just_words)

    # Appends the RAKE ranking
    for classification_sublist, ranking in zip(classification_features, rankings):
        classification_sublist.append(ranking)

    return classification_features


# Some arrays contain sentences instead of individual words. These are split and appended in their own separate array
# while maintaining their XML attributes.
#
# @param raw_data: A two-dimensional array which contains each word and its XML data
# @return words: A two-dimensional array which contains each word and its XML attributes
def split_sentences_into_words(raw_data):
    # Will contain individual words and their corresponding XML attributes
    words = []

    for array in raw_data:
        # Will be used to check if the string is a sentence or a word
        is_sentence = False

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
# @param just_words: A list which contains just words
# @return rake_scaled: A list which contains each RAKE ranking
def calculate_rake_ranking(just_words):

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

    # Meant to contain RAKE ranking which aren't scaled yet
    rake_not_scaled = []

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

        rake_not_scaled.append(ranking)

    # Scales the values of the RAKE rankings to [0, 2]
    scaler = MinMaxScaler(feature_range=(0, 2))
    rake_scaled = scaler.fit_transform(np.asarray(rake_not_scaled).reshape(-1, 1))
    rake_scaled = [float(ranking) for ranking in rake_scaled]

    return rake_scaled
