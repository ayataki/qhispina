from django.conf.urls import url, include

from apps.pet.views import index, pet_create

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^create/$', pet_create, name='pet_create'),
]
