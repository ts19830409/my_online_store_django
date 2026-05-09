from django.core.cache import cache
from catalog.models import Product


def get_products_by_category(category_id):
	cache_key = f'products_category_{category_id}'
	products = cache.get(cache_key)
	
	if products is None:
		#products = Product.objects.filter(category_id=category_id, is_published=True)
		products = Product.objects.filter(category_id=category_id)
		cache.set(cache_key, products, 60 * 15)  # кеш на 15 минут
	
	return products