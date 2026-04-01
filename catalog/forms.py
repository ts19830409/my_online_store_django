from django import forms
from .models import Product
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['name', 'description', 'photo', 'category', 'price']
	
	def save(self, commit=True):
		product = super().save(commit=False)
		
		# Обрабатываем фото, если оно загружено
		if self.cleaned_data.get('photo'):
			img = Image.open(self.cleaned_data['photo'])
			img.thumbnail((400, 400), Image.Resampling.LANCZOS)
			
			img_io = BytesIO()
			img.save(img_io, format='JPG, JPEG, PNG, GIF', quality=85)
			
			product.photo.save(
				self.cleaned_data['photo'].name,
				ContentFile(img_io.getvalue()),
				save=False
			)
		
		if commit:
			product.save()
		return product
