from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
import os

from information_retrieval_system.convert import convert_to_pdf


@login_required(login_url='/accounts/login/')
def index(request, template_name="admin_area/index.html"):
    context = {'title': 'Digital Aristotle'}
    return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def upload(request, template_name="admin_area/upload.html"):
    context = {'title': 'Digital Aristotle'}

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        handle_uploaded_file(request.FILES['file'], request.FILES['file'].name, request.FILES['file'].content_type)

    else:
        form = UploadFileForm()

    return render(request, template_name, context, {'form': form})


def handle_uploaded_file(file, filename, file_type):
    path_upload = "information_retrieval_system/uploaded_files/" + filename

    # Enables us to create directories from within the program
    os.makedirs(os.path.dirname(path_upload), exist_ok=True)

    with open(path_upload, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    if file_type == 'application/pdf':
        convert_to_pdf('uploaded_files/' + filename, filename)

    elif file_type == 'application/pptx':
        return 0  # to be changed

    else:
        print("File not supported")  # to be changed

