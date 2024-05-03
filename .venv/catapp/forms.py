from django import forms
from .models import Cat


class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['name', 'image', 'rarity', 'description']

    name = forms.CharField(
        max_length=100,
        required=True,
        label='Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter the name here',
                'class': 'mycssclass',
                'id': 'myid',
            }
        )
    )

    image = forms.ImageField(
        required=True,
        label='Image'
    )

    rarity = forms.CharField(
        max_length=20,
        required=True,
        label='Rarity'
    )

    description = forms.CharField(
        required=True,
        label='Description',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter the description here',
                'class': 'mycssclass',
                'id': 'myid',
                'rows': 3,
            }
        )
    )