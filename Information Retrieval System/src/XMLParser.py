
from xml.etree import ElementTree
from WordObject import WordObject

#
#Variables
#
pageNumber = 0
sentenceNumber = 0
wordNumber = 0
isBold = 0
wordList = []

#Parses words
def hasChild(element):
    if element.text is None:
        return True

    else:
        return False

def getAttribs(e):
    attributes = [e.attrib['top'],e.attrib['left'],e.attrib['width'],e.attrib['height'],e.attrib['font']]
    return attributes

def parseWord(word,sentence):
    global sentenceNumber
    global pageNumber
    global wordNumber
    global isBold
    global fontSize
    global wordList
    wordNumber += 1
    attributes = getAttribs(sentence)
    wordOb = WordObject(word,isBold,1,pageNumber,sentenceNumber,wordNumber,attributes[0],attributes[1],attributes[2],attributes[3],attributes[4])
    wordList.append(wordOb)

def parseWords(words,sentence):
    for e in words:
        parseWord(e,sentence)

#Parses Sentences
def parseSentences(sentences):
    for d in sentences:
        #global fontSize
        #fontSize = d.attrib['font']
        global sentenceNumber
        sentenceNumber += 1
        if not hasChild(d):
            words = d.text.split()
            parseWords(words,d)
        else:
            for child in d:
                if child.tag == 'b':
                    temp = child.text.strip()
                    temp = temp.split()
                    global isBold
                    isBold = 1
                    parseWords(temp,d)
                    isBold = 0


def parsePages(pages):
    for c in pages:
        global pageNumber
        pageNumber += 1
        sentences = c.findall('text')
        parseSentences(sentences)

def printWords(list):
    for w in list:
        print(str(w.getWordArray()))


dom = ElementTree.parse('Data.xml')
pages = dom.findall('page')
parsePages(pages)
printWords(wordList)
