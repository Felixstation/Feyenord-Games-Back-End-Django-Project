from django.contrib import admin
from core.models import Contact, AdvertImage , Subscriber , BlockedIps

admin.site.register(Contact)
admin.site.register(AdvertImage)
admin.site.register(Subscriber)
admin.site.register(BlockedIps)