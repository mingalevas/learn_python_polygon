from django import forms


class NameForm(forms.Form):
    term_one = forms.IntegerField(label='term one')
    term_two = forms.IntegerField(label='term two')
