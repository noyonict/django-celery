from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


def index(request):
    return render(request, 'progress-bar/index.html')


@api_view(['GET'])
def status(request):
    start = request.GET.get('end')
    if not start or int(start) >= 100:
        start = 0
    return Response({"status": int(start) + 5})
