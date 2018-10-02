import re


# Creates an array of keywords given the output of the Keyword extractor
#
# @param path: The output path of the Keyword extractor
# @return keywords: An array which contains only the keywords
def keyword_output(filename):
    # Concatenates the name of the file to a pre-determined input path
    path = "../../keyword_extractor/output/first-year/CS-150/" + filename

    # Will contain keywords
    keywords = []

    # Extracts all keywords and ignores non-keywords line-by-line
    #
    # Each line of the file contains an array made up of a word and its keyword or non-keyword label,
    # e.g. ['word', 1].
    # However, these arrays are treated as strings given that they are stored in a .txt format.
    with open(path, "r") as output_file:
        for line in output_file:
            # Cleans each line of non-alphanumeric characters
            # However, it concatenates words with their keyword or non-keyword label
            # e.g. ['word', 1] becomes word1
            pattern = re.compile('[\W_]+')
            filtered_line = pattern.sub('', line)

            # Appends a word if it is a keyword, excluding its label
            if filtered_line[-1] == "1":
                keywords.append(filtered_line[:-1])

    return keywords