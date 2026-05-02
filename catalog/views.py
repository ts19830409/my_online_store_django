from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Contact, Product, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.forms import ProductForm


class CatalogView(TemplateView):
	template_name = 'products/catalog.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		return context


class ContactsView(TemplateView):
	template_name = 'products/contacts.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['contacts'] = Contact.objects.all()
		return context
	
	def post(self, request, *args, **kwargs):
		name = request.POST.get("name")
		phone = request.POST.get("phone")
		message = request.POST.get("message")
		print(f"Получено сообщение от {name}, телефон: {phone}, сообщение: '{message}'")
		return HttpResponse(f"Спасибо за обратную связь, {name}. Сообщение получено!")


class ProductListView(ListView):
	model = Product
	template_name = 'products/product_list.html'
	
	def get_queryset(self):
		queryset = Product.objects.all()
		category_id = self.request.GET.get('category')  # ← берем параметр из URL
		if category_id:
			queryset = queryset.filter(category_id=category_id)
		return queryset


class ProductDetailView(LoginRequiredMixin, DetailView):
	model = Product
	template_name = 'products/product_detail.html'
	success_url = reverse_lazy('catalog:product_list')


class ProductCreateView(LoginRequiredMixin, CreateView):
	model = Product
	template_name = 'products/product_form.html'
	# fields = ("name", "description", "photo", "category", "price")
	form_class = ProductForm
	success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
	model = Product
	template_name = 'products/product_form.html'
	# fields = ("name", "description", "photo", "category", "price")
	form_class = ProductForm
	success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
	model = Product
	template_name = 'products/product_delete.html'
	success_url = reverse_lazy('catalog:product_list')
