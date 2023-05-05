from django.contrib import admin

from django.apps import apps
# Register your models here.

api_models = apps.get_models()

for model_n in api_models:
    try:
        admin.site.register(model_n)
    except admin.sites.AlreadyRegistered:
        pass