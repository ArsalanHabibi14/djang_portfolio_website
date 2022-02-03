from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(
        label='Full Name',
        widget=forms.TextInput(
            attrs={'id': 'form_name', 'name': 'name', 'class': 'form-control',
                   'data-error': 'Name is required'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={'id': 'form_email', 'name': 'email', 'class': 'form-control',
                   'data-error': 'email is required'})
    )
    message = forms.CharField(
        label="Message for Me",
        widget=forms.Textarea(
            attrs={'id': 'form_message', 'name': 'message', 'class': 'form-control',
                   'data-error': 'Please, leave a message', 'rows': '4'}
        )
    )
