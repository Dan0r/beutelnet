from django import forms

class SearchForm(forms.Form):
    search_term = forms.CharField(
        label="",
        max_length = 100,
        # Style with CSS using Django Widgets
        widget=forms.TextInput(attrs={
            "type":"search",
            "placeholder":"Name Ihres Staubsaugers",
            "autofocus":True,
        })
    )

