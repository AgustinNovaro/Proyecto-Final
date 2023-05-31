from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        # fields = ('nombre', 'sabor', 'ingredientes', 'instrucciones', 'tiempo_preparacion', 'dificultad', 'num_porciones', 'imagen')
        fields = ('nombre', 'sabor', 'ingredientes', 'instrucciones', 'tiempo_preparacion', 'dificultad', 'num_porciones')
    
    
        widgets = {
            'nombre': forms.TextInput(attrs={'required': False}),
            'sabor': forms.TextInput(attrs={'required': False}),
            # Agrega más campos y widgets aquí
        }
