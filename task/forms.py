from django import forms
from .models import Task


class taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "important"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Escribe un título"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Escribe una descripción"}
            ),
            "important": forms.CheckboxInput(
                attrs={"class": "form-check-input m-auto"}
            ),
        }