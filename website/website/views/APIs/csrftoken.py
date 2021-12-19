from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def CsrfView(request):

    return Response({'token': get_token(request)})
