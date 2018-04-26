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
    for elem in sentences:
        sentence_num = sentence_num+1
        element_attributes = elem.attrib
        if(hasText(elem) and is_not_head_or_foot(element_attributes)):
            parsed_words.append([elem.text,element_attributes, 0,file_number, page_num,sentence_num])
        elif is_not_head_or_foot(element_attributes):
            parsed_words.append([collect_all_text(elem), element_attributes, 1,file_number, page_num,sentence_num])
    return parsed_words

#collects each page in the file and sends them to the sentence parser
def parse_pages( pages, parsed_words, file_number):
    page_num = 0
    for c in pages:
        page_num = page_num +1
        sentences = c.findall('text')
        parsed_words = parse_sentences(sentences, page_num, parsed_words, file_number)
    return parsed_words

#parses a file and increments the number
def parse_file(file_path, file_number):
    parsed_words = []
    dom = ElementTree.parse(file_path)
    pages = dom.findall('page')
    parsed_words = parse_pages(pages, parsed_words, file_number)
    return parsed_words
