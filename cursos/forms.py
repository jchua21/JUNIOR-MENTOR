from django import forms
from .models import Curso, Comment
from .snippets import choices

class CursoCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título'}))
    categories = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categorías separadas por coma. Ejemplo: chino, tailandés'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la ubicación'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el precio'}))
    taste = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=choices)
    persons = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=choices)
    details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Curso
        fields = ['title', 'image', 'categories', 'location', 'price', 'taste', 'persons', 'details']

