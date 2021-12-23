from django import forms

class SearchForm(forms.Form):
    brand = forms.CharField(label="Brand Name", max_length=100)
    category = forms.CharField(label="Type of Garment", max_length=100)
    keyword = forms.CharField(label="Search keyword", max_length=100, required=False)