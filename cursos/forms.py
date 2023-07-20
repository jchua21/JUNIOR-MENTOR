from django import forms
from .models import Curso, Comment
from .snippets import choices

class CursoCreateForm(forms.ModelForm):
    title = forms.CharField(label="Título", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título'}))
    categories = forms.CharField(label="Categorías", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categorías separadas por coma. Ejemplo: chino, tailandés'}))
    image = forms.ImageField(label="Imagen", widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    location = forms.CharField(label="Ubicación", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la ubicación'}))
    price = forms.IntegerField(label="Precio", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el precio'}))
    taste = forms.ChoiceField(label="Gusto", widget=forms.Select(attrs={'class': 'form-control'}), choices=choices)
    persons = forms.IntegerField(
        label="Personas",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la cantidad de personas'}),
        min_value=0,
        max_value=100,
        error_messages={
            'min_value': 'El número de personas debe ser al menos 0.',
            'max_value': 'El número de personas no puede ser mayor que 100.'
        }
    )
    details = forms.CharField(label="Detalles", widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Curso
        fields = ['title', 'image', 'categories', 'location', 'price', 'taste', 'persons', 'details']

