from django import forms


class BuyForm(forms.Form):
    bank = forms.CharField()
    money = forms.IntegerField()



