from django import forms
from .models import contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter your full name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['subject'].widget.attrs['placeholder'] = 'Enter your subject'
        self.fields['message'].widget.attrs['placeholder'] = 'Write your message'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'