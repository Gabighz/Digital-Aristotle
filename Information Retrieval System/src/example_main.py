from XML_parser import *
from feature_selection import *
def Main():
    #set your own absolute path to file#############################
    path = r'C:\Users\Slades-PC\Documents\Test\Data.xml'
    file_number = 1

    #doesnt take multiple files but returns an array so they can be joined other can easily be changed to take multiple
    #assigned parsed file to an array with parsed xml data
    parsed_file = parse_file(path, file_number)


    #prints out each entry in the raw data
    for e in parsed_file:
        print(e)



    #assigned_features is set equal to an array of feature assigned word data
    assigned_features = feature_assignment(parsed_file)
    #prints out the polished word data
    for e in assigned_features:
        print(e)

Main()
