from django.urls import include, path

from classification.views import classify_dog_breeds, get_classification_home

urlpatterns = [
    path("", get_classification_home),
    path("dog-breeds", classify_dog_breeds),
]
