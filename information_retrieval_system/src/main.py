#
# Main program which takes as input XML files
# and outputs AIML files.
#
# Calls keyword_extractor,
# keyphrase_extractor and aiml_generator
#
# Author: Gabriel Ghiuzan
#


import os
import information_retrieval_system.src.aiml_generator as aiml_generator
import information_retrieval_system.src.keyphrase_extractor as keyphrase_extractor
import information_retrieval_system.src.keyword_extractor as keyword_extractor


# This function requests user input of the name of a file as a string
#
# @return filename: The name of the file which will be processed
def input_path():
	filename = input("Input path: ../input/")

	return filename


def main():
	# Opens the input file. Can also handle the FileNotFoundError exception.
	while True:
		try:
			# Gets the name of the file from the user
			filename = input_path()

			# Concatenates the name of the file to a pre-determined input path
			input_file_path = "../input/" + filename + ".xml"

			break
		except FileNotFoundError:
			print("File not found! Try again.")

	#aiml_rules = keyword_extractor(input_file_path, filename)

	# Creates and array in which the first index is the name of the file
	# and the second index is the extension of the file (typically 'xml')
	filename_and_extension = filename.split('.')

	# Takes only the name of the file and adds the .aiml extension
	output_filename = filename_and_extension[0] + '.aiml'

	# Stores the path of the file which will contain AIML rules
	output_path = "../output/" + output_filename

	# Opens a writeable File object
	aiml_file = open(output_path, "w")

	# Header information
	aiml_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + "\n")
	aiml_file.write("<aiml version=\"2.0\">" + "\n")

	aiml_file.write("\n</aiml>")

	aiml_file.close()

	return "ok"
