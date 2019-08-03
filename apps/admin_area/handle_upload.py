from django.core.exceptions import SuspiciousOperation
import os

from information_retrieval_system.convert import convert_to_pdf


def handle_uploaded_file(file, filename, file_type):
    path_upload = "information_retrieval_system/uploaded_files/" + filename

    # Enables us to create directories from within the program
    os.makedirs(os.path.dirname(path_upload), exist_ok=True)

    if file_type in ['application/pdf', 'application/pptx']:

        with open(path_upload, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

    else:
        raise SuspiciousOperation(
            'File type not supported'
        )

    if file_type == 'application/pdf':
        convert_from_pdf(path_upload, filename)

    else:
        return 0  # to be changed with converter from pptx to xml

