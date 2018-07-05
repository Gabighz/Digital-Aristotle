############################################################################################
# Selects desired features of words from XML data and represents each word as an array.    #
# This array contains the word itself as a string and its features as numerical values.    #
#                                                                                          #
# Each word is saved in the following format: [WordString, isBold, isBig, is unusualColour, RAKE]#
#                                                                                          #
# Word String: String, represents the word                                                 #
# isBold: 1 or 0, 1 if the word is is bold                                                 #
# isBig: 1 or 0, 1 if the word is in a big font                                            #
# unusual_color: 1 or 0, 1 if the word font is not black                                   #
# RAKE: the rake score                                                                     #
############################################################################################

from rake_nltk import Rake
import math

#word number created as a global variable for this version, will be changed
word_number = 0

# Constructs the word list
def feature_assignment(raw_data):
    selected_features = []
    selected_features = populate_word_list(raw_data);

    return selected_features

# Assigns the features for each word in the data and adds it to an array
def populate_word_list(raw_data):
    biggest = max(raw_data_slice(raw_data, 5))
    smallest =min(raw_data_slice(raw_data, 5))
    all_words = raw_data_slice(raw_data, 0)

    word_list = []
    used_words = []
    for entry in raw_data:
        word_list = add_words_to_list(entry[0], entry[1], entry[5], entry[6], biggest, smallest, used_words, word_list)
        #for each element in raw data.... addword()...

    word_list = assign_rake_ranking(all_words, word_list)
    return word_list

#adds each word in a sentence to the array
def add_words_to_list(words_string, isBold, font_size, color, biggest, smallest, used_words, word_list):
    isBold = isBold

    words = words_string.split()
    for w in words:
        global word_number
        word_number = word_number +1
        #word_list.append([w, isBold, isBig(font_size, biggest,smallest), is_unusual_color(color)])
        word_to_add = [w, isBold, isBig(font_size, biggest,smallest), is_unusual_color(color)]
        add_word(word_list, used_words, word_to_add)
    return word_list

def add_word(words_list, used_words, word_to_add):
    if word_to_add[0].lower() in used_words:
        notFound = True
        counter = 0
        while (notFound == True ) and( counter != len(used_words)-1) :
            counter +=1
            if(words_list[counter][0] == word_to_add[0] ):
                words_list[counter][1] = words_list[counter][1] + word_to_add[1]
                words_list[counter][2] = words_list[counter][2] + word_to_add[2]
                words_list[counter][3] = words_list[counter][3] + word_to_add[3]
                notFound = False
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
            if (entry[0] == raked[0]) &( done == 0) :
                entry.append(raked[1])
                done = 99
    return words_with_features


#this funtion simply checks if a colour is unusual or not, returns 1 if it is
#else 0. At the moment this function only counts anything that is not black as
#unusual.
def is_unusual_color(color):
    if color != "#000000":
        return 1
    else:
        return 0

#This is a utility fucntion that simply returns an array that is a slice of a
#2D array, for example it is used to return all of the font sizes from raw_data
def raw_data_slice(raw_data, row):
    sizes = []
    for entry in raw_data:
        sizes.append(entry[row])
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
def calculate_rake_ranking(selected_features):
    output_array = []

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

        array_item = [word_array, ranking]
        output_array.append(array_item)
        #word_array.append(ranking)

    return output_array
