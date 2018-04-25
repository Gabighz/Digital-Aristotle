##################################################
# Handles pre-processing (stopwords filtering)   #
# and post-processing (performance testing)      #
##################################################

import re

from nltk.corpus import stopwords
from sklearn.metrics import f1_score


#this function removes all stop word entries from the raw data from the xml_parser
def remove_stop_words(sentence):
    word_array = sentence.split()

    # Converts all words to lowercase; e.g. so Sensors and sensors are not
    # considered different words
    word_array = [word.lower() for word in word_array]

    stop_words = stopwords.words("english")

    # Added additional stopwords
    stop_words.extend(["a", "the", "th", "your"])

    # Filters out stopwords from the array of words and concatenates them to a string
    filtered_string = ' '.join([word for word in word_array if word not in stop_words])

    # Cleans each word of non-alphanumeric characters
    # e.g. so 'sensors)' and 'sensors' are not considered different words
    filtered_string = re.sub("[^a-zA-Z]"," ", filtered_string)

    return filtered_string

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

    return f1_score(true_output, estimated_targets)

# Only for the SlidesWeek2 file at the moment
def manual_annotation(true_output):

    for i in range(1, 132):
        true_output.append(0)

    true_output.append(1)
    true_output.append(1)
    true_output.append(0)
    true_output.append(1)
    true_output.append(1)
    true_output.append(1)
    true_output.append(1)

    for i in range(139, 153):
        true_output.append(0)

    true_output.append(1)
    true_output.append(1)

    for i in range(155, 160):
        true_output.append(0)

    true_output.append(1)
    true_output.append(0)
    true_output.append(1)

    for i in range(163, 166):
        true_output.append(0)

    true_output.append(1)
    true_output.append(0)
    true_output.append(1)

    for i in range(169, 174):
        true_output.append(0)

    true_output.append(1)

    for i in range(175, 187):
        true_output.append(0)

    true_output.append(1)
    true_output.append(0)
    true_output.append(0)
    true_output.append(1)
    true_output.append(0)
    true_output.append(1)

    for i in range(193, 206):
        true_output.append(0)

    true_output.append(1)
    true_output.append(1)

    for i in range(208, 214):
        true_output.append(0)

    true_output.append(1)

    for i in range(215, 218):
        true_output.append(0)

    true_output.append(1)

    for i in range(219, 232):
        true_output.append(0)

    true_output.append(1)
    true_output.append(1)
    true_output.append(0)
    true_output.append(1)
    true_output.append(1)

    for i in range(237, 243):
        true_output.append(0)

    true_output.append(1)

    for i in range(244, 249):
        true_output.append(0)

    true_output.append(1)

    for i in range(250, 256):
        true_output.append(0)

    true_output.append(1)

    for i in range(257, 262):
        true_output.append(0)

    true_output.append(1)
    true_output.append(0)
    true_output.append(1)

    for i in range(265, 275):
        true_output.append(0)

    true_output.append(1)

    for i in range(276, 293):
        true_output.append(0)

    true_output.append(1)

    for i in range(294, 326):
        true_output.append(0)

    true_output.append(1)

    for i in range(327, 344):
        true_output.append(0)

    true_output.append(1)
    true_output.append(1)
    true_output.append(0)
    true_output.append(0)
    true_output.append(1)
    true_output.append(1)
    true_output.append(1)

    for i in range(351, 362):
        true_output.append(0)

    true_output.append(1)
    true_output.append(1)
    true_output.append(1)

    for i in range(365, 392):
        true_output.append(0)

    true_output.append(1)

    for i in range(393, 429):
        true_output.append(0)

    true_output.append(1)

    for i in range(430, 460):
        true_output.append(0)

    true_output.append(1)

    for i in range(461, 470):
        true_output.append(0)

    true_output.append(1)

    for i in range(471, 477):
        true_output.append(0)

    true_output.append(1)

    for i in range(478, 485):
        true_output.append(0)

    return true_output
