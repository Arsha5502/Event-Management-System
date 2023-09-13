from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from .forms import ApplicantForm

# Create your views here.

def index(request):
    events= Event.objects.all()
    context = {
        'events' : events
    }
    return render(request,'index.html', context)

def eventdetail(request,pk):
              
              
        event_s=Event.objects.get(pk=pk)
        form = ApplicantForm()
        if request.method == 'POST':
              form = ApplicantForm(request.POST)
              if form.is_valid():
                    applicant = form.save(commit=False)
                    applicant.event = event_s
                    applicant.save()
                    
        context = {
              'event' : event_s,
              'form'  : form
        }
        return render(request,'eventdetail.html',context)

