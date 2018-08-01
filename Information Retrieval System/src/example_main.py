from XML_parser import parse_file
from feature_selection import feature_assignment
from processing import pre_processing


def main():
    # set your own absolute path to file#############################
    path = r'C:\Users\Slades-PC\Documents\Swansea-University-CS-chatbot\Information Retrieval System\input\foundation-year\CSC079\Lecture 1 - Understanding what professional issues are.xml'
    file_number = 1

    # doesnt take multiple files but returns an array so they can be joined other can easily be changed to take multiple
    # assigned parsed file to an array with parsed xml data
    parsed_file = parse_file(path, file_number)

    # Pre-processing to filter out stopwords from parsed_files
    filtered_content = pre_processing(parsed_file)

    # Return a two-dimensional array which contains each word and its features
    classification_features = feature_assignment(filtered_content)
    # prints out the polished word data
    for e in classification_features:
        print(e)


Main()
