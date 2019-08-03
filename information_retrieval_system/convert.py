#
# Converts PDF and PPTX files to XML.
#
# Author: Gabriel Ghiuzan
#

import os


def convert_from_pdf(path_to_file, filename):

    # Creates and array in which the first index is the name of the file
    # and the second index is the extension of the file
    filename_and_extension = filename.split('.')

    output_filename = filename_and_extension[0] + '.xml'

    output_path = 'information_retrieval_system/xml_files/' + output_filename

    # Enables us to create directories from within the program
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Executes a command which converts the pdf file to xml
    os.system("pdftohtml -xml %s %s" % (path_to_file, output_path))
