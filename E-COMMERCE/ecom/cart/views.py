from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
# Create your views here.

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    return render(request,"cart_summary.html",{"cart_products":cart_products,"quantities":quantities})


def cart_add(request):
    # get the cart
    cart = Cart(request)
    # if post
    if request.POST.get('action') == 'post':
        #get the data
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        #look for the product in database
        product = get_object_or_404(Product,id= product_id)
        # save to session
        cart.add(product=product,quantity=product_qty)

        # get cart quantity
        cart_quantity = cart.__len__()
        #return response
        # response = JsonResponse({'Product Name:':product.name})
        response = JsonResponse({'qty':cart_quantity})
        return response
    


def cart_delete(request):
    pass


def cart_update(request):
    pass