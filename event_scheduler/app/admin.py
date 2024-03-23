from django.contrib import admin
from  .models import Event,EventStatus
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display=('title','start','duration','status')

admin.site.register(Event,EventAdmin)
admin.site.register(EventStatus)
