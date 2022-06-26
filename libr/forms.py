from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Library, User

class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = '__all__'


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user