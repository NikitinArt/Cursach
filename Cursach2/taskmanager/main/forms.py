from .models import Invest
from django.forms import ModelForm, TextInput, NumberInput


class InvestForm(ModelForm):
    class Meta:
        model = Invest
        fields = ["name", "old_price", "new_price", "growth", "recommendations"]
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите название инвестиции"
            }),
            "old_price": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Введите нынешнюю цену акций"
            }),
            "new_price": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Введите новую цену акций"
            }),
            "growth": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Введите рост акций в %",
                "step": "any"
            }),
            "recommendations": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите рекомендации по инвестиции"
            })
        }