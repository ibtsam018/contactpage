from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return HttpResponseRedirect(request.path_info)
    else:
        f = FeedbackForm()
    return render(request, 'contact.html', {'form': f})