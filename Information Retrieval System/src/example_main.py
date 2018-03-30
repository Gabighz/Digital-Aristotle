from XMLParser import XMLParser
from FeatureAssignment import FeatureAssignment
def Main():
    #set your own absolute path to file#############################
    path = r'C:\Users\Slades-PC\Documents\Test\Data.xml'
    parsedFiles = XMLParser()
    #can take multiple files########################################
    parsedFiles.parseFile(path)
    #parsedFiles.parseFile(path)

    #prints out the raw word data from both files
    #print(parsedFiles.getParsedWords())

    assignedFeatures = FeatureAssignment(parsedFiles.getParsedWords())
    #prints out the polished word data
    var = assignedFeatures.getWordList()
    for e in var:
        print(e)

Main()
