from django.forms import ModelForm, Textarea, CheckboxInput, Select
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        labels = {
            'important': 'Importante',  # Aquí especificamos la etiqueta con tilde
        }
        widgets = { 'description': Textarea(attrs={'class': 'form-control'}), 'important': CheckboxInput(attrs={'class': 'form-check-input'})}
