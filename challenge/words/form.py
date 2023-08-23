from django import forms


class AlphaWordForm(forms.Form):
    text = forms.CharField(
        label="", required=True, widget=forms.Textarea(attrs={"class": "form-control"})
    )
