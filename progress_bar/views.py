from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


def index(request):
    """
    Load Bootstrap Progress bar
    :param request: http request
    :return: a html file
    """
    return render(request, 'progress-bar/index.html')


@api_view(['GET'])
def status(request):
    """
    take only GET request and return status code
    :param request: progress variable a number from the clint
    :return: progress + 5 if between 0  to 100
    """
    progress = request.GET.get('progress')
    if not progress or int(progress) >= 100:
        progress = 0
    return Response({"status": int(progress) + 5})
