#
# Converts PDF and PPTX files to XML.
#
# Author: Gabriel Ghiuzan
#

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import XMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
import os


def convert_to_pdf(path_to_file, filename):
    rsrcmgr = PDFResourceManager()
    retstr = io.BytesIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = XMLConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path_to_file, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)

    xml_output = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()

    # Creates and array in which the first index is the name of the file
    # and the second index is the extension of the file
    filename_and_extension = filename.split('.')

    # Takes only the name of the file and adds the .txt extension
    output_filename = filename_and_extension[0] + '.xml'

    # Stores the path of the file which will contain the converted file
    output_path = "information_retrieval_system/xml_files/" + output_filename

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    output_file = open(output_path, "w")
    output_file.write(str(xml_output))

    output_file.close()
