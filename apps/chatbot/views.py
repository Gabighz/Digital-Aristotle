from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from information_retrieval_system.src import main as ir_system


@csrf_exempt
def get_response(request):
    response = {'status': None}

    if request.method == 'POST':
        data = json.loads(request.body)
        message = data['message']

        chat_response = 'ok'  # to be replaced later with something from the IR System
        response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True}
        response['status'] = 'ok'

    else:
        response['error'] = 'no post data found'

    return HttpResponse(
        json.dumps(response),
        content_type="application/json"
    )


def index(request, template_name="index.html"):
    context = {'title': 'Digital Aristotle'}
    return render_to_response(template_name, context)
