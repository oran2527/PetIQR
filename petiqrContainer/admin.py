from django.contrib import admin
from .models import Countries

# Register your models here.
admin.site.register(Countries)
admin.site.register(States)
admin.site.register(Cities)
admin.site.register(Owners)
