from django.contrib import admin
from .models import Reminder

class ReminderAdmin(admin.ModelAdmin):
    list_display = ('Title','Task','Due_Date')

admin.site.register(Reminder, ReminderAdmin)

# Register your models here.

# Register your models here.
