#########################################################################################
# Selects desired features of words from XML data and represents each word as an array. #
# This array contains the word itself as a string and its features as numerical values. #
#########################################################################################

import RAKE
import math

#word number created as a global variable for this version, will be changed
word_number = 0

#this method might be redundant but constructs the word list
def feature_selection(raw_data):
    selected_features = []
    selected_features = populate_word_list(raw_data);

    complete_features = assign_rake_ranking(selected_features)
    return complete_features

#assigns the features for each word in the data and adds it to an array
def populate_word_list(raw_data):

    word_list = []
    for e in raw_data:
        word_list = add_words_to_list(e[0], e[1], e[2], e[3], e[4], e[5], word_list)
        #for each element in raw data.... addword()...
    return word_list

#adds each word in a sentence to the array
def add_words_to_list(words_string, attributes, isBold, documentNumber, pageNumber, sentenceNumber, word_list):
    isBold = isBold
    documentNumber = documentNumber
    pageNumber = pageNumber
    sentenceNumber = sentenceNumber

    top = int(attributes['top'])
    left = int(attributes['left'])
    width = int(attributes['width'])
    height = int(attributes['height'])
    fontSize = int(attributes['font'])

    words = words_string.split()
    for w in words:
        global word_number
        word_number = word_number +1
        word_list.append([w, documentNumber,pageNumber,sentenceNumber,word_number,
        top,left,width,height,fontSize])
    return word_list

# Assigns RAKE ranking to each word and appends the ranking to the end of
# each word's array
def assign_rake_ranking(selected_features):

    Rake = RAKE.Rake(["a"]) # !! needs stopwords as list of strings


    # Contains all the words in the document
    words_string = ''

    for array in selected_features:

        words_string += array[0] + " "

    rake_ranking = Rake.run(words_string)

    print(rake_ranking)


#converts the word into a unique number
#def get_word_data(word):
#    return int.from_bytes(word.encode(), 'little')
#    return word
