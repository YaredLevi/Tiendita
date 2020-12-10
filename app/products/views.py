from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import PoleraForm
from cart.cart import Cart


# Create your views here.
@login_required(login_url='/autenticacion/acceder')
def listado_productos(request):
    cart = Cart(request)
    products = Product.objects.all()
    return render(request, "products/listado.html", {
        "products": products
    })
    
def read(request):
    producto = Product.objects.all()
    return render(request, "products/read.html", {
        "poleras": producto
    })
    
def agregar(request):

    data = {
        'form':PoleraForm()
    }
    
    if request.method == 'POST':
        formulario = PoleraForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['msg'] = "Guardado de forma exitosa."
            
    return render(request, "products/agregar.html", data)