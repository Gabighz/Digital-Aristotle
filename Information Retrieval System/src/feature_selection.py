############################################################################################
# Selects desired features of words from XML data and represents each word as an array.    #
# This array contains the word itself as a string and its features as numerical values.    #
#                                                                                          #
# Each word is saved in the following format: [WordString, isBold, isBig, is unusualColour]#
#                                                                                          #
# Word String: String, represents the word                                                 #
# isBold: 1 or 0, 1 if the word is is bold                                                 #
# isBig: 1 or 0, 1 if the word is in a big font                                            #
# unusual_color: 1 or 0, 1 if the word font is not black                                   #
#                                                                                          #
############################################################################################

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
    biggest = max(font_sizes(raw_data))
    smallest =min(font_sizes(raw_data))

    word_list = []
    for entry in raw_data:
        word_list = add_words_to_list(entry[0], entry[2], word_list, entry[5], entry[6], biggest, smallest)
        #for each element in raw data.... addword()...
    return word_list

#adds each word in a sentence to the array
def add_words_to_list(words_string, isBold, word_list, font_size, color, biggest, smallest):
    isBold = isBold

    words = words_string.split()
    for w in words:
        global word_number
        word_number = word_number +1
        word_list.append([w, isBold, isBig(font_size, biggest,smallest), is_unusual_color(color)])
    return word_list

#this funtion simply checks if a colour is unusual or not, returns 1 if it is
#else 0. At the moment this function only counts anything that is not black as
#unusual.
def is_unusual_color(color):
    if color != "#000000":
        return 1
    else:
        return 0

#This is a utility fucntion that simply converts the font sizes in their raw_data
# into one font size array, this is used to make it easier to find the min
# and max font sizes.
def font_sizes(raw_data):
    sizes = []
    for entry in raw_data:
        sizes.append(entry[5])
    return sizes


#Determines if a word is big or note.
#Params: current-word checking, biggest-biggest font from document, smallest-
#        smallest font from document
#returns: 1 if is big, else 0
def isBig(current, biggest, smallest):

    #the smallest and biggest variables are taken from the document
    big = biggest
    small = smallest

    #this if statement converts the current word into a decimal point based
    #upon its font size in relation to the biggest and smallest, this point is
    #between 0 and one, anything over 0.5 is considered big.
    if ( ((current - small) / (big-small)) > 0.5  ):
        return 1
    else:
        return 0

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
