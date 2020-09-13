from django import forms



class TodolistForm(forms.Form):
    text = forms.CharField(max_length=45,
                           widget=forms.TextInput(
                             attrs={'name': 'add_item', 'placeholder': 'Add new item'}))