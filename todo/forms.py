from django import forms

from .models import Schedule

class ScheduleForm(forms.ModelForm):
    to_do = forms.CharField(label='Your name', max_length=100)
    class Meta:
        model = Schedule
        fields = ('to_do', 'date',)


