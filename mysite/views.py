from django.shortcuts import render
from testing.models import Reminder

def home(request):
    reminders = Reminder.objects.all().order_by('-Due_Date')
    return render(request, 'testing/main.html', { 'reminders': reminders })

def main(request):
    reminders = Reminder.objects.all()
    return render(request, 'testing/main.html', { 'reminders': reminders })