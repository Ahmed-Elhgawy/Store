from django.urls import path
from django.contrib.auth.decorators import login_required
from store.views import index, storeApp, smartPhoneStore, electricalDevicesStore, furnitureStore, clothesStore, add_to_cart, remove_from_cart, view_cart, increase_quantity, decrease_quantity, user_signup, user_login, user_logout, address, visa, clear_cart, save_order

urlpatterns = [
    path('', index, name='home'),
    path('accounts/login/', user_login, name='login'),
    path('register/', user_signup, name='register'),
    path('store/', storeApp, name='store'),
    path('logout/', user_logout, name='logout'),
    path('store/smartPhones/', smartPhoneStore, name='smart phone'),
    path('store/electricaldevices/', electricalDevicesStore, name='electrical device'),
    path('store/furniture/', furnitureStore, name='furniture'),
    path('store/clothes/', clothesStore, name='clothes'),
    path('store/cart/', view_cart, name='cart'),
    path('add/<int:id>', add_to_cart, name='add'),
    path('remove/<int:id>', remove_from_cart, name='remove'),
    path('increase/<int:id>', increase_quantity, name='increase'),
    path('decrease/<int:id>', decrease_quantity, name='decrease'),
    path('store/cart/payment/', address, name='payment'),
    path('store/cart/payment/visa/', visa, name='visa'),
    path('clear/', clear_cart, name='clear'),
    path('save/', save_order, name='saveOrder'),
    ]
