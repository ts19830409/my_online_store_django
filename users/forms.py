from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'
		self.fields['username'].label = 'Email'
		self.fields['password'].label = 'Пароль'


class UserRegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['email', 'password1', 'password2']
		labels = {'email': 'Электронная почта'}
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'
		
		self.fields['password1'].label = 'Пароль'
		self.fields['password2'].label = 'Подтверждение пароля'
		
		self.fields['password1'].help_text = None
		self.fields['password2'].help_text = None
