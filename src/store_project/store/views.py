from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, Cart, CartItem, UserAddress, UserVisa, OrderInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from store.forms import UserCreationForm, LoginForm, ProfileFrom, VisaForm
# from django.views.generic.edit import CreateView
# Create your views here.


def index(request):
    return render(request, "store/index.html")


# register page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.htm', {'form': form})


# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('/store/')
    else:
        form = LoginForm()
    return render(request, 'store/login.htm', {'form': form})


# logout page
def user_logout(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/accounts/login/')
def storeApp(request):
    phones = Product.objects.filter(product_class__product_class__contains='Smart phone')
    devices = Product.objects.filter(product_class__product_class__contains='Household Devices')
    furniture = Product.objects.filter(product_class__product_class__contains='Furniture')
    clothes = Product.objects.filter(product_class__product_class__contains='Clothes')
    user_name = request.user.username
    context = {
        'class_1': phones,
        'class_2': devices,
        'class_3': furniture,
        'class_4': clothes,
        'user_name': user_name
    }
    return render(request, 'store/store.htm', context=context)


@login_required(login_url='/accounts/login/')
def smartPhoneStore(request):
    phones = Product.objects.filter(product_class__product_class__contains='Smart phone')
    context = {
        'class_1': phones
    }
    return render(request, 'store/phones.htm', context=context)


@login_required(login_url='/accounts/login/')
def electricalDevicesStore(request):
    devices = Product.objects.filter(product_class__product_class__contains='Household Devices')
    context = {
        'class_2': devices
    }
    return render(request, 'store/devices.htm', context=context)


@login_required(login_url='/accounts/login/')
def furnitureStore(request):
    furniture = Product.objects.filter(product_class__product_class__contains='Furniture')
    context = {
        'class_3': furniture
    }
    return render(request, 'store/furnitures.htm', context=context)


@login_required(login_url='/accounts/login/')
def clothesStore(request):
    clothes = Product.objects.filter(product_class__product_class__contains='Clothes')
    context = {
        'class_4': clothes
    }
    return render(request, 'store/clothes.htm', context=context)


@login_required(login_url='/accounts/login/')
def add_to_cart(request, id):
    product = Product.objects.get(pk=id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url='/accounts/login/')
def remove_from_cart(request, id):
    cart = Cart.objects.get(user=request.user)
    product = Product.objects.get(pk=id)
    cart.remove_from_cart(product)
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url='/accounts/login/')
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_price': total_price})


@login_required(login_url='/accounts/login/')
def increase_quantity(request, id):
    cart = Cart.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.increase_quantity()
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url='/accounts/login/')
def decrease_quantity(request, id):
    cart = Cart.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.decrease_quantity()
    return redirect(request.META.get('HTTP_REFERER', '/'))


# class Payment(CreateView):
#     login_required = True
#     model = UserAddress
#     form_class = ProfileFrom
#     template_name = "store/payment.htm"
#     success_url = '/store/cart/payment/visa/'


@login_required(login_url='/accounts/login/')
def address(request):
    if request.POST:
        address = UserAddress()
        address.email = request.POST["email"]
        address.phone = request.POST["phone"]
        address.country = request.POST["country"]
        address.state = request.POST["state"]
        address.city = request.POST["city"]
        address.address = request.POST["address"]
        address.save()
        return redirect('/store/cart/payment/visa/')
    myform = ProfileFrom()
    return render(request, "store/payment.htm", context={'form': myform})
    

# class Visa(CreateView):
#     login_required = True
#     model = UserVisa
#     form_class = VisaForm
#     template_name = "store/visa.htm"
#     success_url = '/adduserinfo/'


@login_required(login_url='/accounts/login/')
def visa(request):
    if request.POST:
        visa = UserVisa()
        visa.name = request.POST["name"]
        visa.cardnumber = request.POST["cardnumber"]
        visa.expirationdate = request.POST["expirationdate"]
        visa.securitycode = request.POST["securitycode"]
        visa.save()
        return redirect('/save/')
    myform = VisaForm()
    return render(request, "store/visa.htm", context={'form': myform})


@login_required(login_url='/accounts/login/')
def clear_cart(request):
    cart = CartItem.objects.all().delete()
    user_address = UserAddress.objects.all().delete()
    user_visa = UserVisa.objects.all().delete()    
    return redirect('/store/')


def save_order(request):
    order_info = OrderInfo()

    user_address = UserAddress.objects.all()
    for i in user_address :
        order_info.email = i.email
        order_info.phone = i.phone
        order_info.country = i.country
        order_info.state = i.state
        order_info.city = i.city
        order_info.address = i.address

    user_visa = UserVisa.objects.all()
    for i in user_visa :
        order_info.name = i.name
        order_info.cardnumber = i.cardnumber
        order_info.expirationdate = i.expirationdate
        order_info.securitycode = i.securitycode
 
    cart_items = CartItem.objects.all()
    
    name = []
    price = []
    quantity = []
    for i in cart_items :
        name.append(i.product.name)
        price.append(i.product.price)
        quantity.append(i.quantity)
    products = f'{name}\n{price}\n{quantity}'
    order_info.products = products

    order_info.save()

    return redirect('/clear/')
