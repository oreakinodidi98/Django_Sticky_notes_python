from django import forms
from .models import Stick_notes, Author

# form for creating notes
class Stick_notesForm(forms.ModelForm):
    class Meta:
        model = Stick_notes
        fields = ('title', 'content', 'author')

# form for sighning in user
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name','username', 'email', 'password', 'date_of_birth')
        widgets = {
            'password': forms.PasswordInput(),
            'date_of_birth': forms.DateInput()
        }