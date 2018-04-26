############################################################################
# Takes lectures notes which were pre-converted from pdf or pptx into XML  #
# and parses the XML attributes of each word or sentence                   #
############################################################################

from xml.etree import ElementTree

#not used but might in future version!
#def hasChild( element):
    #if len(element):
        #return True
    #else:
        #return False

#returns true if the element has text and false if not
def hasText( element):
    if element.text is None:
        return False
    else:
        return True

#returns true if the attributes are not those of a header or footer
#on later iterations this will be changed to work with any sized page
def is_not_head_or_foot(attributes):
    top = int(attributes['top'])

    #checks top against the header and footer heights of a powerpoint page
    if top > 765 or top < 30:
        return False
    else:
        return True

#returns true if child exists in the element, otherwise false
def collect_all_text( element):
    return "".join(element.itertext())

#parses each sentence in a list of sentences form a page and stores the raw
#data in parsedWords
def parse_sentences( sentences, page_num, parsed_words, file_number):
    #This is where the raw parsed data is stored
    #Format: group of words, text attributes[], isBold, file number, page number, sentence number
    #text attributes format: top,left,width,height,font
    sentence_num = 0

    #iterates for each sentence in the page
    for elem in sentences:

        sentence_num = sentence_num+1

        element_attributes = elem.attrib

        #adds the sentence to the array if it contains text and if it is note
        #a header or footer
        if(hasText(elem) and is_not_head_or_foot(element_attributes)):
            parsed_words.append([elem.text,element_attributes, 0,file_number, page_num,sentence_num])
        elif is_not_head_or_foot(element_attributes):
            parsed_words.append([collect_all_text(elem), element_attributes, 1,file_number, page_num,sentence_num])
            
    return parsed_words

#collects each page in the file and sends them to the sentence parser
#keeps track of the page number for future use
def parse_pages( pages, parsed_words, file_number):
    page_num = 0

    #iterates through each page and runs each one through a method that parses
    #each sentence on each page
    for c in pages:
        page_num = page_num +1

        #'text' is the tag that the sentences are saved under in the xml files
        sentences = c.findall('text')
        parsed_words = parse_sentences(sentences, page_num, parsed_words, file_number)

    return parsed_words

#this is the main method used to parse a files
#the parameters taken are a file path, to succesfully find the file and a file
#number so that the current amount of files passed can be recorded
def parse_file(file_path, file_number):

    parsed_words = []

    #An element tree is created from the xml file in order to use the ElementTree
    #library to access parts of the xml file
    dom = ElementTree.parse(file_path)

    #an array of all the pages in the document is saved and sent to a method that
    #that parses them, adding the end product to parsed parsed_words
    pages = dom.findall('page')
    parsed_words = parse_pages(pages, parsed_words, file_number)

    #returns an array containing sentences with all the corresponding data
    #added and any uneccesarry data filtered out.
    return parsed_words
