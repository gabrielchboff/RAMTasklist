from django.forms import ModelForm, TextInput, CheckboxInput
from core.models import Tasklist

class TasklistForm(ModelForm):
    class Meta:
        model = Tasklist
        fields = ['is_done', 'description']
        widgets = {
            'is_done': CheckboxInput(
                attrs={'class': 'form-check-input'}
            ),
            'description': TextInput(
                attrs={'class':'form-control'}
                )
        }