from django import forms
from .models import BinPackingDemo

class BinPackingDemoForm(forms.ModelForm):
    class Meta:
        model = BinPackingDemo
        fields = ['algorithm', 'bin_capacity', 'item_list']
        widgets = {
            'algorithm': forms.Select(attrs={'class': 'form-control'}),
            'bin_capacity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'item_list': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'e.g., 10, 20, 30'
            }),
        }
