##################################################
# Handles pre-processing (stopwords filtering)   #
# and post-processing (performance testing)      #
##################################################

import re
import nltk
import numpy as np

from sklearn.metrics import f1_score

def pre_processing(raw_data):

    # Iterates through raw XML data and concatenates all words to a string
    sentence = ' '.join([word for (array_index, word_index), word in np.ndenumerate(raw_data) if word_index == 0])

    # Converts all words to lowercase; e.g. so Sensors and sensors are not
    # considered different words
    lowercase_string = sentence.lower()

    # Cleans each word of non-alphanumeric characters
    # e.g. so 'sensors)' and 'sensors' are not considered different words
    filtered_string = re.sub("[^a-zA-Z]"," ", lowercase_string)

    # Further filtering to keep only nouns; thus filtering stopwords as well
    tokens = nltk.word_tokenize(filtered_string)
    tags = nltk.pos_tag(tokens)

    filtered_string = ' '.join([word for word,pos in tags if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')])
    print(filtered_string)

    # Compiles the filtered words to an array which contains
    # each word and its XML features
    filtered_data = []
    iterable_array = filtered_string.split()

    for i in range(len(iterable_array)):
        word_data = []
        for j in range(len(raw_data)):

            if iterable_array[i] in raw_data[j][0].lower():
                word_data.append(iterable_array[i])

                for features in raw_data[j][1:]:
                    word_data.append(features)

        filtered_data.append(word_data)

    return filtered_data

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
