from django.db import models


class Category(models.Model):
	"""Класс Category"""
	
	name = models.CharField(max_length=150, verbose_name="Наименование категории")
	description = models.TextField(
		verbose_name="Описание категории", blank=True, null=True
	)
	
	def __str__(self):
		"""Строковое представление категории"""
		return self.name
	
	class Meta:
		verbose_name = "категория"
		verbose_name_plural = "категории"
		ordering = [
			"name",
		]


class Product(models.Model):
	"""Класс Product"""
	
	name = models.CharField(max_length=150, verbose_name="Наименование продукта")
	description = models.TextField(verbose_name="Описание продукта")
	photo = models.ImageField(
		upload_to="products",
		blank=True,
		null=True,
		verbose_name="Изображение продукта",
	)
	
	category = models.ForeignKey(
		Category,
		on_delete=models.CASCADE,
		blank=True,
		null=True,
		verbose_name="Категория продукта",
		related_name="products",
	)
	price = models.DecimalField(
		max_digits=10, decimal_places=2, verbose_name="Цена продукта"
	)
	created_at = models.DateTimeField(
		verbose_name="Дата создания записи", auto_now_add=True
	)
	updated_at = models.DateTimeField(verbose_name="Дата изменения записи", auto_now=True)
	
	def __str__(self):
		"""Строковое представление продукта"""
		return self.name
	
	class Meta:
		verbose_name = "продукт"
		verbose_name_plural = "продукты"
		ordering = [
			"name",
		]


class Contact(models.Model):
	name = models.CharField(max_length=100, verbose_name='Контактное лицо')
	email = models.EmailField(max_length=100, verbose_name='Адрес электронной почты')
	phone = models.CharField(max_length=20, verbose_name='Номер телефона')
	address = models.TextField(verbose_name='Адрес')
	
	def __str__(self):
		"""Строковое представление контакта"""
		return self.name
	
	class Meta:
		verbose_name = "контакт"
		verbose_name_plural = "контакты"
		
	
