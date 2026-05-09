from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.core.management import call_command
from django.db import connection


class Command(BaseCommand):
	help = 'Внесение данных в БД'
	
	def handle(self, *args, **options):
		self.stdout.write('Удаление существующих данных...')
		Category.objects.all().delete()
		Product.objects.all().delete()
		
		with connection.cursor() as cursor:
			cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1;")
			cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1;")
		
		self.stdout.write('Загрузка данных из фикстур...')
		call_command('loaddata', 'fixtures/category.json')
		call_command('loaddata', 'fixtures/product.json')
		
		self.stdout.write(self.style.SUCCESS('Данные успешно загружены!'))
