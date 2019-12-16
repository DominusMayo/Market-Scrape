from django import forms

class PriceSelection(forms.Form):
    min_price= forms.FloatField(min_value=0, help_text='Минимальная цена', max_value=1000000)
    max_price = forms.FloatField(min_value=0, help_text='Максимальная ценв', max_value=1000000)
    
