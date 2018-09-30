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
# Author: Slade Brooks & Gabriel Ghiuzan & Avi Varma                                                          #
###############################################################################################################

from rake_nltk import Rake
from sklearn.feature_selection import VarianceThreshold

# word number created as a global variable for this version, will be changed
WORD_NUMBER = 0

# The position of the word in the raw XML array
WORD_INDEX = 0


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
        for x in range(len(word) - 1):
            if x > 0 and word[x] > 0:
                word[x] = 1


# Assigns classification features for each word in the data and adds it to an array
#
# @param raw_data: A two-dimensional array which contains each word and its XML data
# @return classification_features: A two-dimensional array which contains each word and its features
def generate_classification_features(raw_data):

    # The position of the bold value in the raw XML array
    bold_index = 1

    # The position of the font size in the raw XML array
    font_size_index = 5

    # The position of the font size in the raw XML array
    colour_index = 6

    # The biggest and smallest size of the fonts recorded in the xml file
    biggest_font_size = max(raw_data_slice(raw_data, font_size_index))
    smallest_font_size = min(raw_data_slice(raw_data, font_size_index))

    # An array which contains only the words
    all_words = raw_data_slice(raw_data, WORD_INDEX)

    classification_features = []
    used_words = []
    for element in raw_data:
        classification_features = add_words_to_list(element[WORD_INDEX], element[bold_index], element[font_size_index],
                                                    element[colour_index], biggest_font_size, smallest_font_size,
                                                    used_words, classification_features)

    classification_features = assign_rake_ranking(all_words, classification_features)
    return classification_features


# Adds each word in a sentence to the array
#
# @param words: String that contains all the words in the XML array
# @param is_bold: Specifies the boldness of the word
# @param font_size: Specifies the font size of the word
# @param color: Specifies the hexadecimal value for the color of the word
# @param biggest_font_size : The biggest size of the fonts recorded in the xml file
# @param smallest_font_size: The smallest size of the fonts recorded in the xml file
# @param used_words: (?) no idea what this does yet (?)
# @return classification_features: A two-dimensional array which contains each word and its features
def add_words_to_list(words, is_bold, font_size, color, biggest_font_size, smallest_font_size,
                      used_words, classification_features):

    words = words.split()
    for word in words:
        global WORD_NUMBER
        WORD_NUMBER = WORD_NUMBER + 1
        # word_list.append([w, is_bold, is_larger(font_size, biggest,smallest), is_not_black(color)])
        word_to_add = [word, is_bold, is_larger(font_size, biggest_font_size, smallest_font_size),
                       is_not_black(color)]

        add_word(classification_features, used_words, word_to_add)
    return classification_features


# Adds each word and its classification features to an array.
#
# @param classification_features: A two-dimensional array which contains each word and its features
# @param used_words: (?) no idea what this does yet (?)
# @param word_to_add: (?) no idea what this does yet (?)
def add_word(classification_features, used_words, word_to_add):
    if word_to_add[WORD_INDEX].lower() in used_words:
        not_found = True
        counter = 0
        while not_found and (counter != len(used_words) - 1):
            if classification_features[counter][0] == word_to_add[0]:
                classification_features[counter][1] = classification_features[counter][1] + word_to_add[1]
                classification_features[counter][2] = classification_features[counter][2] + word_to_add[2]
                classification_features[counter][3] = classification_features[counter][3] + word_to_add[3]
                not_found = False
            counter += 1
    else:
        classification_features.append(word_to_add)
        used_words.append(word_to_add[0].lower())


# Assigns Rake ranking to each word.
#
# @param all_words: words from the XML file.
# @param words_with_features: Words from XML file that have been highlighted with different features to rest of text.
# @return words_with_features: Added the ranking to the array with the data on word features.
def assign_rake_ranking(all_words, words_with_features):
    pre_ranked_words = []

    for element in all_words:
        if ' ' in element:
            sentence = element.split(' ')
            for word in sentence:
                pre_ranked_words.append(word)
        else:
            pre_ranked_words.append(element)

    ranked_words = calculate_rake_ranking(pre_ranked_words)

    for element in words_with_features:

        done = False
        for word in ranked_words:
            if (element[0] == word[0]) and not done:
                element.append(word[1])
                done = True

    return words_with_features


# This function checks if a colour is unusual or not, returns 1 if true else 0.
# At the moment this function only counts anything that is not black as usual.
def is_not_black(color):
    if color != "#000000":
        return 1
    else:
        return 0


# This is a utility function that simply returns an array that is a slice of a
# 2D array, for example it is used to return all of the font sizes from raw_data
def raw_data_slice(raw_data, row):
    sizes = []

    for element in raw_data:
        sizes.append(element[row])
    return sizes


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
# @param classification_without_rake: A two-dimensional array which contains each word and its features,
#                                     but not RAKE yet
# @return classification_with_rake: A two-dimensional array which contains each word and all of its features,
#                                   including RAKE
def calculate_rake_ranking(classification_without_rake):

    # Meant to contain each word and its features, but with RAKE ranking not normalized
    rake_not_normalized = []
    
    # Will be the value returned by this function, containing each word and its features, with RAKE normalized
    classification_with_rake = []

    # Initializes the Rake object
    r = Rake()

    # Meant to contain each word in a string
    words_string = ''

    # Extracts only the word itself as a string
    for word_array in classification_without_rake:
        words_string += word_array[0] + " "

    # The Rake object ranks all the words in the string
    r.extract_keywords_from_text(words_string)

    # The return type of both functions called below is Dictionary (key -> value)
    frequency_distribution = r.get_word_frequency_distribution()  # word -> frequency (number of times it occurs)
    word_degrees = r.get_word_degrees()  # word -> degree (linguistic co-occurrence)

    # Appends the ranking to each word's array
    for word_array in classification_without_rake:

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
        classification_with_rake.append(rake_not_normalized[i])

    return classification_with_rake
