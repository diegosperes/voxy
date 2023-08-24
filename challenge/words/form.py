from django import forms


class WordForm(forms.Form):
    text = forms.CharField(
        label="", required=True, widget=forms.Textarea(attrs={"class": "form-control"})
    )
