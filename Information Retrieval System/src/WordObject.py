class WordObject:
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
    wordString = ""
    wordData = 0
    isBold = 0

    def __init__(self,word,isBold,documentNumber,pageNumber,sentenceNumber,wordNumber,top,left,width,height,fontSize):
        self.isBold = isBold
        self.wordString = word
        self.documentNumber = documentNumber
        self.pageNumber = pageNumber
        self.sentenceNumber = sentenceNumber
        self.wordNumber = wordNumber
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        self.fontSize = fontSize
        self.wordData = 1
        self.wordString = word

    def getWordArray(self):
        output = [self.documentNumber,self.pageNumber,self.sentenceNumber,self.wordNumber,self.top,self.left,self.width,self.height,self.fontSize,self.wordData]
        return output

        #need to finnish
    def setWordData():
        return 1;

    def wordInfo(self):
        info = str(self.isBold) + " " + str(self.wordString) + " " + str(self.documentNumber) + str(self.pageNumber) + " " + str(self.sentenceNumber) + " " + str(self.wordNumber) + " " + str(self.top) + " " + str(self.left) + " " + str(self.height)+ " " + str(self.fontSize) + " " + str(self.wordData)
        return info
