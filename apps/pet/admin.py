from __future__ import absolute_import
from django.contrib import admin

from apps.pet.models import Pet, Vaccine

admin.site.register(Pet)
admin.site.register(Vaccine)
# Register your models here.
