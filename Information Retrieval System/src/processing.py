##################################################
# Handles pre-processing (stopwords filtering)   #
# and post-processing (performance testing)      #
##################################################
from nltk.corpus import stopwords
from sklearn.metrics import f1_score

#this function removes all stop word entries from the raw data from the xml_parser
#def pre_processing(raw_data):
#    word_data_array = raw_data
#    array_counter = 0
#    stop_words = stop_words.words("english")
    #this loop runs through every word in the array of word data
#    for word_data in word_data_array:

        #the below variable and loop are for running through each stop word for a match
#        stop_word_counter = 0
#        while word_data[array_counter] != stop_word
#            stop_word = stop_words[stop_word_counter]
#            if word_data[array_counter] == stop_word:
#                del word_data_array[array_counter]
#            stop_word_counter +=1
#        array_counter += 1
#        return word_data_array

# Computes the F1-score of our classifier
# Takes in a 2D array which contains each observation and their label
# Compares that to the ground truth (correct) value of each observation
def post_processing(results):

    # Contains manually annoted ground truth values
    true_output = []
    true_output = manual_annotation(true_output)

    # Contains the estimated targets returned by the classifier
    estimated_targets = []

    for i in range(len(results)):
        estimated_targets.append(results[i][1])

    return f1_score(true_output, estimated_targets, average='binary')

# Only for the SlidesWeek2 file at the moment
def manual_annotation(true_output):

    for i in range(1, 158):
        true_output.append(0)

    for i in range(158, 163):
        true_output.append(1)

    for i in range(163, 182):
        true_output.append(0)

    true_output.append(1)

    for i in range(183, 190):
        true_output.append(0)

    true_output.append(1)
    true_output.append(0)
    true_output.append(0)
    true_output.append(1)

    for i in range(193, 199):
        true_output.append(0)

    true_output.append(1)
    true_output.append(0)
    true_output.append(0)
    true_output.append(1)

    for i in range(203, 212):
        true_output.append(0)

    true_output.append(1)

    for i in range(213, 226):
        true_output.append(0)

    true_output.append(1)

    for i in range(227, 232):
        true_output.append(0)

    true_output.append(1)
    true_output.append(0)
    true_output.append(1)

    for i in range(235, 254):
        true_output.append(0)

    true_output.append(1)
    true_output.append(1)

    for i in range(256, 265):
        true_output.append(0)

    true_output.append(1)

    for i in range(266, 272):
        true_output.append(0)

    true_output.append(1)

    for i in range(273, 288):
        true_output.append(0)

    true_output.append(1)
    true_output.append(1)
    true_output.append(0)
    true_output.append(1)
    true_output.append(1)

    for i in range(293, 304):
        true_output.append(0)

    true_output.append(1)

    for i in range(305, 319):
        true_output.append(0)

    true_output.append(1)
    true_output.append(1)

    for i in range(321, 327):
        true_output.append(0)

    true_output.append(1)
    true_output.append(0)
    true_output.append(0)
    true_output.append(1)

    for i in range(331, 346):
        true_output.append(0)

    true_output.append(1)

    for i in range(347, 367):
        true_output.append(0)

    true_output.append(1)

    for i in range(368, 408):
        true_output.append(0)

    true_output.append(1)

    for i in range(409, 430):
        true_output.append(0)

    true_output.append(1)
    true_output.append(1)
    true_output.append(0)
    true_output.append(0)

    for i in range(434, 439):
        true_output.append(1)

    for i in range(439, 454):
        true_output.append(0)

    for i in range(454, 457):
        true_output.append(1)

    for i in range(457, 495):
        true_output.append(0)

    true_output.append(1)

    for i in range(496, 546):
        true_output.append(0)

    true_output.append(1)

    for i in range(547, 584):
        true_output.append(0)

    true_output.append(1)

    for i in range(585, 599):
        true_output.append(0)

    true_output.append(1)

    for i in range(600, 605):
        true_output.append(0)

    true_output.append(1)

    for i in range(606, 617):
        true_output.append(0)

    true_output.append(1)

    for i in range(618, 625):
        true_output.append(0)

    return true_output
