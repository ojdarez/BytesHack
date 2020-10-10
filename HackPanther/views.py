from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import HealthForm

def index(request):
    mapbox_access_token = 'pk.eyJ1Ijoiam9qb3NlcGgxMiIsImEiOiJja2czYmR0b3YwOGh1MnFqdGl0cnEyYWhkIn0.LOPwbn5Mh9gl79tMRoFTvA'
    return render(request, "HackPanther/index.html", { 'mapbox_access_token': mapbox_access_token })


def health(request):
    context ={} 
  
    # create object of form 
    form = HealthForm(request.POST or None, request.FILES or None) 
      
    # check if form data is valid 
    if form.is_valid(): 
        # save the form data to model 
        form.save() 
  
    context['form'] = form 
    return render(request, "HackPanther/health.html", context) 