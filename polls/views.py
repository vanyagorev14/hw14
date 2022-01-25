from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, render

from polls.tasks import celery_send_mail

from .forms import Reminder


def reminder(request):
    if request.method == "POST":
        form = Reminder(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            receiver = form.cleaned_data['email']
            time = form.cleaned_data['time']
            celery_send_mail.apply_async((message, receiver), eta=time)
            messages.success(request, 'Remind is created')
            return redirect('')
        else:
            messages.error(request, 'Reminder not created!')
    else:
        form = Reminder()

    return render(request, "index.html", context={"form": form})
