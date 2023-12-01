from django.contrib import admin
from store.models import Product, ProductClass, Cart, CartItem, UserAddress, UserVisa, OrderInfo
# Register your models here.


admin.site.register(Product)
admin.site.register(ProductClass)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(UserAddress)
admin.site.register(UserVisa)
admin.site.register(OrderInfo)
