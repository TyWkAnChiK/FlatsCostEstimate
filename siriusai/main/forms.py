from .models import question
from django.forms import ModelForm, TextInput, Select, ChoiceField
class questionForm(ModelForm):
    class Meta:
        model = question
        fields = [
            'metro_station',
            'minutes_to_metro',
            'number_of_rooms',
            'all_area',
            'living_area',
            'kitchen_area',
            'floor',
            'number_of_floors',
            'renovations'
        ]

        widgets = {
            "metro_station" : TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ближайшая станция метро'
            }),
            "minutes_to_metro": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время ходьбы до метро(в минутах)'
            }),
            "number_of_rooms": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество комнат'
            }),
            "all_area": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Общая площадь(в кв. метрах)'
            }),
            "living_area": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Жилая площадь(в кв. метрах)'
            }),
            "kitchen_area": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Площадь кухни(в кв. метрах)'
            }),
            "floor": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Этаж'
            }),
            "number_of_floors": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество этажей в доме'
            }),
            "renovation": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ремонт(\'дизайнерский\'/\'евро\'/\'без ремонта\'/\'косметический\')'
            }),
            "renovations": Select(
                attrs={
                    'class': 'form-control'
                },
                choices=(
                    ("Designer", "дизайнерский"),
                    ("Without renovation", "без ремонта"),
                    ("European-style renovation", "евро-ремонт"),
                    ("Cosmetic", "косметический"))
            )
        }
