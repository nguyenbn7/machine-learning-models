from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(["GET"])
def get_classification_home(request: HttpRequest):
    return Response({"message": "GET /api/classification"})


@api_view(["GET"])
def classify_dog_breeds(request: HttpRequest):
    return Response({"message": "GET /api/classification"})
