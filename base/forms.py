from django import forms

class PaymentForm(forms.Form):
    amount = forms.DecimalField(
        max_digits=10, decimal_places=2, widget=forms.HiddenInput()
    )
    card_holder_first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Imię'})
    )
    card_holder_last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'})
    )
    card_number = forms.CharField(
        max_length=16,
        widget=forms.TextInput(attrs={'placeholder': 'Numer Karty'})
    )
    card_expiry = forms.CharField(
        max_length=5,
        widget=forms.TextInput(attrs={'placeholder': 'Data Ważności'})
    )
    card_cvc = forms.CharField(
        max_length=3,
        widget=forms.TextInput(attrs={'placeholder': 'CVC'})
    )
