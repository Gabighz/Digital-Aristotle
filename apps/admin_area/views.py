from django.shortcuts import render_to_response


def index(request, template_name="admin_index.html"):
    context = {'title': 'Digital Aristotle'}
    return render_to_response(template_name, context)
