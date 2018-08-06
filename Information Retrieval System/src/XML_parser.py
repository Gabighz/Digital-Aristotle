############################################################################
# Takes lectures notes which were pre-converted from pdf or pptx into XML  #
# and parses the XML attributes of each word or sentence                   #
############################################################################

from xml.etree import ElementTree


# Returns true if the element has text and false if not
def has_text(element):
    if element.text is None:
        return False
    else:
        return True


# Returns true if the attributes are not those of a header or footer
# on the next version this will be changed to work with any sized page
def is_not_head_or_foot(attributes):
    top = int(attributes['top'])

    # Checks top against the header and footer heights of a powerpoint page
    if top > 765 or top < 30:
        return False
    else:
        return True


# Returns true if child exists in the element, otherwise false
def collect_all_text(element):
    return "".join(element.itertext())


# Parses each sentence in a list of sentences form a page and stores the raw
# data in parsedWords
def parse_sentences(sentences, page_num, parsed_words, file_number, fontspec_array):
    # This is where the raw parsed data is stored
    sentence_num = 0

    # Iterates for each sentence in the page
    for elem in sentences:

        sentence_num = sentence_num + 1

        # 'top': '77', 'left': '29', 'width': '671', 'height': '62', 'font': '4'
        element_attributes = elem.attrib

        # font attributes 'id': '4', 'size': '52', 'family': 'Times', 'color': '#1159a0'
        font_specs = fontspec_array[int(element_attributes['font'])].attrib

        # Adds the sentence to the array if it contains text and if it is note
        # a header or footer.
        # Format: group of words, isBold, file number, page number, sentence number, fontsize, font color
        if has_text(elem) and is_not_head_or_foot(element_attributes):
            parsed_words.append(
                [elem.text, 0, file_number, page_num, sentence_num, int(font_specs['size']), font_specs['color']])
        elif is_not_head_or_foot(element_attributes):
            parsed_words.append(
                [collect_all_text(elem), 1, file_number, page_num, sentence_num, int(font_specs['size']),
                 font_specs['color']])

    return parsed_words


# Collects each page in the file and sends them to the sentence parser
# keeps track of the page number for future use.
def parse_pages(pages, parsed_words, file_number):
    page_num = 0
    fontspec_array = []

    # iterates through each page and runs each one through a method that parses
    # each sentence on each page
    for page in pages:
        page_num = page_num + 1

        # the current list of font attributes used
        fontspec_array = fontspec_array + page.findall('fontspec')

        # 'text' is the tag that the sentences are saved under in the xml files
        sentences = page.findall('text')
        parsed_words = parse_sentences(sentences, page_num, parsed_words, file_number, fontspec_array)

    return parsed_words


# This is the main method used to parse a files.
# The parameters taken are a file path, to successfully find the file and a file
# number so that the current amount of files passed can be recorded
def parse_file(file_path, file_number):
    parsed_words = []

    # An element tree is created from the xml file in order to use the ElementTree
    # library to access parts of the xml file
    dom = ElementTree.parse(file_path)

    # An array of all the pages in the document is saved and sent to a method that
    # that parses them, adding the end product to parsed parsed_words
    pages = dom.findall('page')
    parsed_words = parse_pages(pages, parsed_words, file_number)

    # Returns an array containing sentences with all the corresponding data
    # added and any unnecessary data filtered out.
    return parsed_words
