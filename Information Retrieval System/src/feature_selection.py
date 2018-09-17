###############################################################################################################
# Selects desired features of words from XML data and represents each word as an array.                       #
# This array contains the word itself as a string and its features as numerical values.                       #
#                                                                                                             #
# Each word is stored in a 2D array as the following: [word, is_bold, is_larger, is unusualColour, RAKE]      #
#                                                                                                             #
# word: A String which represents the word                                                                    #
# is_bold: A Boolean value to see if it is bold                                                               #
# is_larger: A Boolean value to see if it is a larger font                                                    #
# is_not_black: A Boolean value to see if it is not black                                                     #
# RAKE: The RAKE ranking                                                                                      #
#                                                                                                             #
# Author: Slade Brooks & Gabriel Ghiuzan                                                                      #
###############################################################################################################

from rake_nltk import Rake
from sklearn.feature_selection import VarianceThreshold

# word number created as a global variable for this version, will be changed
WORD_NUMBER = 0


# Constructs the word list
def feature_assignment(raw_data):
    selected_features = populate_word_list(raw_data)

    normalise_features(selected_features)
    variance_threshold(selected_features)

    return selected_features


# Removes all zero-variance features, i.e. features that have the same value in all samples
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


# Normalising approach of [word,6,3,0] becomes [word,1,1,0]
def normalise_features(classification_features):

    for word in classification_features:
        for x in range(len(word) - 1):
            if x > 0 and word[x] > 0:
                word[x] = 1


# Assigns the features for each word in the data and adds it to an array
def populate_word_list(raw_data):
    biggest = max(raw_data_slice(raw_data, 5))
    smallest = min(raw_data_slice(raw_data, 5))
    all_words = raw_data_slice(raw_data, 0)

    word_list = []
    used_words = []
    for entry in raw_data:
        word_list = add_words_to_list(entry[0], entry[1], entry[5], entry[6], biggest, smallest, used_words, word_list)
        # for each element in raw data.... addword()...

    word_list = assign_rake_ranking(all_words, word_list)
    return word_list


# adds each word in a sentence to the array
def add_words_to_list(words_string, is_bold, font_size, color, biggest, smallest, used_words, word_list):
    is_bold = is_bold

    words = words_string.split()
    for w in words:
        global WORD_NUMBER
        WORD_NUMBER = WORD_NUMBER + 1
        # word_list.append([w, is_bold, is_larger(font_size, biggest,smallest), is_unusual_color(color)])
        word_to_add = [w, is_bold, is_larger(font_size, biggest, smallest), is_unusual_color(color)]
        add_word(word_list, used_words, word_to_add)
    return word_list


def add_word(words_list, used_words, word_to_add):
    if word_to_add[0].lower() in used_words:
        not_found = True
        counter = 0
        while (not_found == True) and (counter != len(used_words) - 1):
            counter += 1
            if words_list[counter][0] == word_to_add[0]:
                words_list[counter][1] = words_list[counter][1] + word_to_add[1]
                words_list[counter][2] = words_list[counter][2] + word_to_add[2]
                words_list[counter][3] = words_list[counter][3] + word_to_add[3]
                not_found = False
    else:
        words_list.append(word_to_add)
        used_words.append(word_to_add[0].lower())


def assign_rake_ranking(all_words, words_with_features):
    pre_raked_data = []
    for elem in all_words:
        if ' ' in elem:
            sentence = elem.split(' ')
            for word in sentence:
                pre_raked_data.append(word)
        else:
            pre_raked_data.append(elem)
    raked_data = calculate_rake_ranking(pre_raked_data)

    for entry in words_with_features:
        done = 0
        for raked in raked_data:
            if (entry[0] == raked[0]) & (done == 0):
                entry.append(raked[1])
                done = 99
    return words_with_features


# This function checks if a colour is unusual or not, returns 1 if true else 0.
# At the moment this function only counts anything that is not black as usual.
def is_unusual_color(color):
    if color != "#000000":
        return 1
    else:
        return 0


# This is a utility function that simply returns an array that is a slice of a
# 2D array, for example it is used to return all of the font sizes from raw_data
def raw_data_slice(raw_data, row):
    sizes = []
    for entry in raw_data:
        sizes.append(entry[row])
    return sizes


# Determines if a word is big or note.
# Params: current-word checking, biggest-biggest font from document, smallest-
#        smallest font from document
# returns: 1 if is big, else 0
def is_larger(current, biggest, smallest):
    # the smallest and biggest variables are taken from the document
    big = biggest
    small = smallest

    # this if statement converts the current word into a decimal point based
    # upon its font size in relation to the biggest and smallest, this point is
    # between 0 and one, anything over 0.5 is considered big.
    if ((current - small) / (big - small)) > 0.5:
        return 1
    else:
        return 0


# Assigns RAKE ranking to each word and appends the ranking to the end of
# each word's array, using degree(word)/frequency(word) as the metric
def calculate_rake_ranking(selected_features):
    unnormalized_array = []
    output_array = []

    r = Rake()

    # Contains all the words in the document
    words_string = ''

    # Extracts only the word itself as a string
    for word_array in selected_features:
        words_string += word_array[0] + " "

    r.extract_keywords_from_text(words_string)

    # The return type of both functions called below is Dictionary (key -> value)
    frequency_distribution = r.get_word_frequency_distribution()  # word -> frequency (number of times it occurs)
    word_degrees = r.get_word_degrees()  # word -> degree (linguistic co-occurrence)

    # Appends the ranking to each word's array
    for word_array in selected_features:

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

        array_item = [word_array, ranking]
        unnormalized_array.append(array_item)

    # Gets the maximum ranking
    maximum_ranking = 0
    for word_array in unnormalized_array:
        if word_array[1] > maximum_ranking:
            maximum_ranking = word_array[1]

    # Normalizes the value of the ranking to [0, 2]
    for i in range(len(unnormalized_array)):
        ranking = unnormalized_array[i][1]
        # Normalizes to [0, 1]
        unscaled_ranking = ranking / maximum_ranking
        # Scales to [0, 2]
        unnormalized_array[i][1] = round(unscaled_ranking * 2, 5)
        output_array.append(unnormalized_array[i])

    return output_array
