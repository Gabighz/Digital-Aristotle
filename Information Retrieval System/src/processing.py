##################################################
# Handles pre-processing (stopwords filtering)   #
# and post-processing (performance testing)      #
##################################################

import re
import nltk
import numpy as np

from sklearn.metrics import f1_score

def pre_processing(raw_data):

    # Prints the raw XML data so we can check if the pre-processor is working correctly
    print("\n Raw XML Data: \n")
    counter = 0
    for word_array in sorted(raw_data):
        print(word_array)
        counter += 1
    print("\n Number of word arrays in raw XML data: ", counter)

    # Iterates through raw XML data and concatenates all words to a string
    sentence = ' '.join([word for (array_index, word_index), word in np.ndenumerate(raw_data) if word_index == 0])

    # Converts all words to lowercase; e.g. so Sensors and sensors are not
    # considered different words
    lowercase_string = sentence.lower()

    # Cleans each word of non-alphanumeric characters
    # e.g. so 'sensors)' and 'sensors' are not considered different words
    filtered_string = re.sub("[^a-zA-Z]"," ", lowercase_string)

    # Further filtering to keep only nouns; thus filtering stopwords as well
    # Also filters out words which have a character count of 1 or less.
    tokens = nltk.word_tokenize(filtered_string)
    tags = nltk.pos_tag(tokens)

    filtered_string = ' '.join([word for word,pos in tags
                    if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')
                    and (len(word) > 1)])

    print("\n Words that have remained after filtering (all in one string): \n")
    print(filtered_string)

    # Compiles the filtered words to an array which contains
    # each word and its XML features
    filtered_data = []
    clean_words = filtered_string.split()

    # Compiles only filtered words from raw data to an array which contains
    # each word and its XML features that were in raw data
    for word_array in raw_data:

        filtered_sentence = ""
        raw_sentence = re.sub("[^a-zA-Z]"," ", word_array[0]).split()

        for i in range(len(raw_sentence)):
            if raw_sentence[i].lower() in clean_words:
                filtered_sentence= filtered_sentence + " " + raw_sentence[i]

        if len(filtered_sentence.lstrip()) > 0:

            filtered_data.append([filtered_sentence.lstrip().lower(),
            word_array[1], word_array[2], word_array[3], word_array[4],
            word_array[5], word_array[6]])

    print("\n Filtered data (each word with its own XML features): \n")
    counter = 0
    for word_array in sorted(filtered_data):
        print(word_array)
        counter += 1
    print("\n Number of word arrays in filtered data: ", counter)

    return filtered_data

# Computes the F1-score of our classifier
# Takes in a 2D array which contains each observation and their label
# Compares that to the ground truth (correct) value of each observation
def post_processing(results):

    # Contains manually annoted ground truth values
    true_output = manual_annotation(results)

    # Contains the estimated targets returned by the classifier
    estimated_targets = []

    for i in range(len(results)):
        estimated_targets.append(results[i][1])

    return f1_score(true_output, estimated_targets)

# Only for the SlidesWeek2 file at the moment
def manual_annotation(results):

    true_output = []

    true_keywords = ["nxt", "mindstorms", "lego", "robot", "sensors", "servo", "motors"]

    for i in range(len(results)):

        if results[i][0] in true_keywords:
            true_output.append(1)
        else:
            true_output.append(0)


    return true_output
