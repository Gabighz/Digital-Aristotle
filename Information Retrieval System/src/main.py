##################################################
# Main program which executes the modules,       #
# handles pre-processing and post-processing,    #
# and writes Keywords and Non-keywords to a file #
##################################################

CLUSTERS = 2

from XML_parser import parse_file
from feature_selection import feature_assignment
from kmeans import kmeans_clustering

def main():
    # Open a file here and apply a function from XML_parser to it

    path = '../input/foundation-year/CSC079/Slides-Week-2.xml'
    file_number = 0
    parsed_files = parse_file(path, file_number)

    # Pre-processing to filter out stopwords from parsed_files


    # Apply a function from feature_selection to the return of the aforementioned function.
    # Return a two-dimensional array which contains each word and its features, named word_list

    selected_features = feature_assignment(parsed_files)

    #prints off each entry in the selected features array(purely for debugging and demonstration not needed)
    for e in selected_features:
        print(e)

    # Apply K-means clustering to the aforementioned array
    # At the moment, the return is a data collection of the labels of each point
    clustered_data = kmeans_clustering(selected_features, CLUSTERS)

    # Write to file
    file = open("keywords.txt", "w")

    for observation in clustered_data:

        file.write(str(observation) + "\n")

    file.close()

main()
