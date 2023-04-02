from django import forms
from .models import Quote, Person

class QuoteForm(forms.ModelForm):
    person = forms.ModelChoiceField(queryset=Person.objects.all())

    class Meta:
        model = Quote
        fields = ('content', 'person',)