############################################################################
# Takes lectures notes which were pre-converted from pdf or pptx into XML  #
# and parses the XML attributes of each word or sentence                   #
# Author: Gabriel Ghiuzan                                                  #
############################################################################

import xml.etree.ElementTree as elementTree


# Creates a two-dimensional array which contains each word or sentence and its XML attributes
#
# @param path: The path of the XML file
# @return parsed_xml: A two-dimensional array which contains each word or sentence and its XML attributes
def parse_xml(path):

    tree = elementTree.parse(path)

    tree_root = tree.getroot()

    document_fontspecs = []

    for fontspec in tree_root.iter('fontspec'):
        document_fontspecs.append(fontspec.attrib)


    