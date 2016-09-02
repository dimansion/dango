from django import forms

from .models import *

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('to_do', 'date',)
	widgets={
		'to_do':forms.TextInput(),
		'date':forms.DateTimeInput(),
	}

