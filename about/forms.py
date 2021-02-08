from django import forms
from .models import Timeline, Expertise, AboutMe
class ExpertForm(forms.ModelForm):
    class Meta:
        model = Expertise
        fields = '__all__'

class TimelineForm(forms.ModelForm):
    class Meta:
        model = Timeline
        fields ='__all__'