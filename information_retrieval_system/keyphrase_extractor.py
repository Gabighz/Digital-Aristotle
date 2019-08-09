#
# Module which identifies and outputs keyphrases
# based on XML files and the output of the keyword_extractor
#
# Author: Gabriel Ghiuzan
#

import re
import numpy as np

# The position of text in the raw XML array
TEXT_INDEX = 0


# Given keywords and text data from the XML input file, extracts phrases that contain keywords.
# Then, these phrases are ranked.
# For each phrase associated with a keyword, the highest-ranking phrase is labelled a keyphrase.
# Finally, the function returns a list of each keyword and its keyphrase.
#
# @param keyword_extractor_output: Contains a numpy array of keywords extracted from the XML input file
# and a numpy array of the text data from the XML input file.
# @return keyphrases: A list of keyword-keyphrase pairs.
def keyphrase_extractor(keyword_extractor_output):

	keywords, text = keyword_extractor_output

	sentences = pre_processing(text)

	potential_keyphrases = [sentence for sentence in sentences if any(word in sentence for word in keywords)]


# Ranks the extracted sentences that are associated with a particular keyword
#
# @param sentences: A list of sentences that contain a specific keyword.
# @param keyphrase: The highest-ranking sentence is returned, considered to be a keyphrase
def ranking_system(sentences):

	return []  # to be implemented


# Cleans text of non-alphanumeric characters
# and joins together arrays that are thought to form sentences
#
# @param text: A numpy array of text data
# @return clean_text: A numpy array of text stripped of non-alphanumeric characters
def pre_processing(text):

	text = np.array(text).tolist()

	# Removes non-alphanumeric characters
	clean_text = [re.sub("[^a-zA-Z]", " ", sentence) for sentence in text]

	# Removes leading and ending spaces
	clean_text = list(map(str.strip, clean_text))

	sentences = []  # to be implemented

	return sentences
