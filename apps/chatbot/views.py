from django.shortcuts import render_to_response
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_response(request):
    response = {'status': None}

    if request.method == 'POST':
        data = json.loads(request.body)
        message = data['message']

        chat_response = 'ok'  # to be replaced later with a function
        response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True}
        response['status'] = 'ok'

    else:
        response['error'] = 'no post data found'

    return HttpResponse(
        json.dumps(response),
        content_type="application/json"
    )


def index(request, template_name="chatbot/index.html"):
    context = {'title': 'Digital Aristotle'}
    return render_to_response(template_name, context)
