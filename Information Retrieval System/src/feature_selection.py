#########################################################################################
# Selects desired features of words from XML data and represents each word as an array. #
# This array contains the word itself as a string and its features as numerical values. #
#########################################################################################

from rake_nltk import Rake
import math

#word number created as a global variable for this version, will be changed
word_number = 0

# Constructs the word list
def feature_assignment(raw_data):
    selected_features = []
    selected_features = populate_word_list(raw_data);
    # Call a method here on selected_features for the other feature

    complete_features = assign_rake_ranking(selected_features)

    return complete_features

#assigns the features for each word in the data and adds it to an array
def populate_word_list(raw_data):

    word_list = []
    for e in raw_data:
        word_list = add_words_to_list(e[0], e[2], word_list)
        #for each element in raw data.... addword()...
    return word_list

#adds each word in a sentence to the array
def add_words_to_list(words_string, isBold, word_list):
    isBold = isBold


    words = words_string.split()
    for w in words:
        global word_number
        word_number = word_number +1
        word_list.append([w, isBold])
    return word_list

# Assigns RAKE ranking to each word and appends the ranking to the end of
# each word's array, using degree(word)/frequency(word) as the metric
def assign_rake_ranking(selected_features):

    r = Rake()

    # Contains all the words in the document
    words_string = ''

    # Extracts only the word itself as a string
    for word_array in selected_features:

        words_string += word_array[0] + " "

    r.extract_keywords_from_text(words_string)

    # The return type of both functions called below is Dictionary (key -> value)
    frequency_distribution = r.get_word_frequency_distribution() # word -> frequency (number of times it occurs)
    word_degrees= r.get_word_degrees() # word -> degree (linguistic co-occurance)



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

        ranking = word_degree / word_frequency # in accordance with the chosen metric

        word_array.append(ranking)

    return selected_features



#converts the word into a unique number
#def get_word_data(word):
#    return int.from_bytes(word.encode(), 'little')
#    return word
