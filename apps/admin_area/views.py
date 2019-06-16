from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def index(request, template_name="admin_area/index.html"):
    context = {'title': 'Digital Aristotle'}
    return render_to_response(template_name, context)


@login_required(login_url='/accounts/login/')
def upload(request, template_name="admin_area/upload.html"):
    context = {'title': 'Digital Aristotle'}
    return render_to_response(template_name, context)
