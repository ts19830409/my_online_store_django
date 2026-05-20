from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.conf import settings
from users.models import User
from users.forms import UserRegisterForm
from django.core.mail import send_mail


class RegisterView(CreateView):
	model = User
	form_class = UserRegisterForm
	template_name = 'users/register.html'
	success_url = reverse_lazy('users:login')
	
	def form_valid(self, form):
		user = form.save()
		self.send_welcome_email(user.email)
		return super().form_valid(form)
	
	def send_welcome_email(self, user_email):
		subject = "Добро пожаловать в наш магазин"
		message = "Благодарим за регистрацию"
		from_email = settings.DEFAULT_FROM_EMAIL
		recipient_list = [user_email, ]
		send_mail(subject, message, from_email, recipient_list)
