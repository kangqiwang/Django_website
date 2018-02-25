from django.shortcuts import render, HttpResponse
from firstapp.models import Product
# Create your views here.
def first(request):
	content={}
	products=Product.objects.all()
	content["products"]=products
	return render(request, "index.html",content)
	