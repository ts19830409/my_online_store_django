from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from catalog.models import Contact, Product
from catalog.forms import ProductForm


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


def products_list(request):
	products = Product.objects.all()
	context = {'products': products}
	return render(request, 'products_list.html', context)


def products_detail(request, pk):
	products = get_object_or_404(Product, pk=pk)
	context = {'product': products}
	return render(request, 'products_detail.html', context)


def product_add(request):
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('catalog:products_list')
	else:
		form = ProductForm()
		
	return render(request, 'product_add.html', {'form': form})
