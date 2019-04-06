#
# Handles pre-processing (stopwords filtering)
# and post-processing (performance testing)
# Author: Gabriel Ghiuzan
#

import re
import nltk
import numpy as np

from sklearn.metrics import f1_score

# The position of the word in the raw XML array
WORD_INDEX = 0


def pre_processing(raw_data):
    # Converts raw_data to a numpy array
    raw_data = np.array(raw_data, dtype=object)
    # Iterates through raw XML data and concatenates all words to a string
    sentence = ' '.join(raw_data[:, WORD_INDEX])

    # Converts all words to lowercase to prevent duplication of same word with different cases.
    lowercase_string = sentence.lower()

    # Cleans each word of non-alphanumeric characters
    # e.g. so 'sensors)' and 'sensors' are not considered different words
    filtered_string = re.sub("[^a-zA-Z]", " ", lowercase_string)

    # Further filtering to keep only nouns; thus filtering stopwords as well
    # Also filters out words which have a character count of 1 or less.
    tokens = nltk.word_tokenize(filtered_string)
    tags = nltk.pos_tag(tokens)

    filtered_string = ' '.join([word for word, pos in tags
                                if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')
                                and (len(word) > 1)])

    # Compiles the filtered words to an array which contains
    # each word and its XML features
    filtered_data = []
    clean_words = filtered_string.split()

    # Appends only filtered words from raw data to an array which contains
    # each word and its XML features that were in raw data
    for word_array in raw_data:

        filtered_sentence = ""
        raw_sentence = re.sub("[^a-zA-Z]", " ", word_array[0]).split()

        for i in range(len(raw_sentence)):
            if raw_sentence[i].lower() in clean_words:
                filtered_sentence = filtered_sentence + " " + raw_sentence[i]
        # !to be improved
        if len(filtered_sentence.lstrip()) > 0:
            filtered_data.append([filtered_sentence.lstrip().lower(), word_array[1], word_array[2], word_array[3]])

    return filtered_data


# Computes the F1-score of our classifier
# Takes in a 2D array which contains each observation and their label
# Compares that to the ground truth (correct) value of each observation
def post_processing(results, filename):
    # Contains manually annotated ground truth values
    true_output = manual_annotation(results, filename)

    # Contains the estimated targets returned by the classifier
    estimated_targets = []

    for i in range(len(results)):
        estimated_targets.append(results[i][1])

    return f1_score(true_output, estimated_targets)


# Only for the SlidesWeek2 file at the moment
def manual_annotation(results, filename):
    true_output = []
    true_keywords = []

    # These manual annotations must be scrutinized, given their subjective nature
    if filename == "ComputingComponents.xml":
        true_keywords = ["ad", "computer", "memory", "unit", "input", "output", "control", "bus", "cycle",
                         "fetch-execute", "instruction", "register", "program", "counter", "central", "processing",
                         "random", "access", "read", "only", "magnetic", "storage", "disks", "seek", "time", "latency",
                         "transfer", "rate", "cd", "dvd", "blu-ray", "touch", "screen", "resistive", "capacitive",
                         "infrared", "surface", "acoustic", "wave", "embedded", "systems", "cd-rom", "cd-da", "cd-worm",
                         "rw", "ram"]

    elif filename == "GatesAndCircuits.xml":
        true_keywords = ["gates", "transistors", "circuits", "boolean", "expressions", "truth", "tables", "logic",
                         "diagrams", "adder", "half", "full", "multiplexer", "s-r", "latch", "integrated", "circuits",
                         "gate", "not", "and", "or", "xor", "nand", "nor", "transistor", "combinational",
                         "sequential", "equivalence", "algebra", "adders", "multiplexers", "memory", "central",
                         "processing", "unit"]

    elif filename == "NumberSystems.xml":
        true_keywords = ["positional", "convert", "base", "bases", "numbers", "natural", "negative", "integers",
                         "rational", "integer", "base",
                         "converting", "binary", "arithmetic", "subtracting", "octal", "hexadecimal", "decimal",
                         "byte"]

    elif filename == "TheBigPicture.xml":
        true_keywords = ["layers", "abstraction", "analytical", "engine", "history", "application", "programmers",
                         "systems", "hardware", "software", "system", "abacus", "blaise", "pascal", "joseph",
                         "jacquard", "utility", "computing",
                         "charles", "babbage", "ada", "lovelace", "alan", "turing", "harvard", "mark", "vacuum",
                         "tubes", "magnetic", "drum", "card", "readers", "tape", "drives", "transistor", "cores",
                         "disks", "integrated", "circuits", "terminal", "generation", "first", "second", "third",
                         "large-scale", "integration", "pcs", "commercial", "market", "workstations", "laptops",
                         "tablet", "computers", "computer", "smart", "phones", "parallel", "computing", "networking", "arpanet",
                         "lan", "internet", "quantum", "qubits", "machine", "language", "languages", "assembly",
                         "translators", "translator", "changes", "high-level", "separation", "users", "structured", "new",
                         "Microsoft",
                         "design", "object-oriented", "world", "wide", "web"]

    for i in range(len(results)):

        if results[i][0] in true_keywords:
            true_output.append(1)
        else:
            true_output.append(0)

    return true_output
