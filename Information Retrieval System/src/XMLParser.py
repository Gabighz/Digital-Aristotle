from xml.etree import ElementTree

class XMLParser:

    #This is where the raw parsed data is stored
    #Format: group of words, text attributes[], isBold, file number, page number, sentence number
    #text attributes format: top,left,width,height,font
    parsedWords = []
    fileNumber = 0

    #returns the current fileNumber
    def getFileNumber(self):
        return self.fileNumber

    #resets the file number
    def setFileNumber(self, fileNumber):
        self.fileNumber = fileNumber

    #not used but might in future version!
    #def hasChild(self, element):
        #if len(element):
            #return True
        #else:
            #return False

    #returns true if the element has text and false if not
    def hasText(self, element):
        if element.text is None:
            return False
        else:
            return True

    #returns true if child exists in the element, otherwise false
    def collectAllText(self, element):
        return "".join(element.itertext())

    #parses each sentence in a list of sentences form a page and stores the raw
    #data in parsedWords
    def parseSentences(self, sentences, pageNum, parsedWords):
        sentenceNum = 0
        for elem in sentences:
            sentenceNum = sentenceNum+1
            elementAttributes = elem.attrib
            if(self.hasText(elem)):
                parsedWords.append([elem.text,elementAttributes, 0,self.getFileNumber(), pageNum,sentenceNum])
            else:
                parsedWords.append([self.collectAllText(elem), elementAttributes, 1,self.getFileNumber(), pageNum,sentenceNum])

    #collects each page in the file and sends them to the sentence parser
    def parsePages(self, pages, parsedWords):
        pageNum = 0
        for c in pages:
            pageNum = pageNum +1
            sentences = c.findall('text')
            self.parseSentences(sentences, pageNum, parsedWords)

    #parses a file and increments the number
    def parseFile(self, filePath):
        self.setFileNumber(self.getFileNumber() +1)
        dom = ElementTree.parse(filePath)
        pages = dom.findall('page')
        self.parsePages(pages, self.parsedWords)

    #this returns the array of raw parsed data
    def getParsedWords(self):
        return self.parsedWords
