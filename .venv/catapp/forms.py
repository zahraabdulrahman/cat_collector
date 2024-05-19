from django import forms
from .models import Cat

class CatForm(forms.ModelForm):
    RARITY_CHOICES = [
        ('Common', 'Common'),
        ('Uncommon', 'Uncommon'),
        ('Rare', 'Rare'),
        ('Legendary', 'Legendary'),
    ]

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

    rarity = forms.ChoiceField(
        choices=RARITY_CHOICES,
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

    class Meta:
        model = Cat
        fields = ['name', 'image', 'rarity', 'description']
