##################################################
# Handles pre-processing (stopwords filtering)   #
# and post-processing (performance testing)      #
##################################################
from nltk.corpus import stopwords

#this function removes all stop word entries from the raw data from the xml_parser
def pre_processing(raw_data):
    word_data_array = raw_data
    array_counter = 0
    stop_words = stop_words.words("english")
    #this loop runs through every word in the array of word data
    for word_data in word_data_array:

        #the below variable and loop are for running through each stop word for a match
        stop_word_counter = 0
        while word_data[array_counter] != stop_word
            stop_word = stop_words[stop_word_counter]
            if word_data[array_counter] == stop_word:
                del word_data_array[array_counter]
            stop_word_counter +=1
        array_counter += 1
        return word_data_array

def post_processing():
