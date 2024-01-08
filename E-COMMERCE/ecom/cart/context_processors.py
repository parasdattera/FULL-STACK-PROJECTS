from .cart import Cart

# create context processor so that our cart can work on all pages


def cart(request):
    # return default data from our cart
    return {'cart':Cart(request)}
    # now we need to let know our django settings.py file that this context processor exists