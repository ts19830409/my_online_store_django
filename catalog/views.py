from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Contact, Product


def catalog(request):
	"""Отображение страницы'Каталог'"""
	latest_products = Product.objects.all().order_by('-created_at')[:5]
	print("Последние 5 продуктов:")
	for product in latest_products:
		print(f"- {product.name} ({product.price} руб.)")
	
	return render(request, 'catalog.html')


def contacts(request):
	"""Отображение страницы 'Контакты'"""
	if request.method == "POST":
		name = request.POST.get("name")
		phone = request.POST.get("phone")
		message = request.POST.get("message")
		
		print(f"Получено сообщение от {name}, телефон: {phone}, сообщение: '{message}'")
		return HttpResponse(f"Спасибо за обратную связь, {name}. Сообщение получено!")
	
	contacts = Contact.objects.all()
	return render(request, 'contacts.html', {'contacts': contacts})
