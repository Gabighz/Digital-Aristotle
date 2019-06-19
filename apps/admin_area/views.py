from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from .handle_upload import handle_uploaded_file


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

