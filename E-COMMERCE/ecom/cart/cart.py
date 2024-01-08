from store.models import Product

class Cart():
    def __init__(self,request):
        #get session data from user request
        self.session= request.session
        #get the session key from user if exists means if he logged in previously then only
        cart = self.session.get('session_key')
        #if user is new then no session key! , creating one!
        if 'session_key' not in request.session:
            cart = self.session['session_key']={}

        #using context processor so that cart system able to work on all pages of site as user logged in
        
        # as we already get the session key in cart variable so we create a attribute of the Cart class
        self.cart = cart

    def add(self,product,quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id]={'price':str(product.price)}
            self.cart[product_id]=int(product_qty)

        self.session.modified = True


    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        # get ids from cart
        product_ids = self.cart.keys()
        # use ids to lookup products in database models
        products = Product.objects.filter(id__in = product_ids)
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities