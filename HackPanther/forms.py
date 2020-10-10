from django import forms 
  
# import GeeksModel from models.py 
from .models import HealthModel
  
# create a ModelForm 
class HealthForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = HealthModel
        fields = "__all__"