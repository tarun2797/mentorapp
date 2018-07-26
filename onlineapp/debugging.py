import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","onlineproject.settings")
django.setup()
from onlineapp.models import *
manager = college.objects
querysets = college.objects.all()
print(querysets)
for queryset in querysets:
    print(queryset)