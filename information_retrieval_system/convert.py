#
# Converts PDF and PPTX files to XML.
#
# Author: Gabriel Ghiuzan
#

import os
import unicodedata
import string

valid_filename_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
char_limit = 255


def convert_from_pdf(path_to_file, filename):
    # Sanitizes the filename to protect against any injections
    clean_filename = sanitize_filename(filename)

    # Creates and array in which the first index is the name of the file
    # and the second index is the extension of the file
    filename_and_extension = clean_filename.split('.')

    output_filename = filename_and_extension[0] + '.xml'

    output_path = 'information_retrieval_system/xml_files/' + output_filename

    # Enables us to create directories from within the program
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Executes a command which converts the pdf file to xml
    os.system("pdftohtml -xml %s %s" % (path_to_file, output_path))


def sanitize_filename(filename, whitelist=valid_filename_chars, replace=' '):
    # Replace spaces
    for r in replace:
        filename = filename.replace(r, '_')

    # Keep only valid ascii chars
    cleaned_filename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode()

    # Keep only whitelisted chars
    cleaned_filename = ''.join(c for c in cleaned_filename if c in whitelist)
    if len(cleaned_filename) > char_limit:
        print(
            "Warning, filename truncated because it was over {}. Filenames may no longer be unique".format(char_limit))
    return cleaned_filename[:char_limit]