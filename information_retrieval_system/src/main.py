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


def main():

	aiml_rules = aiml_generator(keyphrase_extractor(keyword_extractor()))

	# Opens a writeable File object
	aiml_file = open(output_path, "w")

	# Header information
	aiml_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + "\n")
	aiml_file.write("<aiml version=\"2.0\">" + "\n")

	# Stores the path of the file which will contain AIML rules
	output_path = "../output" + filename + ".aiml"

	# Enables us to create directories from within the program
	os.makedirs(os.path.dirname(output_path), exist_ok=True)

	aiml_file.write("\n</aiml>")

	aiml_file.close()


main()
