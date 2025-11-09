from django.http import JsonResponse

import cart
from shop.models import Product
class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key']={}
        self.cart = cart

    def add(self, product,quantity):
        product_id=str(product.id)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]=int(quantity)
        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_products(self):
        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)
        return products

    def get_quantity(self):
        quantity=self.cart
        return quantity


    def update(self,product,quantity):
        product_id=str(product.id)
        if product_id in self.cart:
            self.cart[product_id]=int(quantity)
            self.session.modified = True

        var=self.cart
        return var

    def delete(self,product):
        product_id=str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True
        var=self.cart
        return var