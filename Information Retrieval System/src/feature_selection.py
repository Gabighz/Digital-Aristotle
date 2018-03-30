#########################################################################################
# Selects desired features of words from XML data and represents each word as an array. #
# This array contains the word itself as a string and its features as numerical values. #
#########################################################################################


class FeatureAssignment:
    #This list contains the word array
    wordList = []

    #the variables that determine its order
    documentNumber = 0
    pageNumber = 0
    sentenceNumber = 0
    wordNumber = 0

    #The on page attributes
    top = 0
    left = 0
    width = 0
    height = 0
    fontSize = 0

    #the word itself
    isBold = 0

    def __init__(self, rawData):
        self.populateWordList(rawData);

    def populateWordList(self, rawData):
        for e in rawData:
            self.setWordVariables(e[1], e[2], e[3], e[4], e[5])
            words = e[0].split()
            for w in words:
                self.wordNumber = self.wordNumber +1
                self.addWord(w)
        #for each element in raw data.... addword()...

    def setWordVariables(self, attributes, isBold, documentNumber, pageNumber, sentenceNumber):
        self.isBold = isBold
        self.documentNumber = documentNumber
        self.pageNumber = pageNumber
        self.sentenceNumber = sentenceNumber

        self.top = attributes['top']
        self.left = attributes['left']
        self.width = attributes['width']
        self.height = attributes['height']
        self.fontSize = attributes['font']

    #Resets the documentNumber for the next word
    def setDocumentNumber(self, documentNumber):
        self.documentNumber = documentNumber

    #Resets the pageNumber for the next word
    def incrementPageNumber(self,pageNumber):
        self.pageNumber = pageNumber

    #Resets the sentenceNumber for the next word
    def incrementSentenceNumber(self, sentenceNumber):
        self.sentenceNumber = sentenceNumber

    #Resets the top for the next word
    def setTop(self, top):
        self.top = top

    #Resets the left for the next word
    def setTop(self, left):
        self.left = left

    #Resets the width for the next word
    def setTop(self, width):
        self.width = width

    #Resets the height for the next word
    def setTop(self, height):
        self.height = height

    #Resets the fontSize for the next word
    def setTop(self, fontSize):
        self.fontSize = fontSize

    #Resets the isBold for the next word
    def setIsBold(self, isBold):
        self.isBold = isBold

    # ToDO:need to finish
    def getWordData(self):
        return 1;

    #adds a word to the word list
    def addWord(self, word):
        self.wordNumber = self.wordNumber + 1
        self.wordList.append([word, self.getWordData(), self.documentNumber,self.pageNumber,self.sentenceNumber,self.wordNumber,
        self.top,self.left,self.width,self.height,self.fontSize])

    #returns the list of word data
    def getWordList(self):
        return self.wordList
