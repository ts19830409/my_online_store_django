from django.shortcuts import render
from django.http import HttpResponse

def catalog(request):
	"""Отображение страницы'Каталог'"""
	return render(request, 'catalog.html')

def contacts(request):
	"""Отображение страницы 'Контакты'"""
	if request.method == "POST":
		name = request.POST.get("name")
		phone = request.POST.get("phone")
		message = request.POST.get("message")
		
		print(f"Получено сообщение от {name}, телефон: {phone}, сообщение: '{message}'")
		return HttpResponse(f"Спасибо за обратную связь, {name}. Сообщение получено!")
	
	return render(request, 'contacts.html')