import os

from information_retrieval_system.convert import convert_to_pdf


def handle_uploaded_file(file, filename, file_type):
    path_upload = "information_retrieval_system/uploaded_files/" + filename

    # Enables us to create directories from within the program
    os.makedirs(os.path.dirname(path_upload), exist_ok=True)

    with open(path_upload, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    if file_type == 'application/pdf':
        convert_to_pdf(path_upload, filename)

    elif file_type == 'application/pptx':
        return 0  # to be changed

    else:
        print("File not supported")  # to be changed
