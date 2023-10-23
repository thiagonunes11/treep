from django import forms
from .models import Roteiro,Natureza, Gastronomia,Praia,Cultura 
from django.utils import timezone as tz
from django.utils import datetime_safe
from django.core.exceptions import ValidationError
from datetime import datetime

class RoteiroForm(forms.ModelForm):
    
    natureza = forms.ModelMultipleChoiceField(queryset=Natureza.objects.all(), widget=forms.CheckboxSelectMultiple,required=False)
    gastronomia = forms.ModelMultipleChoiceField(queryset=Gastronomia.objects.all(), widget=forms.CheckboxSelectMultiple,required=False)
    praia = forms.ModelMultipleChoiceField(queryset=Praia.objects.all(),widget=forms.CheckboxSelectMultiple,required=False)
    cultura = forms.ModelMultipleChoiceField(queryset=Cultura.objects.all(),widget=forms.CheckboxSelectMultiple,required=False)
    def clean(self, *args, **kwargs):
    
        cleaned_data =  super().clean(*args, **kwargs)

        data = cleaned_data.get('data')

        # Obter a data atual
        data_atual = datetime.today()

        # Formatar a data para mostrar apenas o ano, mês e dia
        data_formatada = data_atual.strftime('%Y-%m-%d')

        print(data_formatada)

        if str(data) < data_formatada:
            raise ValidationError('Start time must be later than now.')

        
    class Meta:
        model = Roteiro
        fields = '__all__'
        data = forms.DateField()
        #fields = ['nome','posicao','gastronomia','praia']
        #nome = forms.CharField(widget=forms.TextInput(attrs={'class':'special'}))
        #widgets  =  { 'praia': forms.Select(attrs = {'onchange' : "Mudarestado();"}) }
        
