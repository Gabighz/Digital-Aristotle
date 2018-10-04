############################################################################
# Takes lectures notes which were pre-converted from pdf or pptx into XML  #
# and parses the XML attributes of each word or sentence                   #
# Author: Gabriel Ghiuzan                                                  #
############################################################################

import xml.etree.ElementTree as element_tree


# Creates a two-dimensional array which contains each word or sentence and its XML attributes
#
# @param path: The path of the XML file
# @return parsed_xml: A two-dimensional array which contains each word or sentence and its XML attributes
def parse_xml(path):

    tree = element_tree.parse(path)

    tree_root = tree.getroot()

    document_fontspecs = []

    for pages in tree_root:
        for fontspec in pages.iter('fontspec'):
            document_fontspecs.append(fontspec.attrib)

    print(document_fontspecs)