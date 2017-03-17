from django.conf.urls import url, include

from apps.pet.views import index, pet_view

urlpatterns = [
    url(r'^$', index),
    url(r'^create/$', pet_view, name="pet_create"),
]
