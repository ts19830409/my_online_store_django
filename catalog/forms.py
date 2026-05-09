from django import forms
from django.core.exceptions import ValidationError

from .models import Product
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно',
                   'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['name', 'description', 'photo', 'category', 'price']
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			if field_name == 'category':
				field.widget.attrs['class'] = 'form-select'
			else:
				field.widget.attrs['class'] = 'form-control'
	
	def clean_name(self):
		name = self.cleaned_data.get('name')
		for word in FORBIDDEN_WORDS:
			if word in name.lower():
				raise ValidationError(f"Название содержит запрещенное слово {word}")
		return name
	
	def clean_description(self):
		description = self.cleaned_data.get('description')
		for word in FORBIDDEN_WORDS:
			if word in description.lower():
				raise ValidationError(f"Описание содержит запрещенное слово {word}")
		return description
	
	def clean_price(self):
		price = self.cleaned_data.get('price')
		if price < 0:
			raise ValidationError("Цена не может быть отрицательной")
		return price
	
	def clean_photo(self):
		photo = self.cleaned_data.get('photo')
		if photo:
			if photo.size > 5 * 1024 * 1024:
				raise ValidationError('Размер файла не должен превышать 5 МБ')
			
			if not photo.name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
				raise ValidationError('Неверный формат. Допустимые значения: jpg, jpeg, png, gif')
		return photo
	
	def save(self, commit=True):
		product = super().save(commit=False)
		
		# Обрабатываем фото, если оно загружено
		if self.cleaned_data.get('photo'):
			img = Image.open(self.cleaned_data['photo'])
			img.thumbnail((400, 400), Image.Resampling.LANCZOS)
			
			ext = self.cleaned_data['photo'].name.split('.')[-1].upper()
			if ext in ('JPG', 'JPEG'):
				fmt = 'JPEG'
			elif ext == 'PNG':
				fmt = 'PNG'
			elif ext == 'GIF':
				fmt = 'GIF'
			else:
				fmt = 'JPEG'
			
			img_io = BytesIO()
			img.save(img_io, format=fmt, quality=85)
			
			product.photo.save(
				self.cleaned_data['photo'].name,
				ContentFile(img_io.getvalue()),
				save=False
			)
		
		if commit:
			product.save()
		return product
