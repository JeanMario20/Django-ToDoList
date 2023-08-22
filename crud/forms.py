from django.forms import ModelForm
from .models import task

class formTaks(ModelForm):
    class Meta:
        model = task
        #task = forms.CharField(label="what are you goint to do today?", max_length=100)
        #fields = ["task"]
        #labels = {'task': "NameTask"}
        fields = ['task']
    