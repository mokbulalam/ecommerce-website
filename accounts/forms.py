from django.contrib.auth import get_user_model
User = get_user_model()

from django import forms

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
	username 	= forms.CharField()
	email 		= forms.EmailField()
	password 	= forms.CharField(widget=forms.PasswordInput)
	confirm_password 	= forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data.get('username')
		username_queryset = User.objects.filter(username=username)
		if username_queryset.exists():
			raise forms.ValidationError("Username is already taken!")
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_queryset = User.objects.filter(email=email)
		if email_queryset.exists():
			raise forms.ValidationError("Email is already taken!")
		return email

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
		if password != confirm_password:
			raise forms.ValidationError("Passwords must match!")
		return data
