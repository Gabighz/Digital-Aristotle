############################################################################
# Takes lectures notes which were pre-converted from pdf or pptx into XML  #
# and parses the relevant XML attributes of each word or sentence          #
# Author: Gabriel Ghiuzan                                                  #
############################################################################

import xml.etree.ElementTree as elementTree


# Creates a two-dimensional array which contains each word or sentence and its XML attributes
#
# @param path: The path of the XML file
# @return parsed_xml: A two-dimensional array which contains each word or sentence and its relevant XML attributes.
#                     The format is [word, is_bold, font_size, colour]
def parse_xml(path):

    # Parses the XML document
    tree = elementTree.parse(path)

    # Gets the root of the XML element tree
    tree_root = tree.getroot()

    # Will contain all fontspecs
    # A fontspec specifies the size, family and colour of a font
    document_fontspecs = []

    # Extracts all fontspecs from the document
    for fontspec in tree_root.iter('fontspec'):
        document_fontspecs.append(fontspec.attrib)

    # Will contain each word or sentence and its XML features
    parsed_xml = []

    # Extracts all text and their attributes
    for text in tree.findall('.//page/text'):
        # Will contain a word or sentence and its XML features
        word = []

        # Linear search to match text to its corresponding fontspec
        for fontspec in document_fontspecs:
            if text.attrib["font"] == fontspec["id"]:
                size = fontspec["size"]
                color = fontspec["color"]

        # If tree.findall('.//page/text') returns a None object,
        # it's because the word or sentence is contained by a bold or italic tag.
        if text.text is None:

            # Appends bold text
            for bold_text in text.findall('b'):
                word.extend((bold_text.text, 1, size, color))

        else:
            word.extend((text.text, 0, size, color))

        # Appends non-empty word arrays to parsed_xml
        if word:
            parsed_xml.append(word)

    return parsed_xml
