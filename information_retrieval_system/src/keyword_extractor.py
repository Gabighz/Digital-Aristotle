#
# Module which identifies and outputs Keywords
#
# Author: Gabriel Ghiuzan
#

from information_retrieval_system.src.xml_parser import parse_xml
from information_retrieval_system.src.feature_selection import feature_assignment
from information_retrieval_system.src.kmeans import kmeans_clustering
from information_retrieval_system.src.processing import pre_processing, post_processing

import numpy as np

# This constant is used in kmeans.py. It determines the number of classifications.
# Currently, we have 2 classifications: Keywords and Non-keywords.
CLUSTERS = 2


# Constructs the word list using the raw data which has been normalised, then set is filtered down to the values
# within the variance threshold.
#
# @param input_file_path: The path of the XML input file. Used for XML parsing
# @param filename: The name of the XML input file. Used for performance measuring in post processing
#
# @return keywords: An array of keywords extracted from the XML input file.
def keyword_extractor(input_file_path, filename):

	# An array which contains a phrase or a word and its corresponding XML data
	parsed_xml = parse_xml(input_file_path)

	# Prints the raw XML data
	counter = 0
	print("\n Raw XML Data: \n")
	for word_array in parsed_xml:
		print(word_array)
		counter += 1
	print("\n Number of word arrays in raw XML data: ", counter)

	# Pre-processing to filter out unwanted data from parsed_content
	filtered_content = pre_processing(parsed_xml)

	# Prints the filtered data so we can check if the pre-processor is working correctly
	print("\n Filtered data (each word with its own XML features): \n")
	counter = 0
	for word_array in filtered_content:
		print(word_array)
		counter += 1
	print("\n Number of word arrays in filtered data: ", counter)

	# A two-dimensional array which contains each word and its features
	classification_features = feature_assignment(filtered_content)

	# Prints each word and its classification features and the number of all words in classification_features
	counter = 0
	print("\n \n Each word and its classification features: \n")
	for word in classification_features:
		# Format: [word, is_bold, is_larger, is_not_black, RAKE]
		print(word)
		counter += 1

	print("\n Number of words in classification_features: ", counter)

	# Runs the k-means algorithm 10 times, a number chosen arbitrarily.
	# The cost function of this algorithm converges towards local minima, not guaranteed to find
	# the global minimum. Thus, several restarts are needed.
	runs = []
	for n in range(10):
		# A 2D array which contains each word and its label
		# For example, [word, 0] or [word, 1], which means [word, Non-keyword] or [word, Keyword]
		classified_words = kmeans_clustering(classification_features, CLUSTERS)

		# Post-processing to measure the performance of our keyword extractor
		performance = post_processing(classified_words, filename)

		runs.append([classified_words, performance])

	# The highest performing classification is extracted.
	classified_words, max_performance = max(runs, key=lambda performance_array: performance_array[1])

	# F1 score, from 0 to 1
	print("\n F1 score: ", max_performance)

	# Takes only the keywords (labelled with 1)
	classified_words = np.asarray(classified_words)
	keywords = classified_words[classified_words[:, 1] == "1", 0]

	return keywords
