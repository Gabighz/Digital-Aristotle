##################################################
# Handles pre-processing (stopwords filtering)   #
# and post-processing (performance testing)      #
##################################################
from nltk.corpus import stopwords
from sklearn.metrics import f1_score


#this function removes all stop word entries from the raw data from the xml_parser
def remove_stop_words(sentence):
    word_array = sentence.split()
    stop_words = stopwords.words("english")
    clean_string = ""
    for word in word_array:
        for stop_word in stop_words:
            if word == stop_word:
                word_array.remove(stop_word)
    for word in word_array:
        if clean_string == "":
            clean_string = clean_string + word
        else:
            clean_string = clean_string + " " + word

    return clean_string

def pre_processing(raw_data):
    sentence_array = raw_data
    array_counter = 0
    for sentence in sentence_array:
        sentence[0] = remove_stop_words(sentence[0])
        if remove_stop_words(sentence[0]) ==  "":
            del sentence_array[array_counter]
        elif remove_stop_words(sentence[0]) == " ":
            del sentence_array[array_counter]
        else:
            array_counter += 1

    return sentence_array



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
